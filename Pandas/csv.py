import pandas as pd
var=pd.DataFrame({"Products":["Laptop","Mouse","Keyboard"], "Price":[50000,5000,3000], "sold":[10,20,5]})
print(var)
var.to_csv("Text_new.csv",index=False)
a=pd.read_csv("Text_new.csv")
print(a.to_string(index=False))
