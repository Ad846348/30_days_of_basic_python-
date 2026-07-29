def calc():
    print("SMART CALCULATOR")
    while True:
        print( """ 1. Addition
2.Subtraction
3.Multiplication
4.Floor Division
5.Division
6.Modulus
7.Exponential
8.Table of a and b
9.Exit""")      
        a=int(input("enter the number "))
        b=int(input("enter the number "))
        i=int(input("enter choice "))
        if(i==1):
            print("sum=",a+b)
        elif(i==2):
            print("difference=",a-b)
        elif(i==3):
            print("product=",a*b)
        elif(i==4):
            print("quotient=",a//b)
        elif(i==5):
            print("quotient=",a/b)
        elif(i==6):
            print("remainder",a%b)
        elif(i==7):
            print("exponential=",a**b)
        elif(i==8):
        for j in range(1,11):
            print("table of a=",a*j)
            print("table of b=",b*j)
        elif (i==9):
            print("Exit")
            break 
        else:
          print("invalid")
calc()

          
                                
                                
        
