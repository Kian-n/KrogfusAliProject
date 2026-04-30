# banking.py
# Taite Krogfus and Ibrahim Ali
# 04/28/2026
# Final Project
# DESCRIPTION: Handles all input and output operations for the Banking program,
# including reading account data from a file and displaying it to the user.
# It manages user interaction through menu options, allowing users to access accounts,
# perform transactions, and create new accounts. Newly created accounts are also written
# back to the file for persistent storage.

import random

# Imports our lib files to main
from lib.bank.Lexer import Lexer
from lib.bank.Parser import Parser
from lib.bank.Evaluator import Evaluator
from lib.BankAccount import BankAccount

# var that stores the AccountCreation text file
ACCOUNTS_FILE = "AccountCreation.txt"

# load accounts from the file AccountCreation.txt
def load_accounts(filename):
    accounts = {}

    random.seed(8)  # keeps balances consistent for testing

    # read the file
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            # handles the formatting of the text file and creating the objects needed for accounts
            if len(parts) == 3:
                first_name = parts[0]
                last_name = parts[1]
                account_number = parts[2]

                #populate balance 1-1000 and round to 2 dec places
                balance = round(random.uniform(1, 1000), 2)

                account = BankAccount(first_name, last_name, account_number, balance)
                accounts[account_number] = account

    return accounts

# Method to display the accounts
def display_accounts(accounts):
    print("\nAccounts:")

    for account_number in accounts:
        account = accounts[account_number]

        print(account.get_first_name(),
              account.get_last_name(),
              account.get_account_number(),
              "$" + format(account.get_balance(), ".2f"))


# method to create accounts and write new entries to
# file AccountCreation.txt
def create_account(accounts):
    # validate first name
    valid_first = False
    while not valid_first:
        first_name = input("Enter first name: ").upper()
        if first_name.isalpha() and len(first_name) > 0:
            valid_first = True
        else:
            print("Invalid input. Enter letters only.")

    # validate last name
    valid_last = False
    while not valid_last:
        last_name = input("Enter last name: ").upper()
        if last_name.isalpha() and len(last_name) > 0:
            valid_last = True
        else:
            print("Invalid input. Enter letters only.")

    # generate account number (2 letters + 6 digits)
	#restricts the letters to the first letter of both
	#first and last name and ensures their capitalization
    initials = first_name[0].upper() + last_name[0].upper()

    # ask user for 6 digits for acc#
    valid = False
    account_number = ""
    while not valid:
        digits = input("Enter 6-digit number for account: ")

        if digits.isdigit() and len(digits) == 6:
            account_number = initials + digits

            if account_number not in accounts:
                valid = True
            else:
                print("Account number already exists. Try different digits.")
        else:
            print("Invalid input. Must be exactly 6 digits.")

    # allows user to enter a starting balance for new account
    balance = float(input("Enter starting balance: "))

    account = BankAccount(first_name, last_name, account_number, balance)
    accounts[account_number] = account

    # write to file
    with open(ACCOUNTS_FILE, "a") as file:
        file.write(f"{first_name} {last_name} {account_number}\n")

    print("Account created successfully.")
    print("Account number:", account_number)

# MAIN PROGRAM START

def main():
    # load the initial accounts
    accounts = load_accounts(ACCOUNTS_FILE)

    # Add evaluator which runs the DSL Commands
    evaluator = Evaluator(accounts)

    # Main Loop
    running = True

    while running:

        # Displays the Main Menu
        print("BANKING SYSTEM")
        print("1. Log into an account")
        print("2. Create a new account")
        print("3. Display all accounts")
        print("4. Exit program")

        # Asks the user to choose a menu option
        choice = input("Choose an option: ")

        # Log into an existing account by Account Number
        if choice == "1":
            account_id = input("Enter account number: ").upper()

            # Check if the account exists
            if account_id in accounts:
                account_session(accounts, evaluator, account_id)

            # Lets the user know if account does not exist
            else:
                print("Sorry, The Account Listed does not exist in our Bank. Would you like to create one?")

        # Create a new account
        elif choice == "2":
            create_account(accounts)

        # Show all the accounts in the program
        elif choice == "3":
            display_accounts(accounts)

        # Ends the Program
        elif choice == "4":
            print("Thank you for banking with us.")
            running = False

        else:
            print("Invalid option. Please try again.")

# DSL COMMANDS WHILE LOOP IS RUNNING
def account_session(accounts, evaluator, account_id):
    session_active = True

    while session_active:
        print(f"ACCOUNT {account_id}")
        print("Available DSL commands:")
        print("  deposit <account> <amount>")
        print("  withdraw <account> <amount>")
        print("  balance <account>")
        print("  logout")

        command = input("> ")

        if command.lower() == "logout":
            print("Logging out.")
            session_active = False
        else:
            # run DSL command
            lexer = Lexer(command)
            tokens = lexer.tokenize()

            parser = Parser(tokens)
            ast = parser.parse()

            evaluator.evaluate(ast)

# RUN MAIN

if __name__ == "__main__":
    main()
