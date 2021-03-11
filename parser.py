from ply import yacc, lex
import lexer
import json

import argparse
from ScopedMap import ScopedMap
tokens = lexer.tokens


def toIntIfInt(x):
    return int(x) if x % int(x) == 0 else x


def declarations(name, typeVal, isArray, type):
    if (not lets.inCurrentScope(name) and not fns.inCurrentScope(name)):
        lets.forceNew(name, {
            "type": typeVal,
            "array": isArray,
            "value": None
        })
        return {"type": type, "value": {
            "type": typeVal["value"], "value": name}}
    else:
        raise Exception("{} has already been declared.".format(name))


lets = ScopedMap()
consts = ScopedMap()
fns = ScopedMap()

precedence = (
    ('left', 'LT', 'LEQ', 'GT', 'GEQ', 'EQOP', 'NEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS', 'NOT'),
)


def p_program(t):
    ' program : stmts_or_empty'
    t[0] = {'type': "program", 'value': t[1]}


def p_statements_or_empty(t):
    ''' stmts_or_empty : statements
                       | empty
    '''
    t[0] = t[1]


def p_statements(t):
    ''' statements : statements singleStatement
                   | singleStatement
    '''
    t[0] = t[1] + [t[2]] if len(t) > 2 else [t[1]]


def p_singleStatement(t):
    ''' singleStatement : expr SEMICOL
                        | assignment SEMICOL
                        | declaration SEMICOL
                        | functionDeclaration
                        | whileLoop
                        | forLoop
                        | conditional
                        | returnStatement SEMICOL
    '''
    t[0] = t[1]


def p_expr(t):
    ''' expr : numExpr
             | boolExpr
             | functionCall
             | arrayExpr
             | ternaryOp
             | reference 

    '''
    t[0] = t[1]


def p_ternaryOp(t):
    ''' ternaryOp : boolExpr QMARK expr COL expr
    '''
    if isinstance(t[1]['value'], bool):
        t[0] = t[3] if t[1]['value'] else t[-1]
    else:
        t[0] = {"type": "ternaryOp", 'value': t[1::]}


def p_arrayExpr(t):
    '''arrayExpr : arrayLiteral
                 | letReference
    '''
    t[0] = t[1]


def p_assignment(t):
    '''assignment : reassign
                  | initialize
                  | arrayAssign
                  | binOpAssign
    '''
    t[0] = t[1]


def p_conditional(t):
    ''' conditional : if else
                    | if
    '''
    t[0] = {'type': 'cond', 'value': t[1::]}


def p_if(t):
    ''' if : NANI LPAREN boolExpr RPAREN newScope enclosure popScope
           | NANI LPAREN boolExpr RPAREN newScope singleStatement popScope
    '''
    t[0] = {'type': 'if', 'value': t[2:5]+[t[6]]}


def p_else(t):
    ''' else : NOU newScope enclosure popScope
             | NOU newScope singleStatement popScope
    '''
    t[0] = {'type': 'else', 'value': [t[1]]+[t[3]]}


def p_reassign(t):
    ''' reassign : ID EQ expr
    '''
    _, name, _, val = t
    if (name in lets and name not in consts):
        t[0] = {'type': 'reassign', 'value': t[1::]}
        lets[name]["value"] = val
    else:
        if (name in lets):
            if (consts.inScopeIndex(lets.getScopeIndex(name), name)):
                raise Exception("Cannot reassign constant")
            else:
                t[0] = {'type': 'reassign', 'value': t[1::]}
                lets[name]["value"] = val
        else:
            raise Exception("Variable {} not declared.".format(name))
        # error here


def p_functionDeclaration(t):
    ''' functionDeclaration : newFn newScope LPAREN argumentDeclaration RPAREN enclosure popScope
    '''
    _, newFn, _, l, args, r, enclosure, _ = t
    returnType, _, honorific, fnName = newFn
    t[0] = {'type': 'functionDeclaration',
            'returnType': returnType['value'], 'value': [fnName, l, args, r, enclosure]}
    fns[fnName][1] = (args, enclosure)


def p_enclosure(t):
    ''' enclosure : LBRACE RBRACE
                  | LBRACE statements RBRACE
    '''
    t[0] = {'type': 'enclosure', 'value': t[1::]}


