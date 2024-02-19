import sys
from elexer import ELexer
from eparser import EParser

if __name__ == "__main__":
    # Búa til tilvik af ELexer með staðlaða inntakið
    lexer = ELexer()
    
    # Búa til tilvik af EParser með lesgreininum sem inntak
    parser = EParser(lexer)
    
    # Setja þáttunina í gang
    parser.parse()
