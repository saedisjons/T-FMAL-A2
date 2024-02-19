from etoken import EToken
from elexer import ELexer
class EParser:
    def __init__(self, lexer):
        #print("Inside EParser")
        self.lexer = lexer
        self.curr_token = None
        self.next_token()

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()

    def error(self):
        #print("error")
        raise Exception("Syntax error")
    
    def match(self, expected_token_code):
        #print(f"matching {expected_token_code}")
        if self.curr_token.token_code == expected_token_code:
            self.next_token()
        else:
            self.error()

    def parse(self):
        #print("parse")
        self.statements()
        if self.curr_token.token_code != EToken.END:
            self.parse()

    def statements(self):
        #print("statements")
        if self.curr_token.token_code in [EToken.ID, EToken.PRINT]:
            self.statement()
            self.next_token()
            if self.curr_token.token_code == EToken.SEMICOL:
                #print("Expected SEMICOL")
                self.next_token()
                #print("curr token is", self.curr_token.token_code)
                self.statements()
        elif self.curr_token.token_code != EToken.END:
            #print(f"Expected ID or PRINT, got {self.curr_token.token_code}")
            self.error()

    def statement(self):
        #print("statement")
        if self.curr_token.token_code == EToken.ID:
            self.assign()
        elif self.curr_token.token_code == EToken.PRINT:
            self.match(EToken.PRINT)  # Staðfesta að um prentun sé að ræða
            self.print_statement()
        else:
            self.error()

    def assign(self):
        var_name = self.curr_token.lexeme
        self.match(EToken.ID)
        self.match(EToken.ASSIGN)
        self.expr()
        print(f"PUSH {var_name}")
        print("ASSIGN")

    def print_statement(self):
        #print("print_statement")
        self.match(EToken.PRINT)  # Staðfesta að um prentun sé að ræða
        var_name = self.curr_token.lexeme
        self.match(EToken.ID)  # Staðfesta að eftir prentun komi breytuheiti
        print(f"PUSH {var_name}")  # Útskrift fyrir að ýta breytuheiti á staflið
        print("PRINT")  # Skrifa út PRINT skipun

    def expr(self):
        #print("expr")
        self.term()
        while self.curr_token.token_code in [EToken.PLUS, EToken.MINUS]:
            if self.curr_token.token_code == EToken.PLUS:
                self.match(EToken.PLUS)
                self.term()
                print("ADD")  # Skrifa út ADD skipun
            elif self.curr_token.token_code == EToken.MINUS:
                self.match(EToken.MINUS)
                self.term()
                print("SUB")  # Skrifa út SUB skipun

    def term(self):
        self.factor()
        while self.curr_token.token_code in [EToken.MULT]:  # Assuming DIV for division
            op = self.curr_token.token_code
            self.next_token()
            self.factor()
            if op == EToken.MULT:
                print("MULT")

    def factor(self):
        if self.curr_token.token_code == EToken.INT:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()
        elif self.curr_token.token_code == EToken.ID:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()
        elif self.curr_token.token_code == EToken.LPAREN:
            self.next_token()
            self.expr()
            self.match(EToken.RPAREN)