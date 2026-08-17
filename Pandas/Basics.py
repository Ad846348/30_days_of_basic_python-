import pandas as pd

data = {
    'Name': ['Amit', 'Ravi', 'Priya', 'Sneha'],
    'Marks': [90, 75, 88, 95],
    'City': ['Patna', 'Delhi', 'Mumbai', 'Patna']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("\nShape:", df.shape) 
print("Columns:", df.columns)
print("\nData Types:\n", df.dtypes)
