import random

#рандомное число от 1 до 10
random_int = random.randint(1,10)
print(f'Randint: {random_int}')

#рандомное число от 1 до 20 с шагом 2
#то есть, число всегда нечетное
random_range = random.randrange(1,20,2)
print(f'Randrange: {random_range}')

#генерация рандомного числа типа double от 0 до 1
random = random.random()
print(f'Random: {random}')

#enumerate помогает выводить список с индексами
#индекс слева - элемент в списке справа
#вывод в виде кортежа
my_list = [2,4,'four',8.1,'ten',12]
for i in enumerate(my_list):
    print(i)