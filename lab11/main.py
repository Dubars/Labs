def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}. Кухня: {self.cuisine_type}")

        def open_restaurant(self):
                print("Ресторан открыт.")

    newRes = Restaurant("Теремок", "Русская")
    print(newRes.restaurant_name)
    print(newRes.cuisine_type)

    newRes.describe_restaurant()
    newRes.open_restaurant()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}. Кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт.")

    NewRes = []
    for i in range(3):
        Res = Restaurant(input("Введите название ресторна"), input("Введите кухню ресторана"))
        NewRes.append(Res)
        NewRes[i].describe_restaurant()

def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, restaurant_rate):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.restaurant_rate = restaurant_rate

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}. Кухня: {self.cuisine_type}. Рейтинг : {self.restaurant_rate}")

        def open_restaurant(self):
            print("Ресторан открыт.")

        def new_rate(self, new_rate):
            self.restaurant_rate = new_rate

    Res = Restaurant(input("Введите название ресторна"), input("Введите кухню ресторана"), input("Рейтинг ресторана"))
    Res.describe_restaurant()
    Res.new_rate(input("Введите новый рейтинг ресторана"))
    Res.describe_restaurant()
z1()
z2()
z3()

