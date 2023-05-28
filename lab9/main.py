import os
import csv
def p1():
    from PIL import Image, ImageFilter
    if not os.path.isdir("New_Image"):
        os.mkdir("New_Image")
    os.chdir("Image")
    for filename in os.listdir():
            print(filename)
            with Image.open(filename) as i:
                i.load()
                b = i.filter(ImageFilter.FIND_EDGES)
                b.show()
                os.chdir("../New_Image")
                b.save("New" + filename)
                os.chdir('../Image')
def p2():
    from PIL import Image, ImageFilter
    if not os.path.isdir("New_Image"):
        os.mkdir("New_Image")
    os.chdir("Image")
    for filename in os.listdir():
        if filename.endswith('.jpg') or filename.endswith('.png'):
            print(filename)
            with Image.open(filename) as i:
                i.load()
                b = i.filter(ImageFilter.FIND_EDGES)
                b.show()
                os.chdir("../New_Image")
                b.save("New" + filename)
                os.chdir('../Image')
def p3():
    print("9.3")
    file_path ="F:\lab9\list.csv"
    with open(file_path) as f:
        total_cost = 0
        print('Нужно купить: ')
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            product = row[0]
            quantity = int(row[1])
            prise = int(row[2])
            cost = quantity * prise
            total_cost += cost
            print(f'{product} - {quantity} шт за {prise} руб')
    print(f'Итоговая стоимость: {total_cost} руб')

p1()
p2()
p3()