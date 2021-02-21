from ply import yacc, lex
import lexer
import json
import argparse
tokens = lexer.tokens


def toIntIfInt(x):
    return int(x) if x % int(x) == 0 else x

owotypes = {}
owotypes[int] = 'waifu'
owotypes[float] = 'waifu'
owotypes[bool] = 'catgirl'

class ScopedMap():

    def __init__(self):
        self.scopes = [{}]

    def addScope(self):
        self.scopes.append({})

    def popScope(self):
        self.scopes.pop()

    def __contains__(self, key):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                return True
        return False

    def inCurrentScope(self, key):
        return key in self.scopes[-1]

    def __getitem__(self, key):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                return self.scopes[i][key]
        return None

    def __setitem__(self, key, val):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                self.scopes[i][key] = val
        self.scopes[-1][key] = val

    def getScopeIndex(self, key):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                return i
        return None

    def inScopeIndex(self, index, key):
        return key in self.scopes[index]

    def forceNew(self, key, val):
        self.scopes[-1][key] = val

    def __delitem__(self, key):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                del self.scopes[i][key]

    def __str__(self) -> str:
        return str(self.scopes)

    def toJSON(self):
        return json.dumps(self.scopes, indent=4)


# scopes = []
# scopes.append({"lets": {}, "consts": {}, "fns": {}})
lets = ScopedMap()
consts = ScopedMap()
fns = ScopedMap()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)


def p_statement(t):
    ''' statement : expr SEMICOL
                  | assignment SEMICOL
                  | declaration SEMICOL
                  | statement statement
                  | functionDef
                  | whileLoop
                  | forLoop
    '''
    t[0] = t[1::]


def p_expr(t):
    '''expr : numExpr
            | boolExpr
            | reference
            | functionCall
    '''
    t[0] = t[1]


def p_assignment(t):
    '''assignment : reassign
                  | initialize
                  | arrayAssign
    '''
    t[0] = t[1]


def p_reassign(t):
    ''' reassign : ID EQ expr
    '''
    _, name, _, val = t
    if (name in lets and name not in consts):
        typeVal = lets[name]['type']
        if owotypes[type(val)] == typeVal:
            t[0] = [name, '=', val]
            lets[name]["val"] = val
        else: 
            print("Incorrect type for %s, expecting type %s given type %s", name, typeVal, owotypes[type(val)])
    else:
        if (name in lets):
            if (consts.inScopeIndex(lets.getScopeIndex(name), name)):
                print("Cannot reassign constant")
            else:
                typeVal = lets[name]['type']
                if owotypes[type(val)] == typeVal:
                    t[0] = [name, '=', val]
                    lets[name]["val"] = val
                else: 
                    print("Incorrect type for %s, expecting type %s given type %s", name, typeVal, owotypes[type(val)])
        else:
            print("Variable {} not declared.".format(name))
        # error ehere

def p_shortbinop(t):
    ''' reassign : ID PEQ expr
                 | ID MEQ expr
                 | ID TEQ expr 
                 | ID DEQ expr
                 | ID PP
                 | ID MM
    '''
    if len(t) == 4:
        _, name, op, val = t
    else:
        _, name, op = t
        val = 1
    
    if (name in lets and name not in consts):
        typeVal = lets[name]['type']
        if 'waifu' == typeVal:
            if "+" in op:
                lets[name]["val"] += val
            elif "-" in op:
                lets[name]["val"] -= val
            elif "*" in op:
                lets[name]["val"] *= val
            elif "/" in op:
                 lets[name]["val"] /= val

            t[0] = [name, '=', lets[name]["val"]]
        else: 
            print("Incorrect type for %s, expecting type %s given type %s", name, typeVal, owotypes[type(val)])
    else:
        if (name in lets):
            if (consts.inScopeIndex(lets.getScopeIndex(name), name)):
                print("Cannot reassign constant")
            else:
                typeVal = lets[name]['type']
                if 'waifu' == typeVal:
                    if "+" in op:
                        lets[name]["val"] += val
                    elif "-" in op:
                        lets[name]["val"] -= val
                    elif "*" in op:
                        lets[name]["val"] *= val
                    elif "/" in op:
                        lets[name]["val"] /= val
                    t[0] = [name, '=', lets[name]["val"]]
                else: 
                    print("Incorrect type for %s, expecting type %s given type %s", name, typeVal, owotypes[type(val)])
        else:
            print("Variable {} not declared.".format(name))

def p_functionDef(t):
    ''' functionDef : newFn newScope LPAREN declarationLst RPAREN enclosure popScope
    '''
    _, fnName, _, _, args, _, enclosure, _ = t
    fns[fnName][1] = (args, enclosure)
    t[0] = (fnName, (args, enclosure))


