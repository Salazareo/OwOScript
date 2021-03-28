from ply import yacc
import lexer
import json
import logging

import argparse
from ScopedMap import ScopedMap
tokens = lexer.tokens

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

def rreplace(s: str, old: str, new: str, occurrence=1):
    li = s.rsplit(old, occurrence)
    return new.join(li)


class TypeConvervter():
    def __init__(self):
        self.dic = {
            "senpai": "senpai",
            "kohai": "senpai",
            "waifu": "waifu",
            "husbando": "waifu",
            "catgirl": "catgirl",
            "catboy": "catgirl",
        }

    def __getitem__(self, key):
        try:
            return self.dic[key]
        except Exception:
            return key


typeConv = TypeConvervter()


def declarations(name, typeVal, isArray, type):
    if (not lets.inCurrentScope(name) and not fns.inCurrentScope(name)):
        lets.forceNew(name, {
            "type": typeVal,
            "returnType": typeConv[typeVal["returnType"]],
            "array": isArray,
            "value": None
        })
        return {"type": type, "returnType": typeConv[typeVal["returnType"]], "value": {
            "type": typeVal["value"], "value": name}}
    else:
        raise Exception("{} has already been declared.".format(name))


lets = ScopedMap()
consts = ScopedMap()
fns = ScopedMap()

precedence = (
    ('left', 'QMARK', 'COL'),
    ('left', 'AND', 'OR'),
    ('left', 'NEQ', 'LEQ', 'GEQ', 'LT', 'GT', 'EQOP'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('left', 'POW'),
    ('right', 'UMINUS', 'NOT'),
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'LBRACK', 'RBRACK'),
)


def p_program(t):
    ' program : stmts_or_empty'
    t[0] = {'type': "program", 'value': t[1], "line": t.lineno(1)}


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
    ''' expr : literal
             | arrayLiteral
             | reference
             | functionCall
             | ternaryOp
    '''
    t[0] = t[1]


def p_paren_expr(t):
    ''' expr : LPAREN expr RPAREN
    '''
    t[0] = {
        "type": t[2]["type"], "returnType": t[2]["returnType"], "value": t[1::]
        if not isinstance(t[2]['value'], (bool, int, float)) else t[2]['value'],
        "line": t.lineno(1)
    }


def p_boolExpr(t):
    ''' expr : expr PLUS expr
             | expr MINUS expr
             | expr TIMES expr
             | expr DIVIDE expr
             | expr MOD expr
             | expr POW expr
             | expr LT expr
             | expr GT expr
             | expr LEQ expr
             | expr GEQ expr
    '''
    _, expr1, op, expr2 = t
    boolOptions = {'<': lambda x, y: x < y,
                   '>': lambda x, y: x > y,
                   '>=': lambda x, y: x >= y,
                   '<=': lambda x, y: x <= y,
                   }
    numOptions = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y,
        '%': lambda x, y: x % y,
    }
    if typeConv[expr1["returnType"]] not in ("waifu", "senpai") or typeConv[expr1["returnType"]] != typeConv[expr2["returnType"]]:
        raise Exception("TypeError")

    if typeConv[expr1["returnType"]] == "senpai" and op != '+':
        raise Exception("Operand not supported!")

    if isinstance(expr1["value"], str) and isinstance(expr2["value"], str):
        t[0] = {
            "type": "strExpr",
            "value": numOptions[op](expr1["value"], expr2["value"])
        }
    elif typeConv[expr1["returnType"]] == "senpai":
        t[0] = {"type": "strExpr", "value": {
                "type": op, "value": [expr1, expr2]}}
    else:
        if isinstance(expr1["value"], (float, int)) and isinstance(expr2["value"], (float, int)):
            # Directly evaluates literals as optimization
            if op in numOptions:
                t[0] = {
                    "type": "numExpr",
                    "value": numOptions[op](expr1["value"], expr2["value"])
                }
            else:
                t[0] = {"type": 'boolExpr', "value": boolOptions[op]
                        (expr1["value"], expr2["value"])}

        elif op in numOptions:  # Does not have literals
            t[0] = {"type": "numExpr", "value": {
                "type": op, "value": [expr1, expr2]}}

        else:
            t[0] = {"type": "boolExpr", "value": {"type": op,
                                                  "value": [expr1, expr2]}}
    t[0]["line"] = t.lineno(1)
    t[0]["returnType"] = "catgirl" if t[0]["type"] == "boolExpr"\
        else ("senpai" if t[0]["type"] == "strExpr" else
              "waifu")


