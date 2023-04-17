file = open('Lab12/5/diseases.txt', 'r')
diseases_dict = dict()
for i in file.readlines():
    bufer_list = i.split(' ')
    diseases_dict[bufer_list[0]] = int(bufer_list[1].replace('\n', ''))

top_3 = dict()

for key, value in sorted(diseases_dict.items(), key=lambda x: x[1], reverse=True):
    top_3[key] = value
    if len(top_3) == 3:
        break

print("Топ 3 города по заражаемости: ")
for key, value in top_3.items():
    print(f'Город: {key} - {value} человек')