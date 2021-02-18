from ply import yacc, lex
import lexer
tokens = lexer.tokens


# def p_assign(p):
#     '''assign : ID EQ expression'''
#     print(len(p))
#     vars[p[0]] - p[2]

# we have to do ugly bnf sadge, but ok it kinda works
def p_binary_operators(p):
    '''expression : NUMBER PLUS NUMBER
                  | NUMBER MINUS NUMBER
                  | NUMBER 
    '''
    # print(len(p))
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3].isnumeric():
            p[0] = p[1] * 1/p[3]
        else:
            p[0] = p[1] / p[3]


parser = yacc.yacc()


x = parser.parse('3 - 2')
print(x)
# while True:
#     try:
#         s = raw_input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
