import numpy as np
marks=np.array([
    [90, 85, 78],  # Amit
    [75, 80, 85],  # Ravi  
    [88, 92, 90],  # Priya
    [95, 89, 91],  # Sneha
    [60, 70, 65]   # Rohan
])

print("Marks Matrix:\n", marks)
print()

total = marks.sum(axis=1) 
print("Total Marks:", total)


avg_subject = marks.mean(axis=0) 
print("Subject Average:", avg_subject)


toughest = np.argmin(avg_subject)
print("Toughest Subject Index:", toughest) 
high_marks = marks[marks > 80]
print("80+ wale marks:", high_marks)
print("Count:", high_marks.size)
