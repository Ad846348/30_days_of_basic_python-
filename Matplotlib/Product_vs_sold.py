import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales_data_final.csv')

city_revenue = df.groupby('City')['Final_Revenue'].sum()
print(city_revenue)
print("-"*40)

c=["Red","Blue","Yellow","Green"]
city_revenue.plot(kind='bar', color=c)

plt.title('City vs Total Revenue', fontsize=14, fontweight='bold')
plt.xlabel('City')
plt.ylabel('Revenue (Rs)')
plt.xticks(rotation=0) 

plt.savefig('01_city_revenue_bar.png')
plt.show()

print("Graph ban gaya: 01_city_revenue_bar.png")
