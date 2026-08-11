import os

folder = input("Folder path: ")
prefix = input("New name: ")
ext_wanted = input("type of file? .jpg / .png / .pdf: ")

files = os.listdir(folder)
count = 1

for file in files:
    name, ext = os.path.splitext(file)
    
    if ext == ext_wanted: 
        new_name = f"{prefix}_{count}{ext}"
        os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
        count += 1

print(f"{count-1} files rename ho gayi ✅")
