
def Find():
    with open("synonyms2.txt", "r+") as text:
        lines = text.read()
        text.seek(0)
        n = 0
        word = input(str("Найти слово: "))
        for line in text:
            if word in line:
                n = 1
                print(line.strip())
                Choice(word, line, lines)
        if n == 0:
            print("Cлово не найдено")
            return word


def Choice(word, line, lines):
    user_choice = input("Добавить новый синоним?:  ")
    if user_choice == 'Да' or user_choice == 'Yes':
        lines = Add(word, line, lines)
    else:
        return 0


def Add(word, line, lines):
    x = input("Введите новый синоним: ")
    new_words = lines.replace(line, line.replace('\n','').title() + " - " + x.title() + "\n")
    with open("synonyms2.txt", "w") as text:
        text.write(new_words)
    print("Синоним добавлен")
    lines = new_words
    return


def Main(word = ""):
    while True:
        if Find() == "stop":
            exit(0)
        else:
            Find()
Main()

