import pandas as pd
import numpy as np
var=pd.DataFrame({"Product":["Car","Laptop","Speaker","Monitor","Keyboard"],"Price":[300000,50000,10000,25000,None],"Discount":[50,10,5,20,5]})
print("Original data:",var)
print("_"*50)
a=(var["Price"]*var["Discount"])/100
var["Final_Price"]=var["Price"]-a
print("Previous data:",var)
print("_"*50)
var=var.fillna(0)
print("After fillna:",var)
print("_"*50)
a=(var["Price"]*var["Discount"])/100
var["Final_Price"]=var["Price"]-a
print("Final data:",var)
print("_"*50)
var.to_csv("Products.csv")


