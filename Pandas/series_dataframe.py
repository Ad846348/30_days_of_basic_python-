# Series

import pandas as pd
x=[1,2,3,4,5,6]
print(pd.Series(x))

#To change index

print(pd.Series(x,index=["a","b","c","d","e","f"]))

# Data frames

print(pd.DataFrame(x))
d= {"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]}
var=print(pd.DataFrame(d,columns=["a","d"]))


