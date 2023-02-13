# Напишите	программу,	в	которой	предлагается вводить	учащихся	
# различных	групп,	посещающих	секции	по	разным	предметам.	Требуется	
# упорядочить	 список	 по	 различным	 категориям.	 Вывести	 результат	 на	
# экран.

def students_print(students):
    print('\nВывод студентов: ')
    for i in range(len(students)):
        print(f'Имя: {students[i][0]} - Дисциплина: {students[i][1]}')
    print()


students = []
size = int(input('Сколько всего учеников: '))
for i in range(size):
    students.append([input('Введите имя: '), 
                     input('Введите дисциплину: ')])

students_print(students)

print("Сортировка по имени...")
students.sort()

students_print(students)
