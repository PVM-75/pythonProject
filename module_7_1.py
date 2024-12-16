class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def add(self, *products):
        for item in products:
            file = open(self.__file_name, 'r')
            existing_products = file.read()
            file.close()
            # print("Из функции add:", item.name)           # пользовался при отладке
            # print("existing_products:", existing_products) # пользовался при отладке
            if item.name in existing_products:
                print(f'Продукт {item.name} уже есть в магазине')
                # file.close()
                    # break
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{item.name}, {item.weight}, {item.category}\n')
                file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        print("Содержимое файла:")
        print(file.read())
        file.close()

if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())