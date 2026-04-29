# TOKEN CLASS
# Taite Krogfus
# 04/28/2026
# Final Project
# DESCRIPTION: Defines the Token class used to represent individual pieces of input in
# the Banking DSL. Each token stores a token type (such as ACTION, NUMBER,
# or ACCOUNT_NUMBER) and its associated value. These tokens are produced by the
# Lexer and then used by the Parser.
# Token class stores: token_type and value
# Is imported into Lexer.py class

class Token:
    def __init__(self, token_type, value):
        self.__token_type = token_type
        self.__value = value

    def get_token_type(self):
        return self.__token_type

    def get_value(self):
        return self.__value

    def set_token_type(self, token_type):
        self.__token_type = token_type

    def set_value(self, value):
        self.__value = value

    def __str__(self):
        return f"Token({self.__token_type}, {self.__value})"

    def __repr__(self):
        return self.__str__()
