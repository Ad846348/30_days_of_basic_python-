import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Products.csv")
print(df["NIRF_Ranking"].describe()) 


plt.hist(df["NIRF_Ranking"], bins=10, color='skyblue', edgecolor='black')
plt.title('NIRF Ranking Distribution', fontsize=16)
plt.xlabel('NIRF Ranking')
plt.ylabel('Frequency (Kitne IITs)')
plt.savefig('07_nirf_hist.png')
plt.show()


plt.hist(df["Priority"], bins=5, color='orange', edgecolor='black', rwidth=0.8)
plt.title('Priority Distribution')
plt.xlabel('Priority (1-5)')
plt.ylabel('Count')
plt.savefig('08_priority_hist.png')
plt.show()

print("Histogram ban gaya")