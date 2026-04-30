# PARSER CLASS
# IBRAHIM ALI
# 04/29/2026
# Final Project
# DESCRIPTION: Parser class is used to convert the tokens produced by the Lexer
# into an Abstract Syntax Tree (AST). It builds ASTNode objects for commands needed
# for example DEPOSIT, WITHDRAW, BALANCE, and CREATE.

from lib.bank.ASTNode import ASTNode

class Parser:
    def __init__(self, tokens):

        # Tokens from the lexer
        self.tokens = tokens

        # Checks and keeps track of the token that is being read
        self.position = 0

    # Returns the current token being read but if it at the end it returns None
    def current(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    # Returns the current token and moves forward by one
    def eat(self):
        token = self.current()
        self.position += 1
        return token

    def parse(self):
        token = self.current()

        if token is None:
            raise Exception("No input")

        action = token.get_value().lower()

        # The parser matches the command
        if action == "deposit":
            return self.parse_deposit()

        if action == "withdraw":
            return self.parse_withdraw()

        if action == "balance":
            return self.parse_balance()

        if action == "create":
            return self.parse_create()

        # Returns error if command is not among the 4
        raise Exception("The command is not used in this Banking System.")

    # deposit ACCOUNT NUMBER
    def parse_deposit(self):
        root = ASTNode("DEPOSIT")
        self.eat()
        acc = self.eat()
        amt = self.eat()

        # Add child notes to the AST
        root.add_child(ASTNode("ACCOUNT_NUMBER", acc.get_value()))
        root.add_child(ASTNode("NUMBER", amt.get_value()))
        return root

    # withdraw ACCOUNT NUMBER
    def parse_withdraw(self):
        root = ASTNode("WITHDRAW")
        self.eat()
        acc = self.eat()
        amt = self.eat()

        root.add_child(ASTNode("ACCOUNT_NUMBER", acc.get_value()))
        root.add_child(ASTNode("NUMBER", amt.get_value()))
        return root

    # balance ACCOUNT NUMBER
    def parse_balance(self):
        root = ASTNode("BALANCE")
        self.eat()  # action
        acc = self.eat()

        root.add_child(ASTNode("ACCOUNT_NUMBER", acc.get_value()))
        return root

    # create FIRST LAST ACCOUNT
    def parse_create(self):
        root = ASTNode("CREATE")
        self.eat()  # action
        first = self.eat()
        last = self.eat()
        acc = self.eat()

        root.add_child(ASTNode("FIRST_NAME", first.get_value()))
        root.add_child(ASTNode("LAST_NAME", last.get_value()))
        root.add_child(ASTNode("ACCOUNT_NUMBER", acc.get_value()))
        return root
