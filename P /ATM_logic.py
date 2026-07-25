class ATM:
	def __init__ (self):
		try:
			f=open("Balance.txt","r")
			self.balance=int(f.read())
			print("Balance=",self.balance)
		except:
			self.balance=1000
			print("Balance=",self.balance)
	def save_balance(self):
		with open ("Balance.txt","w") as f:
			f.write(str(self.balance))
	def debit(self,a):
			try:
				a=int(a)
				if(a<=0):
					print("Enter amount greater than zero")
				elif(a>self.balance):
						print("Insufficient Balance")
				else:
					self.balance-=a
					self.save_balance()
			except ValueError :
				print("input only positive numbers")
	def check_balance(self):
			print("Current Balance=",self.balance)
