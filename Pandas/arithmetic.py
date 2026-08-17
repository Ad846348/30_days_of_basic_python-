import pandas as pd
var=pd.DataFrame( {"A":[1,2,3,4],"B":[5,6,7,8]})
print(var)
var["C"]=var["A"]+var["B"]

var["D"]=var["A"]-var["B"]

var["E"]=var["A"]*var["B"]
print(var)