n = int(input('Размер телефоной книги: '))
numbers = {}
for i in range(n):
    name, number = input('Имя и номер: ').split()
    numbers[name] = number

find_name = input('Имя которое нужно найти: ')
find_number = None

if numbers.get(find_name) is None:
    print('Нет в телефонной книге')
else:
    find_number = numbers.get(find_name)

print(f'Номер по имени {find_name}: {find_number}')