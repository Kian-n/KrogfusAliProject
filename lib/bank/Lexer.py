# LEXER CLASS
# Taite Krogfus
# 04/28/2026
# Final Project
# DESCRIPTION: The Lexer class reads user input and breaks it into
# tokens based on the rules(EBNF) of the Banking DSL. It identifies
# commands, account numbers, and numeric values, converting text into
# defined token objects. This is the first step in processing DSL commands.
# imports the Token class

from lib.bank.Token import Token

class Lexer:
    def __init__(self, text):
        self.__text = text
        self.__tokens = [] #creates array to store tokens

    def get_text(self):
        return self.__text

    def get_tokens(self):
        return self.__tokens

    def tokenize(self):
        words = self.__text.strip().split()

        # accepts upper and lower case inputs for commands
        for word in words:
            lower_word = word.lower()

            # DSL commands
            if lower_word in ["deposit", "withdraw", "balance", "create"]:
                token = Token("ACTION", lower_word)

            # check if number
            elif word.replace(".", "", 1).isdigit():
                token = Token("NUMBER", float(word))

            # check if acc#, 8chars, 2 preceding letters...
            # and 6 following digits
            elif len(word) == 8 and word[:2].isalpha() and word[2:].isdigit():
                token = Token("ACCOUNT_NUMBER", word.upper())

            else:
                token = Token("WORD", word.upper())

            self.__tokens.append(token)

        return self.__tokens
