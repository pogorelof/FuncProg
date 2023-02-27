vacations = {}
n = int(input('Количество сотрудников: '))

for i in range(n):
    name, day, months = input('Имя, день и месяц: ').split()
    if vacations.get(months) is None:
        vacations[months] = {name: day}
    else:
        vacations[months][name] = day

find_months = input('По какому месяцу узнать отдыхающих: ')

if vacations.get(find_months) is None:
    print('Отдыхающих нет!')
    exit(0)

for key, values in vacations[find_months].items():
    print(f'{key} отдыхает {values}')
