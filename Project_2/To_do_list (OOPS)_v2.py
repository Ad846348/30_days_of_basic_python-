class To_do_List :
	def __init__ (self):
		self.tasks=[]
	def show(self):
	  if not self.tasks:
	  	print("No tasks")
	  else:
	  	for i,task in enumerate(self.task,1):
	  		print(f"{i}.{tasks}")
	def  add(self):
	  	a=input("Enter the task: ")
	  	self.tasks.append(a)
	  	print(self.tasks)
def delete(self):
   	b=int(input("Enter the no. to delete: "))
   	for i in range(len(self.tasks),1):
   		if (b==i):
   			tasks.pop(b-1)
   		else:
   				print("Invalid")
to_do=To_do_List ()
while True:
   	print("""Main menu
   	1.Show task
   	2.Add task
   	3.Delete task""")
   	c=int(input("Enter choices from(1,3):  "))
   	if (c==1):
   		to_do.show()
   	elif(c==2):
   		to_do.add()
   	elif(c==3):
   		to_do.delete()
   	else:
   		print("invalid")
