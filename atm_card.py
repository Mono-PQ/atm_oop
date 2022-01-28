from customer import *
from account import *

class ATM_Card:
    def __init__(self, atmcardnum, owner):
        '''Constructor to initialise ATM card number and owner via input'''
        self.__atmcardnum = atmcardnum
        self.__owner = owner
    def get_acct_types(self): 
        '''Function to get the list of account types available for the customer'''
        list_acctype = []
        for acc in self.__owner.get_accounts_list(): 
            list_acctype.append(acc.get_type())
        return list_acctype
    def access(self, acctype): 
        '''Function to return an Account object based on the selected account type'''
        for acc in self.__owner.get_accounts_list():
            if acc.get_type() == acctype:
                acc_obj = acc
        return acc_obj        
    def __str__(self): 
        '''Function that retuns string representation of the ATM card details: card number and owner name'''
        return f"Card Number: {self.__atmcardnum} \nName: {self.__owner.get_name()}"
    def get_atmcardnum(self): 
        '''Getter for private attribute: atmcardnum'''
        return self.__atmcardnum
    def get_owner(self):
        '''Getter for private attribute: owner'''
        return self.__owner