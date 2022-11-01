# cti 110
# p4hw1 - Grade List
# Smith Teyon
# 11/1

# ask user for 6 grades for the 6 modules
# add them to a list

grades = [100, 95, 88, 90, 93, 85]
grades = []
#grade1 = int(input('enter grade for module 1:'))
#grades [0] = grade1

for grade in range(6):
    grade = int(input('enter grade: '))
    grades.append(grade)
                  

print(grades)
#max(grades) and min (grades)
# to show lowest and highest in the list

print('The grades are: ', grades)
# max(grades) and min (grades)
# to show lowest and highest  in the list
print('Highest grade: ', max(grades))
print('Lowest grade: ', min(grades))

#now the average - divide the sum ny the length (count)
total = sum(grades)
count = len(grades)
average = total / count
print('Total is: ', total)
print('Average is: ', average)
