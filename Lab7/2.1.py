county_river = {
    'Казахстан': ['Или', 'Иртыш', 'Чу'],
    'США': ['Огайо', 'Снейк', 'Миссури'],
    'Англия': ['Темза', 'Иден', 'Тис']
}

n = int(input('Количество рек: '))
rivers = [input(f'Введите название реки {i+1}: ') for i in range(n)]

new_dict = {}

print()
for river in rivers:
    flag = False
    for key, value in county_river.items():
        if river.capitalize() in value:
            #1
            print(f'Река {river} протекает в {key}\n')
            flag = True
            #3
            if new_dict.get(key) is None:
                new_dict[key] = [river.capitalize()]
            else:
                new_dict[key].append(river.capitalize())
    if not flag:
        #2
        print(f'Реки {river} нет в словаре!')
    
print('Новый словарь на основе списка: ')
print(new_dict)