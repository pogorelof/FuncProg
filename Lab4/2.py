def add_student(name, num_class):
    list_of_names.append(name)
    list_of_class.append(num_class)

def show_student(list_of_names, list_of_class):
    for i in range(len(list_of_names)):
        print(f'Ученик: {list_of_names[i]}')
        print(f'Класс: {list_of_class[i]}')
    

def bubble_sort(nonsort_list, list_names):
    size = len(nonsort_list)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if nonsort_list[j] > nonsort_list[j+1]:
                nonsort_list[j], nonsort_list[j+1] = nonsort_list[j+1], nonsort_list[j]
                list_names[j], list_names[j+1] = list_names[j+1], list_names[j]

list_of_names = []
list_of_class = []

add_student('Vladimir', 11)
add_student('Daniyar', 9)
add_student('Danil', 10)
add_student('Malika', 5)
add_student('Adi', 11)
add_student('Ernar', 6)
add_student('Dulat', 1)

print('До сортировки:')
show_student(list_of_names, list_of_class)
print()

print('После сортировки:')
bubble_sort(list_of_class, list_of_names)
show_student(list_of_names, list_of_class)