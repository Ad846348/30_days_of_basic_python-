from ATM_logic import ATM
atm=ATM()
a=int(input("Enter amount "))
print (atm.check_balance())
print(atm.debit(a))
print (atm.check_balance())
