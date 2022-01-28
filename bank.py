import random
from customer import * 
from account import * 
from additional_exceptions import *

class Bank:
    def __init__(self, code, address):
        '''Constructor to initialise the bank's code and address from input and initialise all lists as empty lists'''
        self.__code = code
        self.__address = address 
        self.list_atm = []
        self.list_customer = []
        self.list_atmcards = []
    def add_customer(self, customer, pin):
        '''Function to add a Customer object and their pin number in Customer record (dict format) to  list_customer'''
        d = {}
        rand_id_digits = str(random.randrange(1000, 9999))
        d['customer_id'] = customer.get_name() + rand_id_digits
        d['customer_obj'] = customer
        d['customer_pin'] = pin
        self.list_customer.append(d)
    def manages(self, atm_card): 
        '''Function to add atm_card object and stores in list_atmcards'''
        self.list_atmcards.append(atm_card)
    def maintains(self, atm): 
        '''Function to add atm object to list_atm'''
        self.list_atm.append(atm)
    def authorize_pin(self, customer, pin):
        '''Function to check if the customer's pin is valid with customer's object and pin as inputs''' 
        for c in self.list_customer:
            if (c['customer_id'][:-4] == customer.get_name()):
                if (c['customer_pin'] == pin): 
                    pin_status = True
                    break
                else: 
                    pin_status = False
        if pin_status == True:
            return True
        else: 
            raise InvalidPinNumber("Invalid pin.")
    def get_acct(self, acctnum): 
        '''Function accepts account number and check if account number is valid. Return Account object if valid, else raise AccountNotFound exception'''
        status = False
        for record in self.list_customer:
            for acc in record['customer_obj'].get_accounts_list(): 
                if acc.get_account_no() == acctnum: 
                    status = True
                    acc_found = acc 
                    break
        if status == True:
            return acc_found
        else: 
            raise AccountNotFound("Account is not found.")