from customer import *
from account import *
from bank import *
from atm_card import *
from atm_transaction import *
from atm import *

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

acc1 = card1.access('current')
acc2 = card2.access('savings')

b.manages(card1)
b.manages(card2)

atm = ATM("Jurong", b)
b.maintains(atm)

atm.set_currentcard(card1)
card = atm.get_currentcard()
print(card)

print(atm.transactions('withdrawal', 550.32, 'savings'))
print(atm.show_balance('savings'))


print(atm.transactions('transfer', 20.57, 'current', '554-1112-1882'))
print(atm.show_balance('current'))

print(atm.check_accts())
print(atm.check_card('444-1111-222'))
print(atm.check_pin('1234'))