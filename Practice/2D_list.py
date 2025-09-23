student_info= []
for i in range(3):
    student=[] #this line will be in here bec we want to keep it's as a fresh start to get new student information
    student.append(input("Enter the name:"))
    student.append(input("Enter the age:"))
    student.append(input("Enter the major:"))
    student.append(input("Enter the nationality:"))
    student_info.append(student)
print(student_info)

for student in student_info:
    for i in student:
        print(i)
