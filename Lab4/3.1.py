my_string = input('Введите строку:')
upper = 0
lower = 0
for i in my_string:
    if i.islower():
        lower += 1
    if i.isupper():
        upper += 1

if lower < upper:
    my_string = my_string.upper()
else:
    my_string = my_string.lower()

print(my_string)