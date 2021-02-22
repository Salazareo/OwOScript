from ply import yacc, lex
import lexer
import json
import argparse
tokens = lexer.tokens


def toIntIfInt(x):
    return int(x) if x % int(x) == 0 else x


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
    ''' statement : singleStatement
                  | statement statement
    '''
    t[0] = t[1::]


def p_singleStatement(t):
    ''' singleStatement : expr SEMICOL
                        | assignment SEMICOL
                        | declaration SEMICOL
                        | functionDef
                        | whileLoop
                        | forLoop
                        | if
                        | returnStatement SEMICOL
    '''
    t[0] = t[1]


def p_expr(t):
    ''' expr : ternaryOp
             | numExpr
             | boolExpr
             | reference
             | functionCall
             | arrayExpr
    '''
    t[0] = t[1]


def p_ternaryOp(t):
    ''' ternaryOp : boolExpr QMARK expr COL expr
    '''
    print("Ternary op with cond {} and exprs {} {}".format(t[1], t[3], t[5]))
    t[0] = t[1::]


def p_arrayExpr(t):
    '''arrayExpr : arrayLiteral
                 | letReference
    '''
    t[0] = t[1]


def p_assignment(t):
    '''assignment : reassign
                  | initialize
                  | arrayAssign
    '''
    t[0] = t[1]


def p_if(t):
    ''' if : ifAlone else
           | ifAlone
    '''
    t[0] = t[1]


def p_ifAlone(t):
    ''' ifAlone : NANI LPAREN boolExpr RPAREN newScope enclosure popScope
                | NANI LPAREN boolExpr RPAREN newScope singleStatement popScope
    '''
    t[0] = t[1]


def p_else(t):
    ''' else : NOU LPAREN boolExpr RPAREN newScope enclosure popScope
             | NOU LPAREN boolExpr RPAREN newScope singleStatement popScope
    '''
    t[0] = t[1]


def p_reassign(t):
    ''' reassign : ID EQ expr
    '''
    _, name, _, val = t
    if (name in lets and name not in consts):
        t[0] = [name, '=', val]
        lets[name]["value"] = val
    else:
        if (name in lets):
            if (consts.inScopeIndex(lets.getScopeIndex(name), name)):
                print("Cannot reassing constant")
            else:
                t[0] = [name, '=', val]
                lets[name]["value"] = val
        else:
            print("Variable {} not declared.".format(name))
        # error ehere


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


