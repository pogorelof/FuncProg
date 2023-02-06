string = 'Hello'

#1
print('#1 count()')
find = 'l'
length = string.count(find)
print(f'Количество букв {find}: {length} \n')

#2
print('#2 lower()')
string = string.lower()
print(string + '\n')

#3
print('#3 capitalize()')
string = string.capitalize()
print(string + '\n')

#4
print('#4 upper()')
string = string.upper()
print(string + '\n')

#5
print('#5 конкатенция')
string_2 = ' World'
string_3 = string + string_2
print(string_3 + '\n')

#6
print('#6 replace()')
string = string.replace('L', '24')
print(string + '\n')

#7
print('#7 index()')
index_of_E = string.index('E')
print(str(index_of_E) + '\n')

#8
print('#8 split()')
string = 'h_e_l_l_o'
string_list = string.split('_')
print(string_list)
print()

#9
print('#9 title()')
print(string.title() + '\n')

#10
print('#10 endswith()')
print(string.endswith('o'))