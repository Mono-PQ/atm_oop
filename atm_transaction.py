from abc import ABC, abstractmethod
from account import *
import datetime

class ATM_Transaction(ABC):
    '''Abstract class'''
    transaction_id = 0
    def __init__(self, timestamp, trans_type, amount=0):
        '''Constructor to initialise transaction timestamp, type and amount via input. Increment the transaction id by 1.'''
        self.timestamp = timestamp
        self._trans_type = trans_type
        self._amount = amount
        ATM_Transaction.transaction_id += 1
    @abstractmethod
    def update(self): 
        pass

class Withdrawal(ATM_Transaction): 
    def __init__(self, amount):
        '''Constructor to initialise the transaction timestamp as time of transaction and type as withdrawal. Amount 
        is assigned via input.'''
        super().__init__(datetime.datetime.now(), "withdrawal", amount)
    def withdraw(self, account): 
        '''Function to withdraw the amount from customer account'''
        return self.update(account, self._amount)
    def update(self, acc, amount, transferacc=None): 
        '''Function to update customer account with funds to be withdrawn'''
        return acc.debit(amount)
class Transfer(ATM_Transaction):
    def __init__(self, amount):
        '''Constructor to initialise the transaction timestamp, type, amount via input. Increment the transaction id by 1.'''
        super().__init__(datetime.datetime.now(), "transfer", amount) 
    def update(self, acc, amount, transferacc=None):
        '''Function to update the customer account with funds for the transfer'''
        self.transferacc = transferacc
        if acc.debit(amount):
            transferacc.credit(amount)
            return True
        else:
            return acc.debit(amount) 