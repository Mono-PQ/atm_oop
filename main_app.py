from atm import *
from additional_exceptions import *

class bcolors: 
    WARNING = '\033[93m'
    OFF = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def acc_selection(): 
    '''
    Function for account selection if user have two accounts.
    Used in the following menu options under atm_menu_sys function:
    '''
    print("Choose Account: \n1. Current Account \n2. Savings Account")
    acc = input("Enter an account option: ")  
    if acc == "1": 
        acctype = "current"
        success = True
    elif acc == "2": 
        acctype = "savings"
        success = True
    else:
        acctype = None 
        success = False
        print(f"{bcolors.BOLD}Error: Invalid option. Returned to ATM menu.{bcolors.ENDC}\n")
    return acctype, success 

def atm_app(ATM): 
    while True:
        print("Availble options: \n1. Insert ATM card \n2. Quit Simulation")
        option = input("Enter an option: ")
        if option == "2":
            '''Menu option 2: to quit stimulation menu'''
            print(f"{bcolors.OFF}System terminated{bcolors.ENDC}")
            break
        elif option == "1":
            '''Menu option 1: to insert ATM card'''
            card = input("Enter a ATM card number: ")
            try:
                '''Verify if card is valid'''
                status = ATM.check_card(card)
                if status == True:
                    pin = input("Enter a pin number: ")
                    ATM.check_pin(pin)
                    print()
                    atm_menu_sys(ATM)
            except InvalidATMCard:
                print(f"{bcolors.WARNING}Unsuccessful: Invalid ATM Card. Please take your card.{bcolors.ENDC}\n")
            except InvalidPinNumber:
                print(f"{bcolors.WARNING}Unsuccessful: Invalid Pin Number. Please take your card.{bcolors.ENDC}\n")
        else: 
            print(f"{bcolors.BOLD}Error: Invalid option. Please try again.{bcolors.ENDC}\n")

def atm_menu_sys(ATM):
    while True:
        print("Available options: \n1. Check balance \n2. Withdraw Funds \n3. Transfer Funds \n4. Return Card")
        option = input("Enter a transaction option: ")
        if option == "4":
            '''Menu option 4: Return to previous stimulation menu'''
            print(f"{bcolors.GREEN}Card Returned!{bcolors.ENDC}\n")
            ATM.set_currentcard(None)
            break
        elif option == "1":
            '''Menu option 1: For user to check balance.'''
            success = False
            if ATM.check_accts():
                '''Prompt user to select account if user has two accounts.'''
                acctype, success = acc_selection()
            else:
                acctype = "savings"
                success = True
            if success == True:
                print(f"{bcolors.BLUE}{ATM.show_balance(acctype)}{bcolors.ENDC}\n")
            else: 
                pass
        elif option == "2":
            '''Menu option 2: for user to withdraw money'''
            success = False
            trans_type_selected = False
            n = 1
            trans_type = "withdrawal"
            acctype = "savings"
            if ATM.check_accts():
                    acctype, trans_type_selected = acc_selection()
            else:
                acctype = "savings"
                trans_type_selected = True
            if trans_type_selected == True: 
                while n < 4: 
                    amt = input("Enter an amount to withdraw: ")
                    try: 
                        if ATM.transactions(trans_type, amt, acctype):
                            print(f"{bcolors.GREEN}Card Returned!{bcolors.ENDC}")
                            print(f"{bcolors.BLUE}{ATM.show_balance(acctype)}{bcolors.ENDC}\n")
                            ATM.set_currentcard(None)
                            success = True
                            break 
                    except InsufficientFunds:
                        print(f"{bcolors.WARNING}Unsuccessful: Insufficient funds available for transaction.{bcolors.ENDC}\n")
                        break
                    except ValueError: 
                        print(f"{bcolors.WARNING}Warning: Invalid amount for the transaction. Please enter a positive amount with maximum of 2 decimal places.{bcolors.ENDC}")
                    finally: 
                        n += 1
                if success != True and n > 3:
                    print(f"{bcolors.BOLD}Error: You have reached the maximum number of attempts.{bcolors.ENDC}\n") 
                if success == True:
                    break
            else: 
                pass 
        elif option == "3":
            '''Menu option 3: for user to transfer money to another account'''
            success = False
            trans_type_selected = False
            n = 1
            trans_type = "transfer"
            if ATM.check_accts():
                    acctype, trans_type_selected = acc_selection()
            else:
                acctype = "savings"
                trans_type_selected = True
            if trans_type_selected == True: 
                transacc = input("Enter the account number to transfer funds to: ")
                while n < 4: 
                    amt = input("Enter an amount to transfer: ") 
                    try: 
                        if ATM.transactions(trans_type, amt, acctype, transacc): 
                            print(f"{bcolors.GREEN}Card Returned!{bcolors.ENDC}")
                            print(f"{bcolors.BLUE}{ATM.show_balance(acctype)}{bcolors.ENDC}\n")
                            ATM.set_currentcard(None)
                            success = True
                            break
                    except InsufficientFunds:
                        print(f"{bcolors.WARNING}Unsuccessful: Insufficient funds available for transaction.{bcolors.ENDC}\n")
                        break
                    except InvalidAccount: 
                        print(f"{bcolors.WARNING}Unsuccessful: Invalid account for the transfer.{bcolors.ENDC}\n")
                        break
                    except ValueError: 
                        print(f"{bcolors.WARNING}Warning: Invalid amount for the transaction. Please enter a positive amount with maximum of 2 decimal places.{bcolors.ENDC}")
                    except AccountNotFound: 
                        print(f"{bcolors.WARNING}Unsuccessful: Account is not found in the system.{bcolors.ENDC}\n")
                        break
                    finally:
                        n += 1
                if success != True and n > 3:
                        print(f"{bcolors.BOLD}Error: You have reached the maximum number of attempts.{bcolors.ENDC}\n")
                if success == True: 
                    break
            else: 
                pass
        else: 
            print(f"{bcolors.BOLD}Error: Invalid option. Please try again.{bcolors.ENDC}\n")