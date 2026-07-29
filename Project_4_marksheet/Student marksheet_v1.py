print(""" Student marksheet""")
name=(input("Enter name "))
marks=[]
for i in range(1,6):
	  m=int(input(f"Enter marksofsubject {i} " ))
	  marks.append(m)
	  Marks=sum(marks)
total=Marks
per=(total/500)*100
print("Name =",name)
print("Marks secured",total,"/500")
print("percentage",per,"%")
if(per>=95):
	print("GradeA")
elif(per>=90):
	print("GradeB")
elif(per>=80):
	print("GradeC")
elif(per<=60):
  print("Fail")
