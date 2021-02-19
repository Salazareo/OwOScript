from ply import yacc, lex
import lexer
tokens = lexer.tokens


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

var = {}
const = {} 
def p_statement_expr(t):
    '''statement : numExpr SEMICOL
                 | boolExpr SEMICOL
                 | declare SEMICOL
    '''
    t[0] = t[1]

    
def p_statement_declare(t):
    ''' declare : declaration
                | declaration EQ numExpr 
                | declaration EQ boolExpr    
    '''
    t[0] = t[1::]
    if t[2] == '=':
        var[t[1][1]][1] = t[3]

def p_statement_declaration_or_assign_h(t):
    ''' declaration : type ID 
                    | arrays ID 
                    | REAL declaration
    '''
    if t[1] == 'real':
        t[0] = t[2]
        const[t[2][1]] = True
    else:       
        t[0] = t[1::]
        var[t[2]] = [t[1], None]

def p_arrays(t):
    ''' arrays : type HAREM 
    '''
    t[0] = t[1::]   

def p_types(t):
    ''' type : WAIFU
             | CATGIRL
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
                 '==' : lambda x,y : x == y,
                 '!=' : lambda x,y : x !=y,
                 '&&': lambda x,y : x and y,
                 '||' : lambda x,y : x or y
                 }
    t[0] = options[t[2]](t[1], t[3])
    
def p_boolExpr_not(t):
    '''boolExpr : NOT boolExpr
    '''
    t[0] = not t[1]

def p_boolExpr_group(t):
    'boolExpr : LPAREN boolExpr RPAREN'
    t[0] = t[2]

def p_bool(t):
    ''' boolExpr : OWO
             | UWU
    '''
    t[0] = True if t[1] == 'uwu' else False 
     
#we know its different... leave us alone, we are code monkeys.
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
        t[0] = t[1] *  1/t[3]


def p_numExpr_uminus(t):
    'numExpr : MINUS numExpr %prec UMINUS'
    t[0] = -t[2]


def p_numExpr_group(t):
    'numExpr : LPAREN numExpr RPAREN'
    t[0] = t[2]


def p_numExpr_number(t):
    'numExpr : NUMBER'
    t[0] = t[1]
    



# def p_expression_name(t):
#     'numExpr : ID'
#     try:
#         t[0] = var[t[1]]
#     except LookupError:
#         print("Undefined name '%s'" % t[1])
#         t[0] = 0


parser = yacc.yacc()

#declaration
#waifu x; 
x = parser.parse('real catgirl x = uwu || owo;')

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
