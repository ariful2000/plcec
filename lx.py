from sly import Lexer

class Lex(Lexer):
    
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    tokens = { 
        IF, 
        THEN, 
        ELSE,
        FOR, 
        FUN, 
        TO, 
        ARROW, 
        EQEQ, 
        NAME, 
        NUMBER, 
        STRING }

    ignore = '\t '

    IF = r'IF'
    THEN = r'THEN'
    ELSE = r'ELSE'
    FOR = r'FOR'
    FUN = r'FUN'
    TO = r'TO'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')



if __name__ == '__main__':
    lexer = Lex()
    env = {}
    while True:
        try:
            text = input('Start ==> ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
