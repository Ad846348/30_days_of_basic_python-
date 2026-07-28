class ATM:
	def __init__ (self):
		try:
			f=open("Balance.txt","r")
			self.balance=int(f.read())
			print("Balance=",self.balance)
		except:
			self.balance=1000
	def save_balance(self):
		with open("Balance.txt","w") as f:
			f.write(str(self.balance))
			f.close()
	def debit(self):
		try:
			a=int(input("Enter the amount :"))
			if(a>self.balance):
				print("Insufficient Balance")
		    elif(a>1000):
			    print(f"only debit till1000")
		    else:
			    self.balance-=a
			    self.save_balance()
			    print(" RemainingBalance=",self.balance)
          except  ValueError:
             print("Error: Input only numbers")
	def check_
Balance(self):
		print("current Balance=",self.balance)
normal=ATM()
normal.check_Balance()
normal.debit()
normal.check_Balance()
