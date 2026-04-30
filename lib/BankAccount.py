# BANK ACCOUNT CLASS
# IBRAHIM ALI
# 04/29/2026
# Final Project
#DESCRIPTION: Defines the bank account varibales and has getters and setters to access the variables


class BankAccount:
    def __init__(self, first_name, last_name, account_number, balance):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = account_number
        self.__balance = balance

    # Getters for the variables

    # Returns the first name
    def get_first_name(self):
        return self.__first_name

    # Returns the last name
    def get_last_name(self):
        return self.__last_name

    # Returns the account number
    def get_account_number(self):
        return self.__account_number

    # Returns the current balance
    def get_balance(self):
        return self.__balance

    # Setters for the variables

    def set_first_name(self, name):
        self.__first_name = name

    def set_last_name(self, name):
        self.__last_name = name

    def set_account_number(self, acc):
        self.__account_number = acc

    def set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount
        self.__balance = round(self.__balance, 2)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__balance = round(self.__balance, 2)
            return True
        return False
