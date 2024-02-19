import sys
from etoken import EToken

class ELexer:
    def __init__(self):
        #print("Inside ELexer")
        self.current_char = None
        self.read_next_char()

    def read_next_char(self):
        self.current_char = sys.stdin.read(1) if self.current_char != '' else ''

    def get_next_token(self):
        #print("In get next token with current char: ", self.current_char)
        self.skip_whitespace()
        if not self.current_char:  # End of input
            print("End of input")
            return EToken('', EToken.END)

        token = None
        if self.current_char.isdigit():
            token = self.handle_number()
        elif self.current_char.isalpha():
            token = self.handle_identifier()
        elif self.current_char == '+':
            token = EToken('+', EToken.PLUS)
            self.read_next_char()
        elif self.current_char == '-':
            token = EToken('-', EToken.MINUS)
            self.read_next_char()
        elif self.current_char == '*':
            token = EToken('*', EToken.MULT)
            self.read_next_char()
        elif self.current_char == '(':
            token = EToken('(', EToken.LPAREN)
            self.read_next_char()
        elif self.current_char == ')':
            token = EToken(')', EToken.RPAREN)
            self.read_next_char()
        elif self.current_char == '=':
            token = EToken('=', EToken.ASSIGN)
            self.read_next_char()
        elif self.current_char == ';':
            token = EToken(';', EToken.SEMICOL)
            self.read_next_char()
        else:
            token = EToken(self.current_char, EToken.ERROR)
            self.read_next_char()

        return token

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.read_next_char()

    def handle_number(self):
        #print("Handling number")
        num_str = ''
        while self.current_char and self.current_char.isdigit():
            num_str += self.current_char
            self.read_next_char()
        return EToken(num_str, EToken.INT)

    def handle_identifier(self):
        #print("Handling identifier")
        id_str = ''
        while self.current_char and (self.current_char.isalpha() or self.current_char.isdigit()):
            id_str += self.current_char
            self.read_next_char()
        # Check for reserved keywords
        if id_str == 'end':
            #print("Found end")
            return EToken(id_str, EToken.END)
        elif id_str == 'print':
            #print("Found print")
            return EToken(id_str, EToken.PRINT)
        return EToken(id_str, EToken.ID)