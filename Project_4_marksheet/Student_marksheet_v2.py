print("***Student report card***")
student={}
student["name"]=input("Enter name ")
student["class"]= int(input("Enter class "))
marks = []
for i in range(1,6):
      m=int(input(f"Enter marks of subject {i} "))
      marks.append (m)
student["marks"]=marks
student["total"] =sum(marks)
print(student)
	
