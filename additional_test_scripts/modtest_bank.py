from customer import *
from account import *
from bank import *

c1 = Customer('John', '50 Sim Ming Lane', '25-JAN-1977')
a1 = Savings_Account('554-1112-1882', c1)
a2 = Current_Account('154-1120-3922', c1)

c2 = Customer('Peter', '21 Jurong East', '25-SEP-1977')
a3 = Savings_Account('154-0000-1993', c2)

c1.owns(a1)
c1.owns(a2)

c2.owns(a3)

a1.set_balance(2000)
a2.set_balance(1000)
a3.set_balance(200)

b = Bank("B001", "10 Sim Ming Lane")
b.add_customer(c1, "1234")
b.add_customer(c2, "0000")
print(b.list_customer)

print(b.authorize_pin(c2, "0000"))
acc = b.get_acct('154-1120-3922')
print(acc)
print(acc.check_balance())

acc2 = b.get_acct('154-0000-1993')
print(acc2)
print(acc2.check_balance())