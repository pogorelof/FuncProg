students = tuple(input().split(' '))
print(students)

find = 'ва'
students_with_find = list()
for i in range(len(students)):
    if not students[i].find(find) == -1:
        students_with_find.append(students[i])

str_of_students = ''
for i in range(len(students_with_find)):
    str_of_students += students_with_find[i]
    str_of_students += ' '

print(str_of_students)