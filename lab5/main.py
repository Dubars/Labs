def one():
    from random import randint
    arr = [randint(0, 20) for i in range(5)]
    a = int(input())
    if a in arr:
        print(a, ' Поздравляю, Вы угадали число!')
    else:
        print(a, 'Нет такого числа!')
    print(arr, '- Все числа')

def two():
    from random import randint
    arr = [randint(0, 10) for i in range(5)]
    a = [x for x in arr if arr.count(x) > 1]
    print(a)
    if len(a) < 1:
        print('Все числа уникальны')
    else:
        x = int(a[0])
        print(x, " - Повторяющиеся число. ", arr.count(x), " - Число повторений")
        print(arr, '- Все числа')

def three():
    week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    weekends = int(input("Сколько желаете выходных? "))
    print('Выходные:', *week[-weekends:])
    print('Будние:', *week[:-weekends])
    print()

def four():
    import random
    grup_one = ["Аленик", "Абадовский", "Бусыгина", "Дюбарев", "Дубовец", "Порталенко", "Тюрин", "Шапран", "Иванов", "Рябиченко"]
    grup_two = ["Бесова", "Воробьёва", "Елизарова", "Исхаков", "Ковалёв", "Кремер", "Паронько", "Ишин", "Жарко", "Иванов"]
    print("Первая группа: ", *grup_one)
    print("Вторая группа: ", *grup_two)
    random.shuffle(grup_one)
    random.shuffle(grup_two)
    team = (grup_one[:5] + grup_two[:5])
    sort_team = sorted(team)
    k = team.count("Иванов")
    print("Команда: ", *team)
    print("Отсортированая Команда: ", *sort_team)
    if k > 0:
        print("Иванов встречается в команде ", k, "раз")
    else:
        print("Иванова нет")
one()
two()
three()
four()