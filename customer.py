import datetime
class Customer: 
    def __init__(self, name, address, dob):
        '''
        Constructor to initialises customer's name, address and date of birth.
        accounts_list is an empty list.
        '''
        self.__name = name
        self.__address = address
        self.__dob = datetime.datetime.strptime(dob, "%d-%b-%Y")
        self.__accounts_list = []
    def owns(self, Account):
        '''
        Function that accepts an Account object and add to the accounts_list
        '''
        self.__accounts_list.append(Account)
    def __str__(self):
        '''
        Returns string representation of the Customer object detailing name, address and dob 
        '''
        return "Customer Name: {} \nAddress: {} \nDate of Birth: {}".format(self.__name, self.__address, self.__dob)
    def get_name(self):
        '''Getter for private attribute: name'''
        return self.__name
    def get_accounts_list(self):
        '''Getter for private attribute: accounts_list'''
        return self.__accounts_list