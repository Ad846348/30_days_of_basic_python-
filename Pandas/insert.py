#Insert
import pandas as pd
var=pd.DataFrame({"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]})
print(var)
print("-"*10)
var.insert(1,"Python",var["A"])
print(var)
print("-"*10)
var["Python_12"]=var["A"][:1]
print(var)
print("*"*10)

#Delete
var1=var.pop("B")
print(var1)
print("*"*10)
print(var)