def p_returnStatement(t):
    ''' returnStatement : expr DESU
    '''
    print("returned {}".format(t[1]))
    t[0] = t[1]


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
            t[0] = [name + ' harem', index, '=', val]
            lets[name]['val'][index] = val
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
    '''
    print(t[1])
    name = t[1]["value"]["value"]
    typeName = t[1]["value"]["type"]
    val = t[3]
    # if (typeOf(val) == typeVal):
    t[0] = {"type": "initialize", "value": [
        {"type": typeName, "value": name}, '=', t[3]["value"]]}
    lets[name]["value"] = val
    # else error


def p_constInitialize(t):
    ''' constInitialize : const_declaration EQ expr
    '''
    typeVal, name = t[1][0:2]
    val = t[3]
    # if (typeOf(val) == typeVal):
    t[0] = [name, '=', val]
    lets[name]["value"] = val


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
            "value": None
        })
    else:
        print("{} has already been declared.".format(name))


def p_let_declaration(t):
    '''let_declartion : type ID'''

    _, typeVal, name = t
    t[0] = {"type": "declaration", "value": {
        "type": t[1]["value"], "value": t[2]}}
    if (not lets.inCurrentScope(name) and not fns.inCurrentScope(name)):
        lets.forceNew(name, {"type": typeVal, "array": False, "value": None})
    else:
        print("{} has already been declared.".format(name))


def p_type(t):
    '''type : WAIFU
            | CATGIRL
    '''
    t[0] = {"type": "typeName", "value": t[1]}


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
    if isinstance(t[1]["value"], (int, float, bool)) and isinstance(t[3]["value"], (int, float, bool)):
        t[0] = {"type": 'bool', "value": options[op](a, b)}
    else:
        t[0] = {"type": 'bool', "value": t[1::]}


def p_boolExprNeg(t):
    'boolExpr : NOT boolExpr'
    t[0] = {"type": 'bool', "value": t[1:3] if not isinstance(
        t[2]["value"], (bool)) else not t[2]["value"]}


def p_boolExpr_group(t):
    '''boolExpr : LPAREN boolExpr RPAREN
    '''
    t[0] = {"type": 'bool', "value": t[1::]}


def p_bool(t):
    ''' boolExpr : OWO
                 | UWU
    '''
    t[0] = {"type": "bool", "value": True if t[1] == 'uwu' else False}


def p_numExpr_binop(t):
    '''numExpr : numExpr PLUS numExpr
                  | numExpr MINUS numExpr
                  | numExpr TIMES numExpr
                  | numExpr DIVIDE numExpr'''
    if isinstance(t[1]["value"], (float, int)) and isinstance(t[3]["value"], (float, int)):
        if t[2] == '+':
            t[0] = {"type": "numExpr", "value": t[1]["value"] + t[3]["value"]}
        elif t[2] == '-':
            t[0] = {"type": "numExpr", "value": t[1]["value"] - t[3]["value"]}
        elif t[2] == '*':
            t[0] = {"type": "numExpr", "value": t[1]["value"] * t[3]["value"]}
        elif t[2] == '/':
            t[0] = {"type": "numExpr", "value": t[1]["value"] / t[3]["value"]}
    else:
        t[0] = {"type": "numExpr", "value": {
            "type": t[2], "value": [t[1]["value"], t[3]["value"]]}}


def p_numExpr_uminus(t):
    'numExpr : MINUS numExpr %prec UMINUS'
    t[0] = {"type": 'numExpr', "value": t[1:3]}


def p_numExpr_group(t):
    'numExpr : LPAREN numExpr RPAREN'
    t[0] = {"type": 'numExpr', "value": t[1::]}


def p_numExpr_number(t):
    'numExpr : NUMBER'
    t[0] = {"type": 'number', "value": t[1]}


def p_numExpr_reference(t):
    'numExpr : reference'
    t[0] = t[1]


def p_boolExpr_reference(t):
    'boolExpr : reference'
    t[0] = {"type": "bool", "value": t[1]}


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
            t[0] = {"type": "letReference", "value": {
                "value": name, "type": lets[name]["type"]["value"]}}
    except IndexError:
        print("Undefined name '%s'" % t[1])
        t[0] = None


def p_print(t):
    '''print : BAKA LPAREN exprLst RPAREN'''
    _, _, _, elements, _ = t
    print(*elements)
    t[0] = lambda: print(elements)


def p_arrayReference(t):
    ''' arrayReference : ID LBRACK numExpr RBRACK '''
    _, name, _, index, _ = t
    try:
        if (name in lets):
            t[0] = {"type": "arrayReference", "value": {
                "name": name, "index": index, "value": lets[name]}}
        else:
            print("Undefined name '%s'" % t[1])
            t[0] = None
    except IndexError:
        print("Index out of bounds")
        t[0] = None


parser = yacc.yacc()

if __name__ == "__main__":
    argParser = argparse.ArgumentParser(
        description='Take in the OwOScript source code and parse it into an AST.')
    argParser.add_argument(
        'FILE', help="Input file with OwOScript source code")
    args = argParser.parse_args()

    f = open(args.FILE, 'r')
    data = f.read()
    f.close()
    ast = parser.parse(data)

    # Write output to a file
    with open('output.json', 'w') as f:
        f.write(json.dumps(ast, indent=2))
    print("parsing complete")

# x = parser.parse('''
#     real waifu x = 4;
#     waifu~chan something(waifu t){
#         waifu x = -1;
#         x = 2;
#         waifu y = 1;
#         y = y + x;
#     }
#     waifu z = 2 + x;
#     whileU (z < 10) iStudied {
#         z = z+1;
#     }
#     shi (real waifu x : w ){
#         baka(z);
#     }
#     shi (waifu x =0; x < 10; x= x+1 ){
#         baka(x);
#     }
# ''')
# # print(x)
# print(fns)


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
