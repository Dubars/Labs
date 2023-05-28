words = []

while (new_word := str(input())) != "stop":
    words.append(new_word)
print("".join(words))

def proc2():

    while (new_word := str(input())) != "stop":
        if 'ф' in new_word or 'Ф' in new_word:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")
def proc3():
    from random import randint
    k = 0
    pobeda = 0
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end = "")
        otvet = input()
        while not otvet.isdigit() and otvet != "stop":
            print("Вы ввели что-то не то...")
            otvet = input()
        if otvet == "stop":
            break
        if int(otvet) == a + b:
            pobeda += 1
            print("Правильно!")
            print(pobeda)
        else:
            k += 1
            print("Ответ неверный")
            print(k)
        if k == 3:
            print(f"Игра окончена. Правильных ответов: {pobeda}")
            break


proc2()
proc3()