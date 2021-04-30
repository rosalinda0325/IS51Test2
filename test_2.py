"""

This program will display the number of grades, the average grade and the percentage of grades that are above above average grade.
The first calculation will display the number of grades. The second calculation will display the average grade.
The third calculation will display the percentage of grades above average.


function1 will initiate the application
function2 will add all of the grades/numbers of grades
function3 will 100* n/ len (grades)


After the code runs it qill output the number of grades, the average grade and the percentage of grades that are above the average grade.
"""

"""
#initiate
open final.txt


#function1
grade = int(grade)

#function2
average = sum (grades)/ len (grades)
num=0

#function3
if grade > average
num +=1

print ("  ")

"""


infile = open( "Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()

for i in range(len(grades)):
    grades [i] = int (grades[i])

average = sum(grades) / len(grades)
num = 0

for grade in grades:
    if grade > average:
        num +=1

print("Number of grades:" , len(grades))
print("Average grade:", average)
print("Percentage of grades above average grade: {0:.2f}%".format(100 * num / len(grades)))
