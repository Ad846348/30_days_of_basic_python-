def add(a,b):
	return (a+b)
def sub(a,b):
	return(a-b)
def prod(a,b):
	return(a*b)
def div(a,b):
	return(a/b)
print("""Main Menu
1. Addition
2.Subtraction
3.Multiplication
4.Division""")
c=int(input("Enter choice : "))
n1=int(input("Enter the number : "))
n2=int(input("Enter the number : "))
if (c==1):
	print(add(n1,n2))
elif(c==2):
	print(sub(n1,n2))
elif(c==3):
	print(prod(n1,n2))
elif(c==4):
	print(div(n1,n2))
else:
	print("Invalid")
