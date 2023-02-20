from customer import *
from account import *

c1 = Customer('John', '50 Sim Ming Lane', '25-JAN-1977')
a1 = Savings_Account('554-1112-1882', c1)
a2 = Current_Account('154-1120-3922', c1)

c1.owns(a1)
c1.owns(a2)

# print(a1.get_type())
# print(a1.get_owner())
# for element in dir(a1):
#     if not element.startswith("__"):
#         print('{} is {}'.format(element, type(getattr(a1, element))))
# print(a1.check_balance())
# print(a1.set_balance(300))
# print(a1.check_balance())
# print(a1.credit(300))
# print(a1.check_balance())
# print(a1.debit(200))
# print(a1.check_balance())

print(a2.get_type())
print(a2.get_owner())
print(a2.check_balance())
print(a2.set_balance(300))
print(a2.check_balance())
print(a2.credit(300))
print(a2.check_balance())
print(a2.debit(200))
print(a2.check_balance())
#print(a2.credit("-45"))
#print(a2.credit("20.8825151"))
print(a2.debit(1000))
print(a2.check_balance())