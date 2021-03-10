import json

# we wont need this once we write straight to uhh the thing


def convertToStr(lst, encl=False):
    out = ''
    for i in lst:
        if encl:
            out+= '\t'
        out += i
    return out


def program(val):
    statements = list(map( \
        lambda x: typeTransfer(x['type'], x['value']), val)) \
        if isinstance(val, list) \
        else [typeTransfer(val['type'], val['value'])]
    return convertToStr(statements)


def functionDeclaration(val):
    return 'const {} = ({}) => {}'.format(val[0],
                                          str(list(map(lambda x: typeTransfer(x['type'], x['value'],
                                                                              True), val[2])))[1:-1].replace('\'', ''),
                                          typeTransfer(val[4]['type'], val[4]['value']))


def declaration(val, special=False):
    # print(val['value'], special)
    return val['value'] if special else 'let {};\n'.format(val['value'])


def enclosure(val):
    return '{\n' + \
        (convertToStr(list(map(lambda x: typeTransfer(x['type'], x['value']), val[1])), True) if isinstance(val[1], list)
         else typeTransfer(val[1]['type'], val[1]['value'])) \
        + '}\n'


def initialize(val, special=False):
    return 'let {} = {}'.format(val[0]['value'],
                                typeTransfer(val[2]['type'], val[2]['value'])) + ('' if special else ';\n')


def constInitialize(val):
    return 'const {} = {};\n'.format(val[0]['value'], typeTransfer(val[2]['type'], val[2]['value']))


def short_binop(val, special=False):
    return '{} {} {}'.format(*val[0:2], typeTransfer(val[2]['type'], val[2]['value'])) \
        + (''if special else';\n')


def numExpr(val, special=False):
    if isinstance(val, (int, float)):
        return str(val)
    else:
        if not isinstance(val, list):
            isParen = val['value'][0] == '('
            val1 = val['value'][0 + int(isParen)]
            val2 = val['value'][1 + int(isParen)]
            return ('('if isParen else '') +\
                '{} {} {}'.format(typeTransfer(val1['type'], val1['value']), val['type'], typeTransfer(val2['type'], val2['value']))\
                + (')'if isParen else '')
        else:
            if isinstance(val[0], str):
                if len(val) == 3:
                    special = True
                return ('({})' if special else '{}').format(
                    ('-'if val[0] == '-' else '')+typeTransfer(val[1]['type'], val[1]['value'], val[0] == '-' and val[1]['type'] == 'numExpr'))
            else:
                return ('({})' if special else '{}').format(typeTransfer(val[0]['type'], val[0]['value']))


def boolExpr(val, special=False):
    if isinstance(val, bool):
        return str(val).lower()
    else:
        if not isinstance(val, list):
            isParen = val['value'][0] == '('
            val1 = val['value'][0 + int(isParen)]
            val2 = val['value'][1 + int(isParen)]
            return ('('if isParen else '') +\
                '{} {} {}'.format(typeTransfer(val1['type'], val1['value']), val['type'], typeTransfer(val2['type'], val2['value']))\
                + (')'if isParen else '')
        else:
            if isinstance(val[0], str):
                if len(val) == 3:
                    special = True
                return ('({})' if special else '{}').format(
                    ('!'if val[0] == '!'else '')+typeTransfer(val[1]['type'], val[1]['value'], val[0] == '!' and val[1]['type'] == 'boolExpr'))
            else:
                return ('({})' if special else '{}').format(typeTransfer(val[0]['type'], val[0]['value']))


def letReference(val):
    return val['value']


def ret(val):
    return 'return {};\n'.format(typeTransfer(val['type'], val['value']))


def functionCall(val):
    out = ''
    for i in val:
        if isinstance(i, str):
            out += i
        else:
            out += typeTransfer(i['type'], i['value'])+', '
    return out.replace(', )', ')')


def reassign(val, special=False):
    return '{} = {}'.format(val[0], typeTransfer(val[2]['type'], val[2]['value']))+(''if special else ';\n')

def ternaryOp(val, special=False):
    val0 = typeTransfer(val[0]['type'], val[0]['value'])
    val2 = typeTransfer(val[2]['type'], val[2]['value'])
    val4 = typeTransfer(val[4]['type'], val[4]['value'])
    return '{} ? {} : {}'.format(val0,val2, val4)

def conditional(val, special=False):
    val0 = typeTransfer(val[0]['type'], val[0]['value'])
    val1 = ''
    if len(val) > 1:
        val1 = typeTransfer(val[1]['type'], val[1]['value'])
    return '{}{}'.format(val0, val1)

def ifstmt(val, special=False):
    val1 = typeTransfer(val[1]['type'], val[1]['value'])
    val2 = typeTransfer(val[3]['type'], val[3]['value'])
    return ('if ({}) {}'.format(val1, val2))

def elsestmt(val, special=False):
    val1 = typeTransfer(val[1]['type'], val[1]['value'])
    return 'else {}'.format(val1)

fakeSwitch = {
    'functionDeclaration': functionDeclaration,
    'declaration': declaration,
    'enclosure': enclosure,
    'initialize': initialize,
    'constInitialize': constInitialize,
    'program': program,
    'short_binop': short_binop,
    'numExpr': numExpr,
    'boolExpr': boolExpr,
    'letReference': letReference,
    'return': ret,
    'functionCall': functionCall,
    'reassign': reassign,
    'ternaryOp': ternaryOp,
    'cond': conditional,
    'if': ifstmt,
    'else': elsestmt
}


def typeTransfer(typeName, val, specialCase=False):
    try:
        if specialCase:
            return fakeSwitch[typeName](val, specialCase)
        else:
            return fakeSwitch[typeName](val)
    except KeyError as e:
        print(e)
        raise(e)


with open('./Example/function_example.owo.json') as ast:
    astAsDict = json.load(ast)
    with open('test.js', 'w') as f:
        f.write(typeTransfer(astAsDict['type'], astAsDict['value']))
    print("compiling complete")
