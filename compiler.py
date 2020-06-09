#!/usr/bin/python3

import re
import shlex
import enum
import sys

class Token(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211

def lex(string):
    lexer = shlex.shlex(string)
    return [ getToken(string) for string in list(lexer) ]

def getToken(string):
    numberRe = re.compile(r"\d+(\.\d+)?")
    stringRe = re.compile(r"\".*\"")
    labelRe = re.compile(r"[A-z]\w+")

    tokenDict = {
        '\0': Token.EOF,
        '\n': Token.NEWLINE,
        "=": Token.EQ,
        '+': Token.PLUS,
        '-': Token.MINUS,
        '*': Token.ASTERISK,
        '/': Token.SLASH,
        "GOTO": Token.GOTO,
        "PRINT": Token.PRINT,
        "INPUT": Token.INPUT,
        "LET": Token.LET,
        "IF": Token.IF,
        "THEN": Token.THEN,
        "ENDIF": Token.ENDIF,
        "WHILE": Token.WHILE,
        "REPEAT": Token.REPEAT,
        "ENDWHILE": Token.ENDWHILE,
        "==": Token.EQEQ,
        "!=": Token.NOTEQ,
        '<': Token.LT,
        '<=': Token.LTEQ,
        '>': Token.GT,
        '>=': Token.GTEQ,
    }

    token = tokenDict.get(string)

    if token is None:
        if numberRe.fullmatch(string):
            return Token.NUMBER
        elif stringRe.fullmatch(string):
            return Token.STRING
        elif labelRe.fullmatch(string):
            return Token.LABEL
        else:
            raise Exception("Could not match token: " + string)

    return token

# statement ::=
#   | "PRINT" (expression | string) nl
#   | "LET" ident "=" expression nl
#   | "IF" comparison "THEN" nl {statement} "ENDWHILE" nl
#   | "WHILE" comparison "REPEAT" nl {statement} "ENDWHILE" nl
#   | "GOTO" ident nl
#   | "INPUT" ident nl
def statement(tokens):
    pass

def parse(tokens):
    pass

if __name__ == "__main__":
   tokens = lex("* test 1 \"Test\"")
   parse(tokens)
