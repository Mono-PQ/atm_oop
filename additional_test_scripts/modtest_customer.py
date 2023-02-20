from customer import *
from account import *

c1 = Customer('John', '50 Sim Ming Lane', '25-JAN-1977')
a1 = Savings_Account('554-1112-1882', c1)

c1.owns(a1)

print(c1)
print(c1.get_name())
print(c1.get_accounts_list())