def p_enclosure(t):
    ''' enclosure : LBRACE RBRACE
                  | LBRACE statement RBRACE
    '''
    if len(t) == 3:
        t[0] = None
    else:
        t[0] = t[2]


def p_newFn(t):
    'newFn : type SQUIGGLY honorific ID'
    _, typeVal, _, _, name = t
    fns.forceNew(name, [typeVal, None])
    t[0] = name


def p_newScope(t):
    'newScope : '
    lets.addScope()
    consts.addScope()
    fns.addScope()
    t[0] = None


def p_popScope(t):
    'popScope : '
    lets.popScope()
    consts.popScope()
    fns.popScope()
    t[0] = None


def p_honorific(t):
    ''' honorific : CHAN
                  | KUN
                  | SAN
                  | SAMA
    '''
    t[0] = t[1]


def p_arrayAssign(t):
    ''' arrayAssign : ID LBRACK NUMBER RBRACK EQ expr
    '''
    _, name, _, index, _, _, val = t
    if (name in lets):
        if (lets[name]['val'] != None):
            # if lets[name]["type"] == typeOf(val):
            if owotypes[type(val)] == lets[name]["type"]:
                t[0] = [name + ' harem', index, '=', val]
                lets[name]['val'][index] = val
            else: 
                print("Incorrect type for harem %s, expecting type %s given type %s", name, lets[name]["type"], owotypes[type(val)])
        else:
            print("Array uninitialized")
    else:
        print("Bad type")


def p_functionCall(t):
    ''' functionCall : print
                     | ID LPAREN exprLst RPAREN
                     | ID LPAREN RPAREN
    '''
    if len(t) == 2:
        t[0] = t[1]
    elif len(t) == 4:
        _, fnName, _, _ = t
        if (fnName in fns):
            # print('ok')
            # ok we need to make objects to store our data properly
            print("{} called with no args".format(fnName))
    else:
        _, fnName, _, args, _ = t
        # print('ok')
        print("{} called with args: {}".format(fnName, *args))
        # ok we need to make objects to store our data properly


def p_arrayLiteral(t):
    ''' arrayLiteral : LBRACK RBRACK
                     | LBRACK exprLst RBRACK
    '''
    if len(t) == 3:
        t[0] = []
    else:
        t[0] = t[2]


def p_exprList(t):
    ''' exprLst : expr
                | expr COMMA exprLst
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[3] + [t[1]]


def p_initialize(t):
    ''' initialize : letInitialize
                   | constInitialize
    '''
    t[0] = t[1]
    # else error


def p_letInitialize(t):
    ''' letInitialize : declaration EQ expr
                      | declaration EQ arrayLiteral
    '''
    typeVal, name = t[1][0:2]
    val = t[3]
    if owotypes[type(val)] == typeVal:
        t[0] = [name, '=', val]
        lets[name]["val"] = val
    else: 
        print("Incorrect type for %s, expecting type %s given type %s", name, typeVal, owotypes[type(val)])


def p_constInitialize(t):
    ''' constInitialize : const_declaration EQ expr
    '''
    typeVal, name = t[1][0:2]
    val = t[3]
    # if (typeOf(val) == typeVal):
    if owotypes[type(val)] == typeVal:
        t[0] = [name, '=', val]
        lets[name]["val"] = val
    else: 
        print("Incorrect type for %s, expecting type %s given type %s", name, typeVal, owotypes[type(val)])


def p_declaration(t):
    ''' declaration : array_declaration
                    | let_declartion
    '''
    # note const declaration cannot go here, we have to assign when we do that
    t[0] = t[1]


def p_declarationLst(t):
    '''declarationLst : declaration
                      | declaration COMMA declarationLst
                      | 
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        if len(t) == 1:
            t[0] = []
        else:
            t[0] = t[3] + [t[1]]


def p_const_declaration(t):
    '''const_declaration : REAL array_declaration
                         | REAL let_declartion
    '''
    _, name = t[2]
    t[0] = t[2] + ['const']
    consts.forceNew(name, True)


def p_array_declaration(t):
    'array_declaration : type HAREM ID'
    _, typeVal, _,  name = t
    t[0] = [typeVal + ' harem', name]
    if (not lets.inCurrentScope(name) and not fns.inCurrentScope(name)):
        lets.forceNew(name, {
            "type": typeVal,
            "array": True,
            "val": None
        })
    else:
        print("{} has already been declared.".format(name))


def p_let_declaration(t):
    '''let_declartion : type ID'''

    _, typeVal, name = t
    t[0] = [typeVal, name]
    if (not lets.inCurrentScope(name) and not fns.inCurrentScope(name)):
        lets.forceNew(name, {"type": typeVal, "array": False, "val": None})
    else:
        print("{} has already been declared.".format(name))