def p_newFn(t):
    'newFn : fnType SQUIGGLY honorific ID'
    _, typeVal, _, _, name = t
    fns.forceNew(name, [typeVal, None])
    t[0] = t[1::]


def p_newScope(t):
    'newScope : '
    lets.addScope()
    consts.addScope()
    fns.addScope()
    t[0] = None


def p_returnStatement(t):
    ''' returnStatement : expr DESU
    '''
    # future error check, can only return in a function.
    t[0] = {'type': 'return', 'value': t[1]}


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
    ''' arrayAssign : ID LBRACK numExpr RBRACK EQ expr
    '''
    _, name, *elements = t
    if (name in lets):
        if (lets[name]['value'] != None):
            # if lets[name]["type"] == typeOf(val):
            t[0] = {"type": "arrayAssign", "value": [name]+elements}
            lets[name]['value'][elements[2]] = elements[-1]
        else:
            raise Exception("Array %s uninitialized" % name)
    else:
        raise Exception("Undefined name '%s'" % name)


def p_functionCall(t):
    ''' functionCall : printCall
                     | ID LPAREN exprLst RPAREN
                     | ID LPAREN RPAREN
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        _, fnName, *elements = t
        if (fnName in fns):
            # ok we need to make objects to store our data properly
            if len(elements) == 2:
                t[0] = {"type": "functionCall",
                        "name": fnName, "value": [fnName]+elements}
            else:
                t[0] = {"type": "functionCall",
                        "name": fnName, "value": [fnName]+[elements[0], *elements[1], elements[2]]}
        else:
            raise Exception("Undefined function name '%s'" % fnName)


def p_arrayLiteral(t):
    ''' arrayLiteral : LBRACK RBRACK
                     | LBRACK exprLst RBRACK
    '''
    _, *elements = t
    if len(t) == 3:
        t[0] = {"type": "arrayLiteral", "value": elements}
    else:
        t[0] = {"type": "arrayLiteral", "value": [
            elements[0], *elements[1], elements[2]]}


def p_exprList(t):
    ''' exprLst : expr
                | expr COMMA exprLst
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = [t[1]] + t[3]


def p_initialize(t):
    ''' initialize : letInitialize
                   | constInitialize
    '''
    t[0] = t[1]


def p_letInitialize(t):
    ''' letInitialize : declaration EQ expr
    '''
    name = t[1]["value"]["value"]
    typeName = t[1]["value"]["type"]
    val = t[3]
    # if (typeOf(val) == typeVal):
    t[0] = {"type": "initialize", "value": [
        {"type": typeName, "value": name}, '=', t[3]]}
    lets[name]["value"] = val
    # else error


def p_constInitialize(t):
    ''' constInitialize : constDeclaration EQ expr
    '''
    name = t[1]["value"]["value"]
    typeName = t[1]["value"]["type"]
    val = t[3]
    # if (typeOf(val) == typeVal):
    t[0] = {"type": "constInitialize", "value": [
        {"type": typeName, "value": name}, '=', t[3]]}
    lets[name]["value"] = val


def p_declaration(t):
    ''' declaration : arrayDeclaration
                    | letDeclaration
    '''
    # note const declaration cannot go here, we have to assign when we do that
    t[0] = t[1]


def p_binOpAssign(t):
    ''' binOpAssign : ID PEQ numExpr
                    | ID MEQ numExpr
                    | ID TEQ numExpr
                    | ID DEQ numExpr
                    | ID PP
                    | ID MM
    '''
    options = {'+=': lambda x, y: x + y,
               '-=': lambda x, y: x - y,
               '*=': lambda x, y: x * y,
               '/=': lambda x, y: x / y,
               '++': lambda x, y: x + 1,
               '--': lambda x, y: x - 1
               }
    if len(t) == 4:
        _, name, op, val = t
    else:
        _, name, op = t
        val = 1
    if (name in lets):
        if (name not in consts):
            t[0] = {'type': 'short_binop', 'value': t[1::]}
        else:
            raise Exception("Cannot reassign constant")
    else:
        raise Exception("Variable {} not declared.".format(name))


