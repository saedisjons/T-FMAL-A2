import sys

class EToken:
    # Skilgreina fasta fyrir tókakóða
    ID, ASSIGN, SEMICOL, INT, PLUS, MINUS, MULT, LPAREN, RPAREN, PRINT, END, ERROR = range(12)

    def __init__(self, lexeme, token_code):
        self.lexeme = lexeme  # Lesið (lexeme) sem strengur
        self.token_code = token_code  # Tókakóði sem integer

    def __str__(self):
        # Snýr til baka strengjaframsetningu af tókanum, gagnlegt fyrir prentun og debug
        return f"EToken({self.lexeme}, {self.token_code})"