def p1():
    a = {"Россия": "Москва", "Германия": "Берлин", "США": "Вашингтон", "Австралия": "Камберра"}
    print("Страны - столицы : ")
    for c, b in a.items():
        print(c, ":", b)
    c = input("Введите название страны: ")
    if c in a:
        print("Столица", c, ":", a[c])
    else:
        print("Страна", c, "не найдена")
    print("Отсортированный словарь: ")
    for c, b in sorted(a.items()):
        print(c, ":", b)

def p2():
    word = input("Введите слово: ").upper()
    k = 0
    for a in word:
        if a in "АВЕИНОРСТ":
            k += 1
        elif a in "ДКЛМПУ":
            k += 2
        elif a in "БГЁЬЯ":
            k += 3
        elif a in "ЙЫ":
            k += 4
        elif a in "ЖЗХЦЧ":
            k += 5
        elif a in "ШЭЮ":
            k += 8
        elif a in "ФЩЪ":
            k += 10
    print(f"стоимость слова {word}: {k}"," очков")
def p3():
    a = set()
    chinese_speakers = []
    students = {'Алексей':{'Китайский','Английский','Немецкий'},'Юра':{'Китайский','Французский'},'Анастасия':{'Английский','Немецкий','Японский'},'Таня':{'Английский','Японский'}}
    for student, languages in students.items():
        a.update(languages)
        if 'Китайский' in languages:
            chinese_speakers.append(student)
    sorted_a = sorted(list(a))
    print(*sorted_a)
    print(*chinese_speakers)
p1()
p2()
p3()