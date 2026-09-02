import pandas as pd
import matplotlib.pyplot as plt


var=pd.DataFrame({"X":["C","C++","Java","Python"],"Y":[10,20,30,40]})
var.to_csv("Language.csv", index=False)

df = pd.read_csv("Language.csv")

fig, ax = plt.subplots(figsize=(8,5))
markerline, stemlines, baseline = ax.stem(df['X'], df['Y'], basefmt=" ")


plt.setp(markerline, color='#E74C3C', markersize=10, markeredgecolor='black')
plt.setp(stemlines, color='#3498DB', linewidth=2, linestyle='--')

ax.set_title('Programming Languages Popularity - Stem Plot', fontsize=14, fontweight='bold')
ax.set_xlabel('Language')
ax.set_ylabel('Popularity Score')
ax.grid(True, alpha=0.3)


for i, v in enumerate(df['Y']):
    ax.text(i, v+1, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('language_stem_plot.png', dpi=300)
plt.show()