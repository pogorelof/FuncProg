girls = open('Lab12/2/girl.txt', 'r')
boys = open('Lab12/2/boys.txt', 'r')

girls_list = list()
boys_list = list()

for i in girls.readlines():
    girls_list.append(i.replace('\n', ''))
for i in boys.readlines():
    boys_list.append(i.replace('\n', ''))

name = input('Введите имя:').capitalize()
if name in girls_list or name in boys_list:
    print('Имя находится в списке популярных имен')
else:
    print('Имя не находится в списке популярных имен')

girls.close()
boys.close()
