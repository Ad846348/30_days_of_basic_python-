import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Language.csv")

a=df['Y']
priority_count = df['X']
print(priority_count)
colors = ["#F08080","#90EE90","#87CEEB","#00FFFF"]
explode = [0, 0, 0, 0.1] 

plt.pie(a,labels=priority_count,autopct='%1.1f%%',colors=colors,explode=explode, startangle=40,textprops={"fontsize":15},wedgeprops={"linewidth":2})

plt.title('Language vs Popularity (Pro)', fontsize=20)
plt.tight_layout()
plt.show()