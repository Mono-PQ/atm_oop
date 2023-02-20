from customer import *
from account import *
from bank import *
from atm_card import *

c1 = Customer('John', '50 Sim Ming Lane', '25-JAN-1977')
a1 = Savings_Account('554-1112-1882', c1)
a2 = Current_Account('154-1120-3922', c1)
card1 = ATM_Card('444-1111-222', c1)

c2 = Customer('Peter', '21 Jurong East', '25-SEP-1977')
a3 = Savings_Account('154-0000-1993', c2)
card2 = ATM_Card('111-2222-333', c2)

c1.owns(a1)
c1.owns(a2)

c2.owns(a3)

a1.set_balance(2000)
a2.set_balance(1000)
a3.set_balance(200)

b = Bank("B001", "10 Sim Ming Lane")
b.add_customer(c1, "1234")
b.add_customer(c2, "0000")

print(card1.get_acct_types())
print(card2.get_acct_types())
# print(card1.get_owner().get_accounts_list())
acc1 = card1.access('current')
acc2 = card2.access('savings')
print(acc1.check_balance())
print(acc2.check_balance())
print(card1)
print(card2)
print(card1.get_atmcardnum())
print(card1.get_owner())

b.manages(card1)
b.manages(card2)

print(b.list_atmcards)