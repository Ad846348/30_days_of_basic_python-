import pandas as pd


data = {
    'Name': ['Aman', 'Priya', 'Rahul', 'Sneha', None],
    'Math': [90, 85, None, 78, 92],
    'Science': [88, None, 75, 82, 95],
    'English': [92, 89, 80, None, 88]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
print("-"*40)


df['Total'] = df['Math'] + df['Science'] + df['English']
df['Average'] = df['Total'] / 3
print("Adding Total and Average:\n", df)
print("-"*40)


df.insert(1, 'RollNo', [101, 102, 103, 104, 105])
print("RollNo inserted:\n", df)
print("-"*40)


df = df.drop('English', axis=1) 
df = df.drop(4, axis=0) 
print("English column aur 5th row delete:\n", df)
print("-"*40)


print("Missing values before:\n", df.isnull().sum())


df_filled = df.fillna(0) 
print("\nfillna(0) ke baad:\n", df_filled)


df_clean = df.dropna() 
print("\ndropna ke baad:\n", df_clean)
print("-"*40)


df_clean.to_csv('clean_report.csv', index=False) 
print("Clean file save ho gayi: clean_report.csv")

df2 = pd.read_csv('clean_report.csv')
print("\nCSV se wapas padha:\n", df2)
