from atm_transaction import Withdrawal, Transfer
from additional_exceptions import *

class ATM(): 
    def __init__(self, location, managed_by):
        '''Constructor to initialise the ATM location and managed by via input'''
        self.location = location 
        self.managed_by = managed_by
        self.__current_card = None
    def get_currentcard(self):
        '''Getter for private attribute: current_card'''
        return self.__current_card
    def set_currentcard(self, current_card): 
        '''Setter for private attribute: current_card'''
        self.__current_card = current_card
    def transactions(self, trans_type, amount, acct_type, acct_num=None): 
        '''Function to process the requested transaction type'''
        if trans_type == "withdrawal":
            w = Withdrawal(amount)
            return w.update(self.__current_card.access(acct_type), amount)
        if trans_type == "transfer":
            t = Transfer(amount)
            acc_no = self.__current_card.access(acct_type).get_account_no()
            if acc_no != acct_num:
                transacc = self.managed_by.get_acct(acct_num)
                return t.update(self.__current_card.access(acct_type), amount, transacc)
            else:
                raise InvalidAccount("Account is not found.")
    def check_accts(self):
        '''Function that checks if user has 1 or 2 account''' 
        lis_acctypes = self.__current_card.get_acct_types()
        if len(lis_acctypes) == 2: 
            return True
        else:
            return False
    def check_pin(self, pin):
        '''Function that accepts user pin and check with bank if the pin is valid.'''
        return self.managed_by.authorize_pin(self.__current_card.get_owner(), pin)
    def check_card(self, atmcardnum): 
        '''Function that accepts ATM card number and check with bank if the card is valid'''
        status = False
        for card in self.managed_by.list_atmcards:
            if card.get_atmcardnum() == atmcardnum:
                self.set_currentcard(card)
                status = True
        if status == True:
            return True
        else:
            raise InvalidATMCard("ATM card is not found.")
    def show_balance(self, acctype): 
        acct = self.__current_card.access(acctype)
        return f"Your {acctype} account has a balance of ${acct.check_balance():.2f}."   