from ply import yacc, lex
import lexer
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


# scopes = []
# scopes.append({"lets": {}, "consts": {}, "fns": {}})
lets = ScopedMap()
consts = ScopedMap()
fns = ScopedMap()

# def p_assign(p):
#     '''assign : ID EQ numExpr'''
#     print(len(p))
#     vars[p[0]] - p[2]
# we have to do ugly bnf sadge, but ok it kinda works
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
    '''
    t[0] = t[1::]


def p_expr(t):
    '''expr : numExpr
            | boolExpr
            | reference
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
        t[0] = [name, '=', val]
        lets[name]["val"] = val
    else:
        if (name in lets):
            if (consts.inScopeIndex(lets.getScopeIndex(name), name)):
                print("Cannot reassing constant")
            else:
                t[0] = [name, '=', val]
                lets[name]["val"] = val
        else:
            print("Variable {} not declared.".format(name))
        # error ehere


def p_functionDef(t):
    ''' functionDef : newFn newScope LPAREN declarationLst RPAREN enclosure popScope
    '''
    _, fnName, _, _, args, _, enclosure, _ = t
    fns[fnName][1] = enclosure
    t[0] = (fnName, enclosure)


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
    ''' initialize : declaration EQ expr
                   | declaration EQ arrayLiteral
                   | const_declaration EQ expr
    '''
    typeVal, name = t[1][0:2]
    val = t[3]
    # if (typeOf(val) == typeVal):
    t[0] = [name, '=', val]
    lets[name]["val"] = val
    # else error


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


def p_letReference(t):
    '''letReference : ID'''
    _, name = t
    try:
        if (name in lets):
            t[0] = lets[name]["val"]
    except IndexError:
        print("Undefined name '%s'" % t[1])
        t[0] = None


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


x = parser.parse('''
    real waifu x = 4;
    waifu~chan something(){
        waifu x = -1;
        x = 2;
        waifu y = 1;
        y = y + x;
    }
    waifu z = 2 + x;
''')
print(x)
print(fns)
print(lets)
# while True:
#     try:
#         s = raw_input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
