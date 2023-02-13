#  Напишите	 функцию,	 показывающую,	 отсортирован	 ли	
# переданный	 ей	 в качестве	 параметра	 список	 (по	 возрастанию	 или	
# убыванию).	 Функция	 должна	 возвращать	 True,	 если	 список	
# отсортирован,	 и False	 в противном	 случае.	 В основной	 программе	
# запросите	 у пользователя	 последовательность	 чисел	 для	 списка,	 после	
# чего	 выведите	 сообщение	 о том,	 является	 ли	 этот	 список	
# отсортированным	изначально

import random


def isSorted(list):
    sorted_list = sorted(list)

    reverse_sorted_list = sorted(list)
    reverse_sorted_list.reverse()
                                            
    if list == sorted_list or list == reverse_sorted_list:
        return True
    else:
        return False

size = random.randint(3,7)
my_list = [random.randint(1,10) for i in range(size)]

print('Список: ' + str(my_list))
print('isSorted: ' + str(isSorted(my_list)))

print('\nСортировка списка...\n')
my_list.sort()

print('Список: ' + str(my_list))
print('isSorted: ' + str(isSorted(my_list)))

print('\nРазворот списка...\n')
my_list.reverse()

print('Список: ' + str(my_list))
print('isSorted: ' + str(isSorted(my_list)))