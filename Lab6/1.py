#Кортежи

#Имя, возраст, язык программирования, место учебы, Специальность, опыт работы
student = ['Vladimir', 21, 'Python', 'Satbayev University', 'Computer Science', 21]

print('Кортеж')
#1
print('1# передача листа в кортеж')
student_tuple = tuple(student)
print(student_tuple)

#2
print('\n2# получение подкортежей')
student_name_age = student_tuple[0:2]
print(student_name_age)

#3
el = 21
print('\n3# количество элементов')
print(f'{el}: ', student_tuple.count(el))

#4
print('\n4# передача строки')
string_tuple = tuple('Hello world!')
print(string_tuple)

#5
print('\n5# изменение элемента')
try:
    string_tuple[0] = 'qwe'
except TypeError:
    print('Ошибка изменения. Кортежи нельзя изменять')

#Множества

print('Множества')
#1
print('\n1# уникальность множеств')
not_unique_list = [1,1,1,2,6,1,4,4,8,7,8]
set_from_list = set(not_unique_list)
print(set_from_list)

#2
print("\n2# добавление элементов")
set_from_list.add(10)
print(set_from_list)

#3
print('\n3# удаление элементов')
set_from_list.remove(1)
print(set_from_list)

#4
print('\n4# копирование элементов')
copy_set = set_from_list.copy()
print('copy_set: ', copy_set)

#5
print('\n5# пересечение элементов')
copy_set = {4,1,2,66}
print('1: ', set_from_list)
print('2: ', copy_set)
inters = set_from_list.intersection(copy_set)
print('Их пересечения: ', inters)