def p_equality_op(t):  # Because both bools and nums can use it
    ''' expr : expr EQOP expr
             | expr NEQ expr
    '''
    _, expr1, op, expr2 = t
    options = {'==': lambda x, y: x == y,
               '!=': lambda x, y: x != y,
               }
    # Check that both expr have the same types
    if typeConv[expr1["returnType"]] != typeConv[expr2["returnType"]]:
        raise Exception("Incomparable types")
    if isinstance(expr1["value"], (int, float)) and isinstance(expr2["value"], (int, float)):
        t[0] = {"value": options[op](expr1["value"], expr2["value"])}
    else:
        t[0] = {"value": {"type": op, "value": [expr1, expr2]}}
    t[0]["type"] = "boolExpr"
    t[0]["returnType"] = "catgirl"


def p_boolExpr_op(t):
    ''' expr : expr AND expr
             | expr OR expr
    '''
    _, expr1, op, expr2 = t
    options = {'&&': lambda x, y: x and y,
               '||': lambda x, y: x or y
               }
    if typeConv[expr1["returnType"]] != "catgirl" and typeConv[expr2["returnType"]] != "catgirl":
        raise Exception("Expected type catgirl")
    elif isinstance(expr1["value"], (bool)) and isinstance(expr2["value"], (bool)):
        # Directly evaluate literals for optimization
        t[0] = {"value": options[op](
            expr1["value"], expr2["value"]), "line": t.lineno(1)}
    else:
        t[0] = {"value": {"type": op, "value": [
            expr1, expr2]}, "line": t.lineno(1)}
    t[0]["type"] = "boolExpr"
    t[0]["returnType"] = "catgirl"


def p_boolExprNeg(t):
    'expr : NOT expr'
    if typeConv[t[2]["returnType"]] != "catgirl":
        raise Exception("Expected type catgirl")
    t[0] = {"value": [t[1], t[2]]} if not isinstance(t[2]['value'], (bool)) \
        else {"value": not t[2]['value'], "line": t.lineno(1)}
    t[0]["type"] = "boolExpr"
    t[0]["returnType"] = "catgirl"


def p_numExpr_uminus(t):
    'expr : MINUS expr %prec UMINUS'
    if typeConv[t[2]["returnType"]] != "waifu":
        raise Exception("Expected type waifu")
    t[0] = {"value": [t[1], t[2]] if not isinstance(t[2]['value'], (int, float))
            else -t[2]['value'], "line": t.lineno(1)}
    t[0]["type"] = "numExpr"
    t[0]["returnType"] = "waifu"


def p_ternaryOp(t):
    ''' ternaryOp : expr QMARK expr COL expr
    '''
    _, condition, _, expr1, _, expr2 = t
    if typeConv[condition["returnType"]] != "catgirl":
        raise Exception("Expected type catgirl for the condition")
    elif typeConv[expr1["returnType"]] != typeConv[expr2["returnType"]]:
        raise Exception("Expressions do not have the same type")
    elif isinstance(condition['value'], bool):
        t[0] = expr1 if condition['value'] else expr2
    else:
        t[0] = {"type": "ternaryOp", "returnType": expr1["returnType"],
                'value': t[1::], "line": t.lineno(1)}


def p_assignment(t):
    '''assignment : reassign
                  | initialize
                  | arrayAssign
                  | binOpAssign
    '''
    t[0] = t[1]


