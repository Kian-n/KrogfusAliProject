# EVALUATOR CLASS
# IBRAHIM ALI
# 04/29/2026
# Final Project
# DESCRIPTION: The Evaluator reads the AST produced by the Parser and
# does the banking command. It describes the deposit, withdraw, balance, and create commands.
# Stores accounts using a dictionary which are directly mapped to our Bank Account Objects

from lib.bank.ASTNode import ASTNode
from lib.BankAccount import BankAccount

# var to store AccountCreation.txt
ACCOUNTS_FILE = "AccountCreation.txt"

class Evaluator:
    def __init__(self, accounts):
        # Accounts is the dictionary
        self.accounts = accounts

    # Determines which command to run based on the AST root node
    def evaluate(self, ast):
        node_type = ast.get_node_type()

        if node_type == "DEPOSIT":
            return self.eval_deposit(ast)

        elif node_type == "WITHDRAW":
            return self.eval_withdraw(ast)

        elif node_type == "BALANCE":
            return self.eval_balance(ast)

        elif node_type == "CREATE":
            return self.eval_create(ast)

        else:
            print("Please enter either DEPOSIT or WITHDRAW or BALANCE or CREATE.")

    # DEPOSIT
    def eval_deposit(self, ast):
        # Deposit command
        # 0 key is the account number
        # 1 key is the amount
        acc = ast.get_children()[0].get_value()
        amt = ast.get_children()[1].get_value()

        # Checks if the account does not exist and lets the user know
        if acc not in self.accounts:
            print("Account does not exist.")
            return

        self.accounts[acc].deposit(amt)
        print(f"Deposited {amt} into {acc}. New balance: {self.accounts[acc].get_balance()}")

    # WITHDRAW
    def eval_withdraw(self, ast):
        acc = ast.get_children()[0].get_value()
        amt = ast.get_children()[1].get_value()

        # Checks if the account does not exist and lets the user know
        if acc not in self.accounts:
            print("Account does not exist.")
            return

        # Check if the user can actually withdraw and lets them know if they can't
        if not self.accounts[acc].withdraw(amt):
            print("Insufficient funds. You are not allowed to withdraw more than your balance.")
            return

        print(f"Withdrew {amt} from {acc}. New balance: {self.accounts[acc].get_balance()}")

    # BALANCE
    def eval_balance(self, ast):
        acc = ast.get_children()[0].get_value()

        # Checks if the account does not exist and lets the user know
        if acc not in self.accounts:
            print("The Account does not exist.")
            return

        print(f"Balance for {acc}: {self.accounts[acc].get_balance()}")

    # CREATE
    def eval_create(self, ast):
        # Deposit command
        # 0 key is the First_Name
        # 1 key is the Last_Name
        # 2 key is the account number
        first = ast.get_children()[0].get_value()
        last = ast.get_children()[1].get_value()
        acc = ast.get_children()[2].get_value()

        # Lets the user know if the account already exists
        if acc in self.accounts:
            print("The Account already exists.")
            return

        # create account object
        self.accounts[acc] = BankAccount(first, last, acc, 0.00)

        # write to file
        with open(ACCOUNTS_FILE, "a") as file:
            file.write(f"{first} {last} {acc}\n")

        print(f"Created account {acc} for {first} {last} with balance 0.00")
