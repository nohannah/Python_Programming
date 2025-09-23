studentsGrade1 = ['John', 9, 10, 7]
studentsGrade2 = ['Marry', 9, 8, 8]
studentsGrade3 = ['Smith', 8, 8, 8]
studentsGrade4 = ['Adam', 6, 4, 7]

# studentsGrade1.remove('John')
# studentsGrade2.remove('Marry')
# studentsGrade3.remove('Smith')
# studentsGrade4.remove('Adam')

# int(studentsGrade1)
# int(studentsGrade2)
# int(studentsGrade3)
# int(studentsGrade4)
sum_john = sum(studentsGrade1[1:])
sum_marry=sum(studentsGrade2[1:])
sum_smith=sum(studentsGrade3[1:])
sum_adam=sum(studentsGrade4[1:])

average1=sum_john/(len(studentsGrade1)-1)
average2=sum_marry/(len(studentsGrade2)-1)
average3=sum_smith/(len(studentsGrade3)-1)
average4=sum_adam/(len(studentsGrade4)-1)

total_average=(average1+average2+average3+average4)/4
print('Average of john is',average1)
print('Average of marry is',average2)
print('Average of smith is',average3)
print('Average of adam is',average4)
print("Total average of these students:",total_average)

# # all_student=[studentsGrade1,studentsGrade2,studentsGrade3,studentsGrade4]

# studentsGrade1 = ['John', 9, 10, 7]
# studentsGrade2 = ['Marry', 9, 8, 8]
# studentsGrade3 = ['Smith', 8, 8, 8]
# studentsGrade4 = ['Adam', 6, 4, 7]

# # Calculate the sum of grades for John
# sum_grades = sum(studentsGrade1[1:])

# # Calculate the average grade for John
# average1 = sum_grades / (len(studentsGrade1) - 1)

# print(average1)
# ## it's will give the same output because it's change in the same location in list1 
# mylist=['john','alax','mary']
# mylist2=mylist 
# mylist2[0]= 'petter'
# print(mylist)
# print(mylist2)
# ## how to add petter in list2 by not effect to lsit1
# mylist=['john','alax','mary']
# mylist2=["" ]+ mylist 
# mylist2[0]= 'petter'
# print(mylist)
# print(mylist2)

mystring="I love python class"
print(mystring.split())

# mylist=["i",'lobe','you']
# print('and'.join(mylist))

# #normal input
# name1=(input("Enter the name "))
# name2=(input("Enter the name "))
# name3=(input("Enter the name ")) 
# myclass=[name1,name2,name3]
# print(myclass)
# #append method
# myclass=[]
# myclass.append(name1) 
# myclass.append(name2)
# myclass.append(name3)
# print(myclass)
# #split
# name=input("enter three name").split()
# print(name)