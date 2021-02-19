import argparse
from ply import lex

# MOST OF THIS IS TOLEN FROM KYOS LAB, I'll go through it setting up more of what's actually to stay

# List of token names. This is always required
tokens = [
    'NUMBER',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LT',
    'LEQ',
    'GT',
    'GEQ',
    'EQOP',
    'NEQ',
    'AND',
    'OR',
    'NOT',
    'SEMICOL',
    'PERIOD',
    'COMMA',
    'EQ',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'LBRACE',
    'RBRACE',
    'SQUIGGLY',
    'MULTID',
    'PEQ',
    'MEQ',
    'TEQ',
    'DEQ',
    'PP',
    'MM'
]

# Reserved words which should not match any IDs we need to add this
reserved = {
    "real": "REAL",
    "waifu": "WAIFU",
    "catgirl": "CATGIRL",
    "chan": "CHAN",
    "kun": "KUN",
    "san": "SAN",
    "yokai": "YOKAI",
    "owo": "OWO",
    "uwu": "UWU",
    "desu": "DESU",
    "harem": "HAREM",
    "nani": "NANI",
    "noU": "NOU",
    "whileU": "WHILEU",
    "iStudied": "ISTUDIED",
    "shi": "SHI"
}

# Add reserved names to list of tokens
tokens += list(reserved.values())


class OwOScriptLexer():
    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Regular expression rule with some action code
    t_PP = r'\+\+'
    t_MM = r'--'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LEQ = r'\<='
    t_LT = r'\<'
    t_GEQ = r'\>='
    t_GT = r'\>'
    t_SQUIGGLY = r'\~'
    t_EQOP = r'\=='
    t_NEQ = r'\!='
    t_AND = r'\&&'
    t_OR = r'\|\|'
    t_NOT = r'\!'
    t_SEMICOL = r';'
    t_PERIOD = r'\.'
    t_COMMA = r','
    t_EQ = r'\='
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LBRACK = r'\['
    t_RBRACK = r'\]'
    t_MULTID = r'\^'
    t_PEQ = r'\+='
    t_MEQ = r'\-='
    t_TEQ = r'\*='
    t_DEQ = r'\/='

   # A regular expression rule with some action code
    def t_NUMBER(self, t):
        # This needs to be like dynamic, it should be a float unless integer, but numbers are like a single thing so
        r'([0-9]*[.])?[0-9]+'
        try:
            t.value = int(t.value)
        except ValueError:
            t.value = float(t.value)
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'ID')  # Check for reserved words
        return t

    # Define a rule so we can track line numbers. DO NOT MODIFY
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule. DO NOT MODIFY
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer. DO NOT MODIFY
    def build(self, **kwargs):
        self.tokens = tokens
        self.lexer = lex.lex(module=self, **kwargs)

    # Test the output. DO NOT MODIFY
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)


m = OwOScriptLexer()
m.build()
# Main function. DO NOT MODIFY
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Take in the OwOScript source code and perform lexical analysis.')
    parser.add_argument('FILE', help="Input file with OwOScript source code")
    args = parser.parse_args()

    f = open(args.FILE, 'r')
    data = f.read()
    f.close()

    m.test(data)
