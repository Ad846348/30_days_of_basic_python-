class ATM:
			def __init__ (self):
				self.balance=1000
			def check_balance(self):
			     print("Balance=",self.balance)
			def debit(self):
			     		a=int(input("Enter the amount : "))
			     		if(a<1000):
			     			print("only debit money till 1000")
			     		elif(a>1000):
			     		   print("Insufficient Balance")
			     		else:
			     				self.balance-=a
			     				print("Remaining Balance=",self.balance)
			     				def credit(self):
			     					a=int(input("Enter the amount : "))
			     					self.balance+=a
			     					print("Balance=", self.balance)
class Super_ATM(ATM):
	def __init__ (self):
		super().__init__()
		self.balance=5000
		def debit(self):
		  	a=int(input("Enter the amount :"))
		  	if(a<5000):
		  		print("only debit money till 5000")
		  	elif(a>5000):
		  			print("Insufficient balance")
		  	else:
		  			print("Remaining=",self.balance-a)
		  			def deposit_bonus(self):
		  				self.balance+=100
		  				print(f"Rs{a}+100 deposited")
		  				print("New balance=",self.balance)
print("Normal ATM")
normal=ATM()
normal.debit()

print("Premium ATM")
premium=Super_ATM()
premium.debit()
