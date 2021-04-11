import argparse
import json
import re

# we wont need this once we write straight to uhh the thing
removeSpace = False


def convertToStr(lst, encl=0):
    out = ''
    for i in prune(lst):
        if encl:
            out += '\t'*encl
        out += i
    if(removeSpace):
        out = re.sub('[\t\n]+', '', out)  # Remove whitespace
        # Remove space between special chars
        out = re.sub('\s*(\W)\s*', r'\1', out)
        return out
    else:
        return out


def prune(lst):
    ret = []
    digit = re.compile(r'([0-9]*[.])?[0-9]+')
    for i in lst:
        if digit.match(i) or i in ['true', 'false'] \
            or i.startswith("'")\
                or i.startswith("[") or i == "":
            pass
        else:
            ret.append(i)
    return ret


class JSConverter():

    def __init__(self):
        self.currentClosure = 0
        self.fakeSwitch = {
            'functionDeclaration': self.functionDeclaration,
            'declaration': self.declaration,
            'constDeclaration': self.constDeclaration,
            'enclosure': self.enclosure,
            'initialize': self.initialize,
            'constInitialize': self.constInitialize,
            'program': self.program,
            'short_binop': self.short_binop,
            'numExpr': self.numExpr,
            'boolExpr': self.boolExpr,
            'letReference': self.letReference,
            'return': self.ret,
            'functionCall': self.functionCall,
            'reassign': self.reassign,
            'ternaryOp': self.ternaryOp,
            'cond': self.conditional,
            'if': self.ifstmt,
            'else': self.elsestmt,
            'whileLoop': self.whileLoop,
            'forLoop': self.forLoop,
            'forTrio': self.forTrio,
            'forElement': self.forElement,
            'arrayLiteral': self.arrayLiteral,
            'printCall': self.printCall,
            'lengthCall': self.lengthCall,
            'arrayAssign': self.arrayAssign,
            'arrayReference': self.arrayReference,
            'strExpr': self.strExpr,
            'strReference': self.strReference,
            'arrExpr': self.arrExpr,
        }

    # def writeToFile(self,f,lst):
    #     for i in lst:
    #         if not isinstance(i, (dict,list)):
    #             f.write(i)
    #         else:
    #             self.writeToFile(f,)

    def program(self, val):
        def mapper(x):
            return self.typeTransfer(x['type'], x['value'])
        statements = []
        if isinstance(val, list):
            statements = list(map(mapper, val))
        else:
            if val == None:
                return ''
            statements = [self.typeTransfer(val['type'], val['value'])]

        return convertToStr(statements)

    def strExpr(self, val, special=False):

        if isinstance(val, str):
            return "'{}'".format(val.replace("'", "\\'"))
        else:
            return '{} + {}'.format(self.typeTransfer(val['value'][0]['type'],
                                                      val['value'][0]['value'], True), self.typeTransfer(val['value'][1]['type'],
                                                                                                         val['value'][1]['value'], True))

    def arrExpr(self, val, special=False):
        return '{}.concat({})'.format(self.typeTransfer(val['value'][0]['type'],
                                                        val['value'][0]['value'], True), self.typeTransfer(val['value'][1]['type'],
                                                                                                           val['value'][1]['value'], True)) + ('' if special else ';\n')

    def strReference(self, val, special=False):
        return '{}[{}]'.format(self.typeTransfer(val[0]['type'],
                                                 val[0]['value'], True), self.typeTransfer(val[2]['type'],
                                                                                           val[2]['value'], True)) + ('' if special else ';\n')

    def functionDeclaration(self, val):
        if not val['referenced']:
            return ''
        val = val['value']
        return 'const {} = ({}) => {}'.format(val[0],
                                              str(list(map(lambda x: self.typeTransfer(x['type'], x['value'],
                                                                                       True), val[2])))[1:-1].replace('\'', ''),
                                              self.typeTransfer(val[4]['type'], val[4]['value']))

    def declaration(self, val, special=False):
        if not val['referenced']:
            return ''
        return '{}'.format(val['value']) if special == True else ('let {}'.format(val['value']) if special == 2 else'let {};\n'.format(val['value']))

    def enclosure(self, val, special=False):
        self.currentClosure += 1
        out = '{\n' + \
            (convertToStr(list(map(lambda x: self.typeTransfer(x['type'], x['value']), val[1])), self.currentClosure) if isinstance(val[1], list)
             else self.typeTransfer(val[1]['type'], val[1]['value'])) \
            + ('\t'*(self.currentClosure-1)) + '}'
        self.currentClosure -= 1
        return out + ('' if special else ';\n')

    def initialize(self, val, special=False):
        if not val[0]['value']['referenced']:
            return ''
        val[0] = val[0]['value']
        return 'let {} = {}'.format(val[0]['value'],
                                    self.typeTransfer(val[2]['type'], val[2]['value'], True)) + ('' if special else ';\n')

    def constInitialize(self, val):

        if not val[0]['value']['referenced']:
            return ''
        val[0] = val[0]['value']
        return 'const {} = {};\n'.format(val[0]['value'], self.typeTransfer(val[2]['type'], val[2]['value'], True))

    def constDeclaration(self, val, _special=None):
        if not val['referenced']:
            return ''
        return 'const {}'.format(val['value'])

    def short_binop(self, val, special=False):
        if len(val) > 2:
            return '{} {} {}'.format(*val[0:2], self.typeTransfer(val[2]['type'], val[2]['value'])) \
                + (''if special else';\n')
        else:
            return '{}{}'.format(*val) + (''if special else';\n')

    def numExpr(self, val, special=False):
        if isinstance(val, (int, float)):
            return str(val)
        else:
            out = ''
            if not isinstance(val, list):
                if not val['type'] in ['arrayReference', 'letReference', 'numExpr']:
                    isParen = val['value'][0] == '('
                    val1 = val['value'][0 + int(isParen)]
                    val2 = val['value'][1 + int(isParen)]
                    out = ('('if isParen else '') +\
                        '{} {} {}'.format(self.typeTransfer(val1['type'], val1['value'], True), val['type'], self.typeTransfer(val2['type'], val2['value'], True))\
                        + (')'if isParen else '')
                else:
                    out = self.typeTransfer(val['type'], val['value'], True)
            else:
                if isinstance(val[0], str):
                    squiggly = False
                    if len(val) == 3:
                        squiggly = True
                    out = ('({})' if squiggly else '{}').format(
                        ('-'if val[0] == '-' else '')+self.typeTransfer(val[1]['type'], val[1]['value'], 2 if (val[0] == '-' and val[1]['type'] == 'numExpr')else True))
                else:
                    out = ('({})' if special == 2 else '{}').format(
                        self.typeTransfer(val[0]['type'], val[0]['value'], True))
            return out + ('' if special == True else ';\n')

    def boolExpr(self, val, special=False):
        if isinstance(val, bool):
            return str(val).lower()
        else:
            out = ''
            if not isinstance(val, list):
                if not val['type'] in ['arrayReference', 'letReference', 'boolExpr']:
                    isParen = val['value'][0] == '('
                    op = val['type'].replace('==', '===').replace("!=", "!==")
                    val1 = val['value'][0 + int(isParen)]
                    val2 = val['value'][1 + int(isParen)]
                    out = ('('if isParen else '') +\
                        '{} {} {}'.format(self.typeTransfer(val1['type'], val1['value'], True), op, self.typeTransfer(val2['type'], val2['value'], True))\
                        + (')'if isParen else '')
                else:
                    out = self.typeTransfer(val['type'], val['value'], True)
            else:
                if isinstance(val[0], str):
                    squiggly = False
                    if len(val) == 3:
                        squiggly = True
                    out = ('({})' if squiggly else '{}').format(
                        ('!'if val[0] == '!'else '')+self.typeTransfer(val[1]['type'], val[1]['value'], 2 if (val[0] == '!' and val[1]['type'] == 'boolExpr')else False))
                else:
                    out = ('({})' if special == 2 else '{}').format(
                        self.typeTransfer(val[0]['type'], val[0]['value']))
            return out + ('' if special == True else ';\n')

    def letReference(self, val):
        return val['value']

    def ret(self, val):
        if val['type'] == "null":
            return 'return;\n'
        else:
            return 'return {};\n'.format(self.typeTransfer(val['type'], val['value'], True))

    def functionCall(self, val, special=False):
        out = ''
        for i in val:
            if isinstance(i, str):
                out += i
            else:
                out += self.typeTransfer(i['type'], i['value'])+', '
        return out.replace(', )', ')') + ('' if special else ';\n')

    def reassign(self, val, special=False):
        return '{} = {}'.format(val[0], self.typeTransfer(val[2]['type'], val[2]['value'], True))+(''if special else ';\n')

    def ternaryOp(self, val, _=False):
        i = 0
        if val[0] == '(':
            return "("+self.ternaryOp(val[1]['value'])+")"

        val0 = self.typeTransfer(val[0+i]['type'], val[0+i]['value'], True)
        val2 = self.typeTransfer(val[2+i]['type'], val[2+i]['value'], True)
        val4 = self.typeTransfer(val[4+i]['type'], val[4+i]['value'], True)
        return '{} ? {} : {}'.format(val0, val2, val4)

    def conditional(self, val):
        val0 = self.typeTransfer(val[0]['type'], val[0]['value'], len(val) > 1)
        val1 = ''
        if len(val) > 1:
            val1 = self.typeTransfer(val[1]['type'], val[1]['value'])
        return '{}{}'.format(val0, val1)

    def ifstmt(self, val, special=False):
        val1 = self.typeTransfer(val[1]['type'], val[1]['value'], True)
        val2 = self.typeTransfer(val[3]['type'], val[3]['value'], special)
        return ('if ({}) {}'.format(val1, val2))

    def elsestmt(self, val):
        val1 = self.typeTransfer(val[1]['type'], val[1]['value'])
        return 'else {}'.format(val1)

    def whileLoop(self, val):
        return 'while ({}) '.format(self.typeTransfer(val[2]['type'],
                                                      val[2]['value'], True)) + self.typeTransfer(val[-1]['type'], val[-1]['value'])

    def forLoop(self, val):
        return 'for ({}) '.format(self.typeTransfer(val[2]['type'], val[2]['value'])) + self.typeTransfer(val[4]['type'], val[4]['value'])

    def forTrio(self, val):
        return '{}; {}; {}'.format(self.typeTransfer(val[0]['type'], val[0]['value'], 2),
                                   self.typeTransfer(val[2]['type'],
                                                     val[2]['value'], True),
                                   self.typeTransfer(val[4]['type'], val[4]['value'], True))

    def forElement(self, val):
        return '{} of {}'.format(self.typeTransfer(val[0]['type'], val[0]['value'], 2),
                                 self.typeTransfer(val[2]['type'], val[2]['value'], True))

    def arrayLiteral(self, val):
        return str(list(map(lambda x: self.typeTransfer(x['type'], x['value'], True), val[1:-1]))).replace("'", '')

    def arrayAssign(self, val, special=False):
        return '{}[{}] = {}'.format(val[0],
                                    self.typeTransfer(
                                        val[2]['type'], val[2]['value'], True),
                                    self.typeTransfer(val[5]['type'], val[5]['value'], True)) + (''if special else ';\n')

    def arrayReference(self, val, special=False):
        return '{}[{}]'.format(self.typeTransfer(val[0]['type'], val[0]['value'], True),
                               self.typeTransfer(val[2]['type'], val[2]['value'], True)) + ('' if special else ';\n')

    def printCall(self, val):
        return 'console.log({});\n'.format(self.typeTransfer(val[2]['type'], val[2]['value'], True))

    def lengthCall(self, val, special=False):
        return '{}.length'.format(self.typeTransfer(val[2]['type'], val[2]['value'], True)) + ('' if special else ';\n')

    def typeTransfer(self, typeName, val, specialCase=False):
        try:
            if specialCase:
                try:
                    return self.fakeSwitch[typeName](val, specialCase)
                except TypeError:
                    return self.fakeSwitch[typeName](val)
            else:
                return self.fakeSwitch[typeName](val)
        except KeyError as e:
            print(e)
            raise(e)


if __name__ == "__main__":
    argParser = argparse.ArgumentParser(
        description='Take in the OwOScript ast and convert it into runnable JS code.')
    argParser.add_argument(
        'FILE', help="Input file with OwOScript ast")
    argParser.add_argument('-whitespace', '--whitespace',
                           help="Turn white space optimization on", action="store_true")
    args = argParser.parse_args()
    if args.whitespace:  # Flag to turn on white space remover
        removeSpace = True
    with open(args.FILE) as ast:
        astAsDict = json.load(ast)
        with open('{}.js'.format(args.FILE.split('.owo')[0]), 'w') as f:
            converter = JSConverter()
            f.write(converter.typeTransfer(
                astAsDict['type'], astAsDict['value']))
            print("compiling complete")
