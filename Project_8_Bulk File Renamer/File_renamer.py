import os

folder_path = input("Enter Path of folder: ") 
prefix = input("Entry new name:")  

files = os.listdir(folder_path)
count = 1

for file in files:
  
    name, ext = os.path.splitext(file)
    
    
    new_name = f"{prefix}_{count}{ext}"
    
    
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
    count += 1

print("Saare files rename ho gaye ✅")
