from additional_exceptions import *
class Account:
    def __init__(self, type, owner):
        '''Constructor to initialises balance to 0'''
        self._type = type
        self.__owner = owner
        self.__balance = 0
    def get_type(self):
        '''Getter for private attribute: type'''
        return self._type
    def get_owner(self):
        '''Getter for private attribute: owner'''
        return self.__owner
    def check_balance(self):
        '''Function to check account balance and return current balance'''
        return self.__balance
    def set_balance(self, balance):
        '''Setter for private attribute: balance'''
        self.__balance = balance
    def debit(self, amount):
        '''
        Function that accepts an amount, check and subtract from balance. If balance is sufficient
        return True, else raise "InsufficientFunds" exception.
        '''
        status = False
        if self.__validate_amount(amount):
            amount = float(amount)
            if self.__balance >= amount:
                new_balance = self.check_balance() - amount
                self.set_balance(new_balance)
                status = True
        if status == True: 
            return True
        else: 
            raise InsufficientFunds("Insufficient funds in account.")
    def credit(self, amount):
        '''Function that accepts an amount, check and add to the balance'''
        if self.__validate_amount(amount):
            amount = float(amount)
            new_balance = self.check_balance() + amount
            self.set_balance(new_balance)
    def __validate_amount(self, amount):
        '''
        Function that accepts a monetary amount (int, float, string) and converts it to type float.
        Raise "ValueError" if monetary amount is <= 0 or more than 2 decimal places. Return True otherwise
        '''
        amount = float(amount)
        #To check if amount has more than 2 decimal places by spilt the integer and floating point.
        if "." in str(amount):
            dp = str(amount).split('.')
        else:
            dp = 0
        if (float(amount) <= 0 or len(dp[-1]) > 2):
            raise ValueError("Invalid amount.")
        else:
            return True

class Savings_Account(Account):
    def __init__(self, account_no, owner):
        '''Constructor to initialises account number and owner from input parameters'''
        super().__init__("savings", owner)
        self.__account_no = account_no        
    def get_account_no(self):
        '''Getter for private attribute: account_no'''
        return self.__account_no

class Current_Account(Account):
    def __init__(self, account_no, owner):
        '''Constructor to initialises account number and owner from input parameters'''
        super().__init__("current", owner)
        self.__account_no = account_no
    def get_account_no(self):
        '''Getter for private attribute: account_no'''
        return self.__account_no