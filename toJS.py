import json


def program(val):
    statements = list(map(lambda x: typeTransfer(x['type'], x['value']), val)) if isinstance(val, list) \
        else [typeTransfer(val['type'], val['value'])]

    out = ''
    for i in statements:
        out += i
    return out


def functionDeclaration(val):
    return 'const {} =  ({}) => '.format(val[0], str(list(map(lambda x: typeTransfer(
        x['type'], x['value'], True))))[1:-1])


def declaration(val, special=False):
    return val['value'] if special \
        else 'let {};\n'.format(val['value']),


def enclosure(val):
    return '{' + \
        str(list(map(lambda x: typeTransfer(x['type'], ['value']), val[1]))) if isinstance(val[1], list) \
        else typeTransfer(val[1]['type'], val[1]['value']) \
        + '}\n'


def initialize(val, special=False):
    return ('let {} = {}'.format(val[0]['value'],
                                 val[2]['value']) + ('' if special else ';\n')).replace('True', 'true').replace('False', 'false')


def constInitialize(val):
    return ('const {} = {};\n'.format(val[0]['value'], val[2]['value'])).replace('True', 'true').replace('False', 'false')


fakeSwitch = {
    'functionDeclaration': functionDeclaration,
    'declaration': declaration,
    'encolsure': enclosure,
    'initialize': initialize,
    'constInitialize': constInitialize,
    'program': program
}


def typeTransfer(typeName, val, specialCase=False):
    try:
        if specialCase:
            return fakeSwitch[typeName](val, specialCase)
        else:
            return fakeSwitch[typeName](val)
    except KeyError as e:
        # print(e)
        return ''


with open('./Example/expr_example.owo.json') as ast:
    astAsDict = json.load(ast)
    with open('test.js', 'w') as f:
        f.write(typeTransfer(astAsDict['type'], astAsDict['value']))
    print("parsing complete")
