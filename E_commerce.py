np.random.seed(42) 

products = ['Laptop', 'Mobile', 'Headphone', 'Keyboard', 'Mouse']
cities = ['Patna', 'Delhi', 'Mumbai', 'Bangalore']

data = {
    'OrderID': np.arange(101, 201), 
    'Product': np.random.choice(products, 100),
    'City': np.random.choice(cities, 100),
    'Price': np.random.randint(500, 50000, 100), 
    'Sold': np.random.randint(1, 20, 100),
    'Rating': np.round(np.random.uniform(2.0, 5.0, 100), 1) 
}

df = pd.DataFrame(data)


df['Revenue'] = df['Price'] * df['Sold'] 
df['Discount'] = np.where(df['Revenue'] > 100000, 10, 5) 
df['Final_Revenue'] = df['Revenue'] - (df['Revenue'] * df['Discount'] / 100)

print("First 5 rows:\n", df.head())
print("-"*50)

print("1. Total Revenue:", np.sum(df['Final_Revenue']))
print("2. Average Rating:", np.mean(df['Rating'])) 


top_product = df.groupby('Product')['Sold'].sum().idxmax()
print("3. Top Selling Product:", top_product)


city_rev = df.groupby('City')['Final_Revenue'].sum().sort_values(ascending=False)
print("4. City wise Revenue:\n", city_rev)


print("\nMissing values:", df.isnull().sum().sum()) 
df = df.drop_duplicates()


df.to_csv('sales_data_final.csv', index=False)
print("\nFile save ho gayi: sales_data_final.csv")
