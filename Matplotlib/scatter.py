import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Products.csv")
print(df[["IITS","NIRF_Ranking","Priority"]].head())
colors=[10,20,30,40,50]
sizes=[900,800,700,600,500]
plt.scatter(df["Priority"],df["NIRF_Ranking"],s=sizes,c=colors,cmap="viridis",alpha=0.5)
plt.title(" Priority vs NIRF Ranking",fontsize=16)
plt.xlabel("Priority",fontsize=20)
plt.ylabel("NIRF Ranking",fontsize=20)
plt.colorbar(label="color bar")
plt.tight_layout()
plt.savefig("nirf.png")
plt.show()


