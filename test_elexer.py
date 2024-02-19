from elexer import ELexer
from etoken import EToken

if __name__ == "__main__":
    lexer = ELexer()                        # Búa til nýtt instance af ELexer klasanum
    curr_token = EToken("",EToken.ERROR)    # Búa til upphafstákn með tóku gildi og 

    while curr_token.token_code != EToken.END:  # Ef current token er ekki END token
        curr_token = lexer.get_next_token()     # Sækja næsta token og setja það sem current token
        print(curr_token)                       # Prenta út current token