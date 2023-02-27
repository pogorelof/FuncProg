student = {
    'name': 'Vladimir',
    'age': 21,
    'language': 'Python',
    'expirience': 0,
}

#1
print('#1 получение элемента по ключу с помощью скобок')
print('Имя: ' + student['name'])
print('Возраст: ' + str(student['age']))

#2
print('\n#2 получение элемента по ключу с помощью get')
print('Язык программирования: ' + student.get('language'))
print('Не существующее значение: ' + str(student.get('exp')))

#3
print('\n#3 удаление элемента с помощью del')
print('До удаления: ' + str(student))
del student['expirience']
print('После удаления: ' + str(student))

#4
print('\n#4 добавление элемента')
print('До добавления: ' + str(student))
student['expirience'] = 1
print('После добавления: ' + str(student))

#5
print('\n#5 удаление элемента с помощью pop')
print('До удаления: ' + str(student))
student.pop('expirience')
print('После удаления: ' + str(student))