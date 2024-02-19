from elexer import ELexer
from etoken import EToken

if __name__ == "__main__":
    lexer = ELexer()
    curr_token = EToken("",EToken.ERROR)

    while curr_token.token_code != EToken.END:
        curr_token = lexer.get_next_token()
        print(curr_token)