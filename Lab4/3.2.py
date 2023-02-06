sum = None

while True:
    num1 = input('Введите число 1:')
    num2 = input('Введите число 2:')
    if not num1.isdigit() or not num2.isdigit():
        print("Были введены некорректные значения. Повторите!")
        continue
    sum = int(num1) + int(num2)
    break

print(f'Сумма: {sum}')