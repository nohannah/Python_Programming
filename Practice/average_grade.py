average_class=[]
total_grade=0
studentsGrades = [['John', "9", "10", "7"],
                  ['Marry', "9", "8", "8"],
                  ['Smith', "8", "8", "8"],
                  ['Adam', "6", "4", "7"]
                ]
for student in (studentsGrades):
    avg_each=0
    for i in student[1:]:
        avg_each+=int(i)
        student_avg=avg_each/len(student[1:])      
    print("average grade for each student:",student_avg)
    average_class.append(student_avg)
#total of the average class
total_grade=sum(average_class)
total=total_grade/len(average_class)
print("the whole class average:",total)
        
        
