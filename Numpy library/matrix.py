# Resize,flatten
import numpy as np
var2=np.array([1,2,3,4,5,6,5,4,3,2,1])
y=np.resize(var2,(3,2))
print(y)
print("-"*5)
print(y.flatten(order="F"))
print("-"*5)

# Insert

v=np.insert(var2,2,20)
print(v)
print("-"*5)

#Unique

x=np.unique(var2)
print(x)
print("-"*5)

#Matrix and its functions

var=np.matrix([[1,2,3],[4,5,6]])
var1=np.matrix([[1,2,3],[4,5,6]])
p=np.multiply(var,var1)
print(p)
print("-"*5)

print(np.transpose(var))
print("-"*5)



