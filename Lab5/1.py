# Напишите	 программу,	 используя минимум	 5 функции для	 работы	 со	
# списком. В	виде	списка	пусть	каждый	студент	предложит свое	резюме

#Имя, возраст, язык программирования, место учебы, Специальность, опыт работы
student = ['Vladimir', 21, 'Python', 'Satbayev University', 'Computer Science', 0]

print('ФИО: ' + student[0])
print('Возраст: ' + str(student[1]))
print('Язык программирования: ' + student[2])
print('Место учебы: ' + student[3])
print('Специальность: ' + student[4])
print('Опыт: ' + str(student[5]))

#1 append()
while True:
    print("\nПринять на работу?\n1-да;\n2-нет.")
    answer = str(input('Ответ: '))
    if answer == '1':
        student.append(True)
        break
    elif answer == '2':
        student.append(False)
        break
    else:
        print("\nНет такого ответа")

#2 clear()
#3 extend()
accepted_workers = ['нет принятых работников']
if student[6]:
    accepted_workers.clear()
    accepted_workers.append(student[0])
    accepted_workers.extend(['Anton', 'Dastan', 'Erasyl', 'Adi', 'Bob'])
    print('Принятые работники: ' + str(accepted_workers))
else:
    student.clear()
    print('Принятые работники: ' + str(accepted_workers[0]))

#4 __len__()
print('Всего принято: ' + str(accepted_workers.__len__()))

#5 sort()
accepted_workers.sort()
print('Сортированный список: ' + str(accepted_workers))