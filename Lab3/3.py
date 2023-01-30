import random

result_list = []

while True:
    my_health = random.randint(100,300)
    enemy_health = random.randint(100,300)
    i = 1
    while True:
        print(f"\nРаунд {i}\n")
        print(f'Ваше здоровье: {my_health}')
        print(f'Здоровье соперника: {enemy_health}')
        if not my_health > 0 and not enemy_health > 0:
            print("Ничья!")
            result_list.append('Ничья')
            break
        elif not enemy_health > 0:
            print("Победа!")
            result_list.append('Победа')
            break
        elif not my_health > 0:
            print("Поражение!")
            result_list.append('Поражение')
            break

        damage_to_enemy = random.randrange(2,150,2)
        damage_to_me = random.randrange(2,150,2)
        enemy_critical_damage = random.random() * 2
        my_critical_damage = random.random() * 2
        
        if enemy_critical_damage > 1:
            damage_to_me *= 1.5
            print(f"Вам нанесен критический урон: {damage_to_me}")
            my_health -= damage_to_me
        else:
            print(f"Вам нанесен урон: {damage_to_me}")
            my_health -= damage_to_me

        if my_critical_damage > 1:
            damage_to_enemy *= 1.5
            print(f"Сопернику нанесен критический урон: {damage_to_enemy}")
            enemy_health -= damage_to_enemy
        else:
            print(f"Сопернику нанесен урон: {damage_to_enemy}")
            enemy_health -= damage_to_enemy
        
        input('\nНажмите для следующего хода\n')
        i += 1
    
    ans = input('Продолжить игру? y/n')
    if ans == 'y':
        continue
    else:
        break

print("Результаты ваших игр: ")
for i in enumerate(result_list, 1):
    print(i)