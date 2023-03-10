#1. Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно. 
print('1 Задача')
a = 2
b = 10
for i in range(a,b+1):
    print(i)
print()
#2. Даны два целых числа A и В. Выведите все числа от A до B включительно, 
#в порядке возрастания, если A < B, или в порядке убывания в противном случае. 
print('2 Задача')
a = 2
b = 10
if a < b:
    for i in range(a, b):
        print(i)
else:
    for i in range(a, b, -1):
        print(i)
print()
#3. Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, 
#в порядке убывания. В этой задаче можно обойтись без инструкции if.
print('3 Задача')
a = 21
b = 2
for i in range(a, b, -3):
    print(i)
print()
#4. Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. 
#Найдите ее, зная номера оставшихся карточек. 
#Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). 
#Программа должна вывести номер потерянной карточки. 
#Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя. 
print('4 Задача')
n = int(input('Всего карточек:'))
sum = 0
for i in range(1, n + 1):
    sum += i
print('Введите все карточки, помимо потерянное:')
for i in range(n - 1):
    sum -= int(input())
print(f'Потерянная карточка: {sum}')