def p_binOpAssign(t):
    ''' binOpAssign : ID PEQ expr
                    | ID MEQ expr
                    | ID TEQ expr
                    | ID DEQ expr
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
        if typeConv[val["returnType"]] != "waifu":
            raise Exception("Expected type waifu")
    else:
        _, name, op = t
        val = 1
    if (name in lets):
        if typeConv[lets[name]["returnType"]] != "waifu":
            raise Exception("Expected type waifu")
        if (name not in consts):
            t[0] = {'type': 'short_binop',
                    'value': t[1::], "line": t.lineno(1)}
        else:
            raise Exception("Cannot reassign constant")
    else:
        raise Exception("Variable {} not declared.".format(name))


def p_conditional(t):
    ''' conditional : if else
                    | if
    '''
    t[0] = {'type': 'cond', 'value': t[1::], "line": t.lineno(1)}


def p_if(t):
    ''' if : NANI LPAREN expr RPAREN newScope enclosure popScope
           | NANI LPAREN expr RPAREN newScope singleStatement popScope
    '''
    if typeConv[t[3]["returnType"]] != "catgirl":
        raise Exception("Expected type catgirl")
    t[0] = {'type': 'if', 'value': t[2:5]+[t[6]], "line": t.lineno(1)}


def p_else(t):
    ''' else : NOU newScope enclosure popScope
             | NOU newScope singleStatement popScope
    '''
    t[0] = {'type': 'else', 'value': [t[1]]+[t[3]], "line": t.lineno(1)}


def p_reassign(t):
    ''' reassign : ID EQ expr
    '''
    _, name, _, val = t
    if name in lets:
        if typeConv[lets[name]["returnType"]] != typeConv[val["returnType"]]:
            raise Exception("Incompatible types for reassignment")
        elif name not in consts or not (consts.inScopeIndex(lets.getScopeIndex(name), name)):
            t[0] = {'type': 'reassign', 'value': t[1::], "line": t.lineno(1)}
            lets[name]["value"] = val
        else:
            raise Exception("Cannot reassign constant")
    else:
        raise Exception("Variable {} not declared.".format(name))


def p_functionDeclaration(t):
    ''' functionDeclaration : fnHeader newScope LPAREN argumentDeclaration RPAREN enclosure popScope
    '''
    _, fnHeader, _, l, args, r, enclosure, _ = t
    returnType, _, honorific, fnName = fnHeader
    t[0] = {'type': 'functionDeclaration',
            'returnType': returnType['value'], 'value': [fnName, l, args, r, enclosure], "line": t.lineno(1)}
    fns[fnName][1] = (args, enclosure)


def p_enclosure(t):
    ''' enclosure : LBRACE RBRACE
                  | LBRACE statements RBRACE
    '''
    t[0] = {'type': 'enclosure', 'value': t[1::], "line": t.lineno(1)}


def p_functionHeader(t):
    'fnHeader : fnType SQUIGGLY honorific ID'
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
    # TODO: Same as above but type check for correct return type
    t[0] = {'type': 'return', 'value': t[1], "line": t.lineno(1)}


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
    ''' arrayAssign : ID LBRACK expr RBRACK EQ expr
    '''
    _, name, *elements = t
    if typeConv[t[3]["returnType"]] != 'waifu':
        raise Exception("Expected type waifu")
    if (name in lets):
        if typeConv[rreplace(lets[name]["returnType"], ' harem', '')] != typeConv[t[6]["returnType"]]:
            raise Exception("Assignment type does not match array type")
        elif (lets[name]['value'] != None):
            t[0] = {"type": "arrayAssign", "value": [
                name]+elements, "line": t.lineno(1)}
            lets[name]['value'][elements[2]] = elements[-1]
        else:
            raise Exception("Array %s at line %s uninitialized" %
                            (name, t.lineno(1)))
    else:
        raise Exception("Undefined name '%s' at line %s" % (name, t.lineno(1)))


def p_printCall(t):
    ''' functionCall : printCall '''
    t[0] = t[1]


def p_functionCall(t):
    ''' functionCall : ID LPAREN exprLst RPAREN
                     | ID LPAREN RPAREN
    '''
    _, fnName, *elements = t
    if (fnName in fns):
        if len(elements) == 2:  # Empty brackets
            t[0] = {"type": "functionCall",
                    "returnType": fns[fnName][0]["value"],
                    "name": fnName, "value": [fnName]+elements, "line": t.lineno(1)}
        else:
            t[0] = {"type": "functionCall",
                    "returnType": fns[fnName][0]["value"],
                    "name": fnName, "value": [fnName]+[elements[0], *elements[1], elements[2]], "line": t.lineno(1)}
    else:
        raise Exception("Undefined function name '%s' at line %s" %
                        (fnName, t.lineno(1)))


def p_arrayLiteral(t):
    ''' arrayLiteral : LBRACK RBRACK
                     | LBRACK exprLst RBRACK
    '''
    _, *elements = t
    if len(t) == 3:  # Empty array
        t[0] = {"type": "arrayLiteral",
                "returnType": "empty harem", "value": elements}
    else:
        # Check if all elements are the same type
        exprList = elements[1]
        arrayType = typeConv[exprList[0]["returnType"]]
        for i in range(1, len(exprList)):
            if arrayType != typeConv[exprList[i]["returnType"]]:
                raise Exception("Harem members are not the same type")

        t[0] = {
            "type": "arrayLiteral",
            "returnType": arrayType + " harem",
            "value": [elements[0], *elements[1], elements[2]],
            "line": t.lineno(1)
        }


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
    typeName = typeConv[t[1]["value"]["type"]]
    val = t[3]
    if typeName == typeConv[val["returnType"]] or \
            ("harem" in typeName and val["returnType"] == "empty harem"):
        t[0] = {"type": "initialize", "value": [
            {"type": typeName, "value": name}, '=', t[3]], "line": t.lineno(1)}
        lets[name]["value"] = val
    else:
        raise Exception("Expression type does not match variable type")


def p_constInitialize(t):
    ''' constInitialize : constDeclaration EQ expr
    '''
    name = t[1]["value"]["value"]
    typeName = t[1]["value"]["type"]
    val = t[3]

    if typeName == val["returnType"] or \
            ("harem" in typeName and val["returnType"] == "empty harem"):
        t[0] = {"type": "constInitialize", "value": [
            {"type": typeName, "value": name}, '=', t[3]], "line": t.lineno(1)}
        lets[name]["value"] = val
    else:
        raise Exception("Expression type does not match variable type")


def p_declaration(t):
    ''' declaration : arrayDeclaration
                    | letDeclaration
    '''
    # note const declaration cannot go here, we have to assign when we do that
    t[0] = t[1]


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
    t[0] = {"type": "constDeclaration",
            "value": t[2]["value"], "line": t.lineno(1)}
    consts.forceNew(name, True)


def p_arrayDeclaration(t):
    'arrayDeclaration : type HAREM ID'
    _, typeVal, _,  name = t

    returnType = typeConv[typeVal["value"]] + " harem"
    t[0] = declarations(
        name, {"type": 'type', "returnType": returnType, "value": returnType},
        True, 'declaration')
    t[0]["line"] = t.lineno(1)


def p_letDeclaration(t):
    '''letDeclaration : type ID'''

    _, typeVal, name = t
    typeVal["returnType"] = typeConv[typeVal["value"]]
    t[0] = declarations(name, typeVal, False, 'declaration')


def p_whileLoop(t):
    '''whileLoop : WHILEU LPAREN expr RPAREN ISTUDIED newScope enclosure popScope
    '''
    _, _, _, cond, _, _, _, statements, _ = t
    if cond["returnType"] != "catgirl":
        raise Exception("Expected type catgirl")
    t[0] = {"type": 'whileLoop', "value": t[1:6] +
            [statements], "line": t.lineno(1)}


def p_forLoop(t):
    '''forLoop : SHI newScope LPAREN forTrio RPAREN enclosure popScope
               | SHI newScope LPAREN forElement RPAREN enclosure popScope
    '''
    t[0] = {"type": 'forLoop', "value": [t[1]]+t[3:7], "line": t.lineno(1)}


def p_forTrio(t):
    ''' forTrio : forAssign SEMICOL expr SEMICOL forReassign
    '''
    if t[3]["returnType"] != "catgirl":
        raise Exception("Expected type catgirl")
    t[0] = {'type': 'forTrio', 'value': t[1::], "line": t.lineno(1)}


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
    t[0] = {'type': 'forElement', 'value': t[1::], "line": t.lineno(1)}


def p_print(t):
    '''printCall : BAKA LPAREN exprLst RPAREN'''
    _, *elements = t
    t[0] = {"type": "printCall", "value": [
        elements[0], elements[1], *elements[2], elements[3]],
        "line": t.lineno(1)
    }


def p_reference(t):
    ''' reference : letReference
    '''
    t[0] = t[1]


def p_letReference(t):
    ''' letReference : ID
    '''
    _, name = t
    if (name in lets):
        t[0] = {
            "type": "letReference",
            "returnType": lets[name]["returnType"],
            "value":
                {
                    "type": lets[name]["type"]["value"],
                    "value": name,
            },
            "line": t.lineno(1)
        }
    else:
        raise Exception("Undefined name '%s' at line %s" % (name, t.lineno(1)))


def p_arrayReference(t):
    ''' expr : expr LBRACK expr RBRACK 
             | ID LBRACK expr RBRACK
    '''
    _, lst, _, index, _ = t

    if index["returnType"] != "waifu":
        raise Exception("Expected type waifu for the index")
    if isinstance(lst, str):
        name = lst
        if (name in lets):
            t[0] = {"type": "arrayReference",
                    "returnType": lets[name]["returnType"].replace(' harem', ''),
                    "value": [{"value": name,
                            "type": lets[name]["type"]["value"]},
                            '[',
                            {"type": "numExpr",
                            "returnType": "waifu",
                            "value": index['value'] if isinstance(index['value'], (int, float)) else index},
                            ']'], "line": t.lineno(1)}
        else:
            raise Exception("Undefined name '%s' at line %s" % (name, t.lineno(1)))
    elif typeConv[lst['returnType']] == "senpai":
        if isinstance(lst['value'], str) and isinstance(index['value'], (int, float)):
            t[0] = {"type": "strExpr",
                    "value": lst['value'][index['value']],
                    'returnType': 'senpai',
                    "line": t.lineno(1)}
        else:
            t[0] = {"type": "strReference",
                    "value": [lst,
                              '[',
                              {"type": "numExpr",
                               "value": index['value'] if isinstance(index['value'], (int, float)) else index},
                              ']'],
                    'returnType': 'senpai',
                    "line": t.lineno(1)}
    else:
        if lst["type"] == 'arrayLiteral' and isinstance(index['value'], (int, float)):
            t[0] = lst["value"][index['value']+1]
        else:
            t[0] = {"type": "arrayReference",
                    "returnType": rreplace(lst["returnType"], ' harem', ''),
                    "value": [lst,
                              '[',
                              {"type": "numExpr",
                               "returnType": "waifu",
                               "value": index['value'] if isinstance(index['value'], (int, float)) else index},
                              ']'],
                    "line": t.lineno(1)}


def p_numExpr_number(t):
    'literal : NUMBER'
    t[0] = {"type": 'numExpr', "returnType": "waifu",
            "value": t[1], "line": t.lineno(1)}


def p_strExpr(t):
    'literal : STRING'
    t[0] = {"type": 'strExpr', "returnType": "senpai",
            "value": t[1][1:-1], "line": t.lineno(1)}


def p_bool(t):
    ''' literal : OWO
                | UWU
    '''
    t[0] = {
        "type": "boolExpr",
        "returnType": "catgirl",
        "value": True if t[1] == 'uwu' else False,
        "line": t.lineno(1)
    }


def p_fnType(t):
    ''' fnType : YOKAI
               | type
    '''
    t[0] = {'type': 'type', "value": t[1],
            "line": t.lineno(1)} if t[1] == 'yokai' else t[1]


def p_type(t):
    ''' type : WAIFU
             | HUSBANDO
             | CATBOY
             | CATGIRL
             | SENPAI
             | KOUHAI
    '''
    t[0] = {'type': 'type', "value": t[1], "line": t.lineno(1)}


def p_empty(t):
    ''' empty : '''
    pass


# def p_error(t):
#     if t:
#         raise SyntaxError('invalid syntax', (None, t.lineno, None, t.value))
#     else:
#         raise SyntaxError('unexpected EOF while parsing',
#                           (None, None, None, None))


def make_parser():
    return yacc.yacc()


def make_ast(sourceCode, parser):
    return parser.parse(sourceCode, debug=log)


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
