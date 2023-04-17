file = open('Lab12/text.txt', 'w') #1
file.write('New Line\n2\n3\n4') #2
file.close() #3

file = open('Lab12/text.txt', 'r')
print(file.read()) #4, 5
file.close()

file = open('Lab12/text.txt', 'r')
print("Первая строка: " + file.readline()) #6
print("Вторая строка: " + file.readline(2))
print("Третья строка: " + file.readline(3))
print("Четвертая строка: " + file.readline(4))
file.close()