import sys

class EToken:

    ID = 'ID'
    ASSIGN = 'ASSIGN'
    SEMICOL = 'SEMICOL'
    INT = 'INT'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULT = 'MULT'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    PRINT = 'PRINT'
    END = 'END'
    ERROR = 'ERROR'
    
    # Skilgreina fasta fyrir tókakóða
    #ID, ASSIGN, SEMICOL, INT, PLUS, MINUS, MULT, LPAREN, RPAREN, PRINT, END, ERROR = range(12)

    def __init__(self, lexeme, token_code):
        #print("Inside EToken")
        self.lexeme = lexeme  # Lesið (lexeme) sem strengur
        self.token_code = token_code  # Tókakóði sem integer

    def __str__(self):
        # Snýr til baka strengjaframsetningu af tókanum, gagnlegt fyrir prentun og debug
        return self.token_code