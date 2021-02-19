#Come back to this ⬇
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
                 'and': lambda x,y : x and y,
                 'or' : lambda x,y : x or y
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