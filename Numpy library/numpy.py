# To convert list into array and check its dimensions:-

import numpy as np
a=np.array([1,2,3,4])
print (a)
print()
print(a.ndim)
print()

# To create n dimensional array

import numpy as np
b=np.array([1,2,3,4],ndmin=10)
print(b)
print()

# To create zeros array

import numpy as np
b=np.zeros(4)
print(b)
print()

# To create ones array

import numpy as np
c=np.ones((3,5))
print(c)
print()

# To create empty array

import numpy as np
c=np.empty(4)
print(c)
print()

# To create range of array

import numpy as np
ar_rn=np.arange(4)
print(ar_rn)
print()

# To create diagonal array

import numpy as np
ar_d=np.eye(2)
print(ar_d)
print()

# To create line space array

import numpy as np
ar_lin = np.linspace(0,10,5)
print(ar_lin)
print()
