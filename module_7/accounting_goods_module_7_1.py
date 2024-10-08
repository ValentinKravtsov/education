class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        file = open(self.__file_name, 'a')
        file.close()


    def get_products(self):
        file = open(self.__file_name, 'r')
        str_ = file.read()
        file.close()
        return str_

    def add(self, *products):
        for product in products:
            file_1 = open(self.__file_name, 'r')
            if str(product) in file_1.read():
                print(f'Продукт {str(product)} уже есть в магазине')
                file_1.close()
            else:
                file_1 = open(self.__file_name, 'a')
                file_1.write(f"{str(product)}\n")
                file_1.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
