import numpy as np

print("=== Bill Calculator ===")
price = np.array([10, 20, 30])
qty = np.array([2, 3, 4])     

item_total = price * qty
bill_total = np.sum(item_total)

print("Price:", price)
print("Quantity:", qty)
print("Item wise total:", item_total)
print("Grand Total Bill: Rs.", bill_total)
