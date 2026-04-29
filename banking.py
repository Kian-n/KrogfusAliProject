# I/O LOGIC TO BE ADDED TO MAIN CLASS
# Taite Krogfus
# 04/28/2026
# Final Project
# DESCRIPTION: Handles all input and output operations for the Banking program,
# including reading account data from a file and displaying it to the user.
# It manages user interaction through menu options, allowing users to access accounts,
# perform transactions, and create new accounts. Newly created accounts are also written
# back to the file for persistent storage.

import random
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
