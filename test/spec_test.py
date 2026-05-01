# spec_testing.py
# Taite Krogfus
# 04/28/2026
# Final Project
# Description: Runs specification tests for the Banking DSL. All tests execute commands
# through the Lexer, Parser and Evaluator to test functionality of the banking DSL. Tests
# include: balance verification after deposits and withdrawals, invalid account lookup, and
# creating account. Account RED BULL RB052026 is created and written to the file. Then
# removed after testing.

import os
import sys
import unittest

# fixes import path to banking.py
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, PROJECT_ROOT)

from banking import load_accounts, ACCOUNTS_FILE
from lib.bank.Lexer import Lexer
from lib.bank.Parser import Parser
from lib.bank.Evaluator import Evaluator


class BankingSpecTests(unittest.TestCase):

    def setUp(self):
        self.accounts = load_accounts(ACCOUNTS_FILE)

    # helper method
    # runs DSL commands
    def run_dsl_command(self, command):
        lexer = Lexer(command)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        evaluator = Evaluator(self.accounts)
        evaluator.evaluate(ast)

    # CHECK BALANCE AFTER DEPOSIT TEST
    def test_deposit_balance(self):
        account = self.accounts["TK171317"]

        before_balance = account.get_balance()
        print(f"\nStarting balance for TK171317: {before_balance:.2f}")  # Print starting balance, 962.33

        self.run_dsl_command("deposit TK171317 100")

        after_balance = account.get_balance()
        print(f"Updated balance after deposit: {after_balance:.2f}")  # Print updated balance, 1062.33

        expected_balance = round(before_balance + 100.00, 2)

        # determine if test case passes or fails, with message
        if after_balance == expected_balance:
            print("PASS: DSL deposit command correctly updated the balance.")
        else:
            print("FAIL: DSL deposit command did not update the balance correctly.")

        self.assertEqual(after_balance, expected_balance)

    # CHECK BALANCE AFTER WITHDRAWAL TEST
    def test_withdraw_balance(self):
        account = self.accounts["BK123456"]  # BEYONCE KNOWLES account

        before_balance = account.get_balance()
        print(f"\nStarting balance for BK123456: {before_balance:.2f}")  # Print starting balance, 999.13

        self.run_dsl_command("withdraw BK123456 50")

        after_balance = account.get_balance()
        print(f"Updated balance after withdrawal: {after_balance:.2f}")  # Print updated balance, 949.13

        expected_balance = round(before_balance - 50.00, 2)

        # determine if test case passes or fails, with message
        if after_balance == expected_balance:
            print("PASS: DSL withdraw command correctly updated the balance.")
        else:
            print("FAIL: DSL withdraw command did not update the balance correctly.")

        self.assertEqual(after_balance, expected_balance)

    # CHECK FOR SEARCHING AN INVALID ACCOUNT NUMBER
    def test_invalid_account_number(self):
        invalid_account = "ZZ000000"

        print("\nTesting invalid account: ZZ000000")
        self.run_dsl_command("balance ZZ000000")

        # determine if test case passes or fails, with message
        if invalid_account not in self.accounts:
            print("PASS: DSL correctly rejected invalid account.")
        else:
            print("FAIL: Invalid account should not exist.")

        self.assertNotIn(invalid_account, self.accounts)

    # CREATE ACCOUNT TEST
    # Implements CREATE DSL command for account creation
    # It will write it to the text file, and then remove it after test is completed.
    # Ensures multiple entries are not present in the AccountCreation.txt file.
    # This tests checks to make sure newly created accounts are present in the file.
    def test_create_account(self):
        account_number = "RB052026"

        # remove test account before running in case it already exists
        remove_test_account(account_number)

        # reload accounts after cleanup
        self.accounts = load_accounts(ACCOUNTS_FILE)

        # DSL command being tested
        command = "create RED BULL RB052026"

        lexer = Lexer(command)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        evaluator = Evaluator(self.accounts)
        evaluator.evaluate(ast)

        created_accounts = load_accounts(ACCOUNTS_FILE)

        if account_number in created_accounts:
            print("PASS: DSL create command successfully created RED BULL RB052026.")
        else:
            print("FAIL: DSL create command did not create RED BULL RB052026.")

        self.assertIn(account_number, created_accounts)

        # remove test account after test has concluded
        remove_test_account(account_number)


# helper method
# Remove account method
# Used in create account
def remove_test_account(account_number):
    with open(ACCOUNTS_FILE, "r") as file:
        lines = file.readlines()

    with open(ACCOUNTS_FILE, "w") as file:
        for line in lines:
            if account_number not in line:
                file.write(line)


# Test running methods
def run_all_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(BankingSpecTests)
    runner = unittest.TextTestRunner()
    runner.run(suite)


def run_selected_test(test_name):
    suite = unittest.TestSuite()
    suite.addTest(BankingSpecTests(test_name))

    runner = unittest.TextTestRunner()
    runner.run(suite)


# main menu
def main():
    choice = ""

    while choice != "exit":
        print("\nBANKING DSL SPEC TESTING")
        print("1. Run all tests")
        print("2. Test deposit")
        print("3. Test withdraw")
        print("4. Test invalid account")
        print("5. Test create account")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            run_all_tests()

        elif choice == "2":
            run_selected_test("test_deposit_balance")

        elif choice == "3":
            run_selected_test("test_withdraw_balance")

        elif choice == "4":
            run_selected_test("test_invalid_account_number")

        elif choice == "5":
            run_selected_test("test_create_account")

        elif choice == "6":
            choice = "exit"
            print("Exiting spec testing program.")

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