def p_argumentDeclaration(t):
    '''argumentDeclaration : declaration
                           | declaration COMMA argumentDeclaration
                           |
    '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        if len(t) == 1:
            t[0] = []
        else:
            t[0] = [t[1]] + t[3]


def p_constDeclaration(t):
    '''constDeclaration : REAL arrayDeclaration
                        | REAL letDeclaration
    '''
    name = t[2]["value"]["value"]
    t[0] = {"type": "constDeclaration", "value": t[2]["value"]}
    consts.forceNew(name, True)


def p_arrayDeclaration(t):
    'arrayDeclaration : type HAREM ID'
    _, typeVal, _,  name = t

    # [typeVal + ' harem', name]
    t[0] = declarations(
        name, {"type": 'type', "value": typeVal["value"] + " harem"}, True, 'declaration')


def p_letDeclaration(t):
    '''letDeclaration : type ID'''

    _, typeVal, name = t
    t[0] = declarations(name, typeVal, False, 'declaration')


def p_whileLoop(t):
    '''whileLoop : WHILEU LPAREN boolExpr RPAREN ISTUDIED newScope enclosure popScope
    '''
    _, _, _, cond, _, _, _, statements, _ = t
    t[0] = {"type": 'whileLoop', "value": t[1:6]+[statements]}


def p_forLoop(t):
    '''forLoop : SHI newScope LPAREN forTrio RPAREN enclosure popScope
               | SHI newScope LPAREN forElement RPAREN enclosure popScope
    '''
    t[0] = {"type": 'forLoop', "value": [t[1]]+t[3:7]}


def p_forTrio(t):
    ''' forTrio : forAssign SEMICOL boolExpr SEMICOL forReassign
    '''
    t[0] = {'type': 'forTrio', 'value': t[1::]}


def p_forAssign(t):
    ''' forAssign : reassign
                  | letInitialize
                  | arrayAssign
                  | binOpAssign
    '''
    t[0] = t[1]


def p_forReassign(t):
    ''' forReassign : reassign
                    | arrayAssign    
                    | binOpAssign
    '''
    t[0] = t[1]


def p_forElement(t):
    ''' forElement : declaration COL ID
                   | constDeclaration COL ID
    '''
    #  need to error check
    t[0] = {'type': 'forElement', 'value': t[1::]}


def p_print(t):
    '''printCall : BAKA LPAREN exprLst RPAREN'''
    _, *elements = t
    t[0] = {"type": "printCall", "value": [
        elements[0], elements[1], *elements[2], elements[3]]}


def p_boolExpr_op(t):
    ''' boolExpr : boolExpr AND boolExpr
                 | boolExpr OR boolExpr
                 | expr NEQ expr
                 | numExpr LEQ numExpr
                 | numExpr GEQ numExpr
                 | numExpr LT numExpr
                 | numExpr GT numExpr
                 | expr EQOP expr
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
    if isinstance(a["value"], (int, float, bool)) and isinstance(b["value"], (int, float, bool)):
        t[0] = {"type": 'boolExpr', "value": options[op]
                (a["value"], b["value"])}
    else:
        t[0] = {"type": "boolExpr", "value": {
            "type": t[2], "value": [t[1], t[3]]}}


def p_numExpr_binop(t):
    '''numExpr : numExpr PLUS numExpr
               | numExpr MINUS numExpr
               | numExpr TIMES numExpr
               | numExpr DIVIDE numExpr
               | numExpr MOD numExpr
               | numExpr POW numExpr'''
    if isinstance(t[1]["value"], (float, int)) and isinstance(t[3]["value"], (float, int)):
        # Directly evaluates literals as optimization
        if t[2] == '+':
            t[0] = {"type": "numExpr", "value": toIntIfInt(
                t[1]["value"] + t[3]["value"])}
        elif t[2] == '-':
            t[0] = {"type": "numExpr", "value": toIntIfInt(
                t[1]["value"] - t[3]["value"])}
        elif t[2] == '*':
            t[0] = {"type": "numExpr", "value": toIntIfInt(
                t[1]["value"] * t[3]["value"])}
        elif t[2] == '/':
            t[0] = {"type": "numExpr", "value": toIntIfInt(
                t[1]["value"] / t[3]["value"])}
        elif t[2] == '%':
            t[0] = {"type": "numExpr", "value": toIntIfInt(
                t[1]["value"] % t[3]["value"])}
        elif t[2] == '**':
            t[0] = {"type": "numExpr", "value": toIntIfInt(
                t[1]["value"] ** t[3]["value"])}
    else:
        t[0] = {"type": "numExpr", "value": {
            "type": t[2], "value": [t[1], t[3]]}}


