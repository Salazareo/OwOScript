from ply import yacc, lex
import lexer
tokens = lexer.tokens


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
vars = {}


def p_statement_assign(t):
    'statement : ID EQ numExpr'
    vars[t[1]] = t[3]


def p_statement_expr(t):
    'statement : numExpr'
    print(t[1])


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


def p_expression_name(t):
    'numExpr : ID'
    try:
        t[0] = vars[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0


parser = yacc.yacc()


parser.parse('x = -2 + 1')

print(vars)
# while True:
#     try:
#         s = raw_input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
