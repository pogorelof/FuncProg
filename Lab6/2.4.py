students = tuple(input().split(' '))
print(students)

find = 'ва'
students_with_find = list()
for i in range(len(students)):
    if not students[i].find(find) == -1:
        students_with_find.append(students[i])

print(*students_with_find)