count_of_comments = {}

while True:
    name = input('Введите имя: ')
    comment = input('Введите комментарий: ')

    if name == '' or comment == '':
        break
    
    if count_of_comments.get(name) is None:
        count_of_comments[name] = 1
    else:
        count_of_comments[name] += 1

count = 0
print('Уникальные комментаторы: ')
for name in count_of_comments.keys():
    if count_of_comments[name] <= 1: 
        print(name)
        count += 1
print('Общее число уникальных комментаторов: ' + str(count))