def p_type(t):
    '''type : WAIFU
            | CATGIRL
    '''
    t[0] = t[1]


def p_boolExpr_op(t):
    ''' boolExpr : expr NEQ expr
                 | numExpr LEQ numExpr
                 | numExpr GEQ numExpr
                 | numExpr LT numExpr
                 | numExpr GT numExpr
                 | expr EQOP expr
                 | boolExpr AND boolExpr
                 | boolExpr OR boolExpr
    '''
    _, a, op, b = t
    options = {'<': lambda x, y: x < y,
               '>': lambda x, y: x > y,
               '>=': lambda x, y: x >= y,
               '<=': lambda x, y: x <= y,
               '==': lambda x, y: x == y,
               '!=': lambda x, y: x != y,
               '&&': lambda x, y: x and y,
               '||': lambda x, y: x or y
               }
    t[0] = options[op](a, b)


def p_boolExprNeg(t):
    'boolExpr : NOT boolExpr'
    t[0] = not t[2]


def p_boolExpr_group(t):
    '''boolExpr : LPAREN boolExpr RPAREN
    '''
    t[0] = t[2]


def p_bool(t):
    ''' boolExpr : OWO
                 | UWU
    '''
    t[0] = True if t[1] == 'uwu' else False


def p_numExpr_binop(t):
    '''numExpr : numExpr PLUS numExpr
                  | numExpr MINUS numExpr
                  | numExpr TIMES numExpr
                  | numExpr DIVIDE numExpr'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]


def p_numExpr_uminus(t):
    'numExpr : MINUS numExpr %prec UMINUS'
    t[0] = -t[2]


def p_numExpr_group(t):
    'numExpr : LPAREN numExpr RPAREN'
    t[0] = t[2]


def p_numExpr_number(t):
    'numExpr : NUMBER'
    t[0] = t[1]


def p_numExpr_reference(t):
    'numExpr : letReference'
    t[0] = t[1]


def p_boolExpr_reference(t):
    'boolExpr : letReference'
    t[0] = t[1]


def p_reference(t):
    '''reference : letReference
                 | arrayReference
    '''
    t[0] = t[1]


def p_whileLoop(t):
    '''whileLoop : WHILEU LPAREN boolExpr RPAREN ISTUDIED newScope enclosure popScope
    '''
    _, _, _, cond, _, _, _, statements, _ = t
    print("While loop with condition {} created".format(cond))


def p_forLoop(t):
    '''forLoop : SHI newScope LPAREN forTrio RPAREN enclosure popScope
               | SHI newScope LPAREN forElement RPAREN enclosure popScope
    '''
    _, _, _, _, cond, _, statements, _ = t
    print("For loop with condition {} created".format(cond))


def p_forTrio(t):
    ''' forTrio : letInitialize SEMICOL boolExpr SEMICOL reassign
                | letInitialize SEMICOL boolExpr SEMICOL arrayAssign
                | arrayAssign SEMICOL boolExpr SEMICOL arrayAssign
    '''
    t[0] = [t[1], t[3], t[5]]


def p_forElement(t):
    ''' forElement : declaration COL ID
                   | const_declaration COL ID
    '''
    #  need to error check
    t[0] = [t[1], t[3]]


def p_letReference(t):
    '''letReference : ID'''
    _, name = t
    try:
        if (name in lets):
            t[0] = lets[name]["val"]
    except IndexError:
        print("Undefined name '%s'" % t[1])
        t[0] = None


def p_print(t):
    '''print : BAKA LPAREN exprLst RPAREN'''
    _, _, _, elements, _ = t
    print(*elements)
    t[0] = lambda: print(elements)


def p_arrayReference(t):
    ''' arrayReference : ID LBRACK NUMBER RBRACK '''
    _, name, _, index, _ = t
    try:
        if (name in lets):
            t[0] = lets[name]["val"][index]
        else:
            print("Undefined name '%s'" % t[1])
            t[0] = None
    except IndexError:
        print("Index out of bounds")
        t[0] = None


parser = yacc.yacc()

# if __name__ == "__main__":
#     argParser = argparse.ArgumentParser(
#         description='Take in the OwOScript source code and parse it into an AST.')
#     argParser.add_argument(
#         'FILE', help="Input file with OwOScript source code")
#     args = argParser.parse_args()

#     f = open(args.FILE, 'r')
#     data = f.read()
#     f.close()
#     parser.parse(data)

#     # Write output to a file
#     with open('output.json', 'w') as f:
#         f.write(json.dumps(fns.scopes, indent=2))
#     print("parsing complete")

x = parser.parse('''
    waifu x = 4;
    x++; x--; x*=2; x/=2; x+=4; x-=1;
''')
print(x)
print(fns)
print(lets)

# print(lets)
# while True:
#     try:
#         s = raw_input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
