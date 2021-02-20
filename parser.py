from ply import yacc, lex
import lexer
tokens = lexer.tokens

########################################HELPERS###############################################
owoTypes = {}
owoTypes[int] = ['waifu']
owoTypes[float] = ['waifu']
owoTypes[bool] = ['catgirl']

##############################################################################################
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

var = {}
const = {} 

def p_multiline_expr(t):
    '''line : statement
            | line statement
    '''
    t[0] = t[1]

def p_statement_expr(t):
    '''statement : expr SEMICOL
                 | assign SEMICOL
                 | declaration SEMICOL
    '''
    t[0] = t[1]

def p_whileloop_statement(t):
    '''statement : WHILEU LPAREN boolExpr RPAREN ISTUDIED LBRACE statement RBRACE'''
    pass
def p_assign(t):
    '''assign : declaration EQ expr 
              | ID EQ expr
    '''
    try:
        var[t[1]][1] = t[3]
        t[0] = t[1::]
    except LookupError:
        print("Undefined name '%s'" % t[1])

def p_declaration(t):
    '''declaration : type ID
                   | array ID
                   | REAL declaration
    '''
    if t[1] == 'real':
        t[0] = t[2]
        const[t[2][1]] = True
    else:       
        t[0] = t[2]
        var[t[2]] = [[t[1]], None]

def p_expr(t):
    '''expr : numExpr
            | boolExpr
            | reference
    '''
    t[0] = t[1]

def p_boolExpr_op(t):
    ''' boolExpr : boolExpr NEQ boolExpr
                 | numExpr NEQ numExpr
                 | numExpr LEQ numExpr
                 | numExpr GEQ numExpr
                 | numExpr LT numExpr
                 | numExpr GT numExpr
                 | numExpr EQOP numExpr
                 | boolExpr EQOP boolExpr
                 | boolExpr AND boolExpr
                 | boolExpr OR boolExpr
    '''
    options = {'<': lambda x,y : x < y,
                '>' : lambda x,y : x > y,
                 '>=' : lambda x,y : x >= y,
                 '<=' : lambda x,y : x<=y,
                 '==' : lambda x,y : x==y,
                 '!=' : lambda x,y : x !=y,
                 '&&': lambda x,y : x and y,
                 '||' : lambda x,y : x or y
    }
    t[0] = options[t[2]](t[1], t[3])

#need to handle arrays
def p_reference(t):
    '''reference : ID
                 | ID LBRACK numExpr RBRACK 
    '''
    try:
        t[0] = var[t[1]][1]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

#these 2 are necessary since boolExpr is different from numExpr
def p_boolExpr_reference(t):
    '''boolExpr : reference'''
    t[0] = t[1]

def p_numExpr_reference(t):
    '''numExpr : reference'''
    t[0] = t[1]  

def p_boolExpr_not(t):
    '''boolExpr : NOT boolExpr'''
    t[0] = not t[2]

def p_boolExpr_group(t):
    '''boolExpr : LPAREN boolExpr RPAREN
    '''
    t[0] = t[2]

def p_numExpr_binop(t):
    '''numExpr : numExpr PLUS numExpr
               | numExpr TIMES numExpr
               | numExpr MINUS numExpr
               | numExpr DIVIDE numExpr

    '''
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


# unary minus operator expression: <expression> -> - <expression>
def p_numExpr_uminus(t):
    'numExpr : MINUS numExpr %prec UMINUS'
    t[0] = - t[2]


# parenthesis group expression: <expression> -> ( <expression> )
def p_numExpr_group(t):
    'numExpr : LPAREN numExpr RPAREN'
    t[0] = t[2]

def p_number(t):
    '''numExpr : NUMBER'''
    t[0] = t[1]

def p_arrays(t):
    '''array : type HAREM'''
    t[0] = t[1::]

def p_bool(t):
    '''boolExpr : OWO
                | UWU
    '''
    t[0] = True if t[1] == 'uwu' else False

def p_prim(t):
    '''prim : type
            | YOKAI
    '''
    t[0] = t[1]

def p_type(t):
    '''type : WAIFU
            | CATGIRL
    '''
    t[0] = t[1]

# def p_error(t):
#     print("Syntax error at '%s'" % t)

parser = yacc.yacc()

#declaration
#waifu x; 
x = parser.parse('waifu x = 0; whileU (x < 10) iStudied { x+=11; }')
print(x)
print(var)
print(const)
# while True:
#     try:
#         s = raw_input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