def p_numExpr_reference(t):
    'numExpr : reference'
    t[0] = t[1]


def p_boolExpr_reference(t):
    'boolExpr : reference'
    t[0] = t[1]


def p_reference(t):
    '''reference : letReference
                 | arrayReference
    '''
    t[0] = t[1]


def p_letReference(t):
    '''letReference : ID
    '''
    _, name = t
    if (name in lets):
        t[0] = {
            "type": "letReference",
            "value":
                {
                    "type": lets[name]["type"]["value"],
                    "value": name,
                }
        }
    else:
        raise Exception("Undefined name '%s'" % name)


def p_arrayReference(t):
    ''' arrayReference : ID LBRACK numExpr RBRACK '''
    _, name, _, index, _ = t
    if (name in lets):
        t[0] = {"type": "arrayReference",
                "value": [{"value": name,
                           "type": lets[name]["type"]["value"]},
                          '[',
                          {"type": "numExpr",
                           "value": index},
                          ']']}
    else:
        raise Exception("Undefined name '%s'" % name)


def p_boolExprNeg(t):
    'boolExpr : NOT boolExpr'

    t[0] = {"type": 'boolExpr', "value": [t[1], t[2]]} if not isinstance(
        t[2]['value'], (bool)) else {"type": "boolExpr", "value": not t[2]['value']}
    # t[0] = {"type": 'boolExpr', "value": t[1:3] if not else not t[2]["value"]}


def p_boolExpr_group(t):
    '''boolExpr : LPAREN boolExpr RPAREN
    '''
    t[0] = {"type": 'boolExpr', "value": t[1::]
            if not isinstance(t[2]['value'], bool) else t[2]['value']}


def p_bool(t):
    ''' boolExpr : OWO
                 | UWU
    '''
    t[0] = {"type": "boolExpr", "value": True if t[1] == 'uwu' else False}


def p_numExpr_uminus(t):
    'numExpr : MINUS numExpr %prec UMINUS'
    t[0] = {"type": 'numExpr', "value": [t[1], t[2]] if not isinstance(
        t[2]['value'], (int, float)) else -t[2]['value']}


def p_numExpr_group(t):
    'numExpr : LPAREN numExpr RPAREN'
    t[0] = {"type": 'numExpr', "value":  t[1::]
            if not isinstance(t[2]['value'], (float, int)) else t[2]['value']}


def p_numExpr_number(t):
    'numExpr : NUMBER'
    t[0] = {"type": 'numExpr', "value": t[1]}


def p_fnType(t):
    ''' fnType : YOKAI
               | type
    '''
    t[0] = {'type': 'type', "value": t[1]} if t[1] == 'yokai' else t[1]


def p_type(t):
    '''type : WAIFU
            | CATGIRL
    '''
    t[0] = {'type': 'type', "value": t[1]}


def p_empty(t):
    '''empty : '''
    pass


# def p_error(t):
#     raise Exception("Syntax error at line", t.lineno)

def make_parser():
    return yacc.yacc()


def make_ast(sourceCode, parser):
    return parser.parse(sourceCode)


def run_parser(sourceCode, outputFileName, parser):
    ast = make_ast(sourceCode, parser)
    # Write output to a file
    with open(outputFileName, 'w') as f:
        f.write(json.dumps(ast, indent=2))
    print("parsing complete")


def reset_parser():
    lets = ScopedMap()
    consts = ScopedMap()
    fns = ScopedMap()


if __name__ == "__main__":
    argParser = argparse.ArgumentParser(
        description='Take in the OwOScript source code and parse it into an AST.')
    argParser.add_argument(
        'FILE', help="Input file with OwOScript source code")
    args = argParser.parse_args()
    parser = make_parser()
    sourceFile = open(args.FILE)
    sourceCode = sourceFile.read()
    sourceFile.close()
    run_parser(sourceCode, '{}.json'.format(args.FILE), parser)
