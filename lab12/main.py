from tkinter import *

def p1():
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт")

    class IceCreamStand(Restaurant):

        def __init__(self, restaurant_name, cuisine_type):
            super().__init__(restaurant_name, cuisine_type)
            self.flavor = ['клубничное', 'шоколадное', 'ванильное', 'фисташковое', 'малиновое']

        def menu(self):
            print("Вкусы мороженного")
            for i in self.flavor:
                print(i)

    Res = IceCreamStand(input("Введите название ресторана"), input("Введите кухню ресторана"))
    Res.describe_restaurant()
    Res.menu()


def p2():

    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print('\n' + self.restaurant_name, "-", self.cuisine_type)

        def open_restaurant(self):
            print(self.restaurant_name, 'открыт!')

    class IceCreamStand(Restaurant):

        def __init__(self, restaurant_name, cuisine_type, location, time, flavor=['клубничное', 'шоколадное', 'ванильное', 'фисташковое', 'малиновое']):
            super().__init__(restaurant_name, cuisine_type)
            self.location = location
            self.time = time.split()
            self.flavor = flavor

        def menu(self):
            for i in self.flavor:
                print(i)
            self.UI()

        def UI(self):
            root = Tk()
            root['bg'] = '#fafafa'
            root.title('Меню вкусов')
            root.geometry('300x250')
            root.resizable(width=False, height=False)

            canvas = Canvas(root, height=250, width=300)
            canvas.pack()

            frame = Frame(root, bg='#ffb700', bd=5)
            frame.place(relx=0.15, rely=0.15, relheight=0.7, relwidth=0.7)

            title = Label(canvas, text='Вкусы мороженого', bg='#fafafa', font=45)

            for i in self.flavor:
                item = Label(frame, text=i, bg='#ffb700', font=40)
                item.pack()
            title.pack()

            root.mainloop()

        def info(self):
            print(self.restaurant_name, "работает c", self.time[0], "по", self.time[1])
            print("Кафе находится по адресу", self.location, '\n')

        def delete(self, a):
            self.flavor.remove(a)

        def add(self, b):
            self.b = b
            self.flavor.append(b)

        def search(self, c):
            if c in self.flavor:
                print(c, "есть в наличии\n")
            else:
                print(c, "нет в наличии\n")

    class FruitIce(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, location, time, size, flavor=['клубничное', 'шоколадное', 'ванильное', 'фисташковое', 'малиновое']):
            super().__init__(restaurant_name, cuisine_type, location, time, flavor)
            self.size = size
            self.flavor = flavor

        def choice(self, ch):
            if self.size == 'маленький':
                print('Cтоимость - 40 р.')
            if self.size == 'средний':
                print('Cтоимость - 80 р.')
            if self.size == 'большой':
                print('Cтоимость - 120 р.')
            if ch in self.flavor:
                print('Ваш заказ принят в работу')
            else:
                print ('Такого вкуса нет, выберете из меню:', *self.flavor)
                self.choice(input('Выберете вкус мороженого'))


    rest = IceCreamStand(input("Введите название ресторана"), input("Введите кухню ресторана"), input("Введите адрес"), input("Введите начало и конец работы через пробел"))
    rest.describe_restaurant()
    rest.info()
    rest.menu()
    rest.delete(input("Что удалить?"))
    rest.add(input("Что добавить?"))
    rest.search(input("Что искать?"))
    rest.menu()
    order1 = FruitIce("sfvg", "drgf", "dfgvdgf", '3 7', input('Выберете размер мороженого'), flavor=['клубничное', 'шоколадное', 'ванильное', 'фисташковое', 'малиновое'])
    order1.choice(input('Выберете вкус мороженого'))

p1()
p2()
