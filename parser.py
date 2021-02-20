from ply import yacc, lex
import lexer
tokens = lexer.tokens


def toIntIfInt(x):
    return int(x) if x % int(x) == 0 else x


lets = {}
consts = {}
fns = {}
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


def p_multiline_expr(t):
    '''line : statement
            | line statement
    '''
    t[0] = t[1::]


def p_expr(t):
    '''expr : numExpr
            | reference
    '''
    t[0] = t[1]

def p_whileloop_statement(t):
    '''statement : WHILEU LPAREN boolExpr RPAREN ISTUDIED LBRACE statement RBRACE'''
    pass
def p_assign(t):
    '''assign : declaration EQ expr 
              | ID EQ expr
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
            print("Cannot reassing constant")
        else:
            print("Variable {} not declared.".format(name))
        # error ehere


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


def p_const_declaration(t):
    '''const_declaration : REAL array_declaration
                         | REAL let_declartion
    '''
    _, name = t[2]
    t[0] = t[2] + ['const']
    consts[name] = True


def p_array_declaration(t):
    'array_declaration : type HAREM ID'
    _, typeVal, _,  name = t
    t[0] = [typeVal + ' harem', name]
    if (name not in lets and name not in fns):
        lets[name] = {
            "type": typeVal,
            "array": True,
            "val": None
        }
    else:
        print("{} has already been declared.".format(name))


def p_let_declaration(t):
    '''let_declartion : type ID'''

    _, typeVal, name = t
    t[0] = [typeVal, name]
    if (name not in lets and name not in fns):
        lets[name] = {"type": typeVal, "array": False, "val": None}
    else:
        print("{} has already been declared.".format(name))


def p_type(t):
    '''type : WAIFU
            | CATGIRL
    '''
    t[0] = t[1]


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

# short binoperation (+=, *=, -=, \=) requires an ID that exists and updated its value in ditionary
def p_numExpr_shortBinOp(t):
    '''numExpr : ID PEQ numExpr
                | ID MEQ numExpr
                | ID DEQ numExpr
                | ID TEQ numExpr
                | ID PP
                | ID MM
    '''
    try:
        if t[2] == '+=':
            var[t[1]][1] = var[t[1]][1] + t[3]
        elif t[2] == '-=':
            var[t[1]][1] = var[t[1]][1] - t[3]
        elif t[2] == '*=':
            var[t[1]][1] = var[t[1]][1] * t[3]
        elif t[2] == '/=':
            var[t[1]][1] = var[t[1]][1] *  1/t[3]
        elif t[2] == '++':
            var[t[1]][1] = var[t[1]][1] + 1
        elif t[2] == '--':
            var[t[1]][1] = var[t[1]][1] - 1
        
        t[0] = var[t[1]][1]
    except LookupError:
        print("Undefined name '%s'" % t[1])

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


def p_reference(t):
    '''reference : letReference
                 | arrayReference
    '''
    t[0] = t[1]


def p_letReference(t):
    '''letReference : ID'''
    try:
        t[0] = lets[t[1]]["val"]
    except LookupError:
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
    except LookupError:
        print("Index out of bounds")
        t[0] = None


parser = yacc.yacc()

#declaration
#waifu x; 
x = parser.parse('waifu x = 0; whileU (x < 10) iStudied { x+=11; }')
print(x)
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
