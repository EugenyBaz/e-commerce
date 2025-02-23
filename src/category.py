from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, product_list=None):
        self.name = name
        self.description = description
        self.__products = product_list if product_list else []
        Category.category_count += 1
        if product_list:
            Category.product_count += len(product_list)

    def __repr__(self):
        return f"Category(name='{self.name}', description='{self.description}')"

    def __str__(self):
        cat_quantity = 0
        for prod in self.__products:
            cat_quantity += prod.quantity
        return f"{self.name}, Количество продуктов: {cat_quantity} шт."

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Продукт не является экземпляром класса Product или любого его подкласса")

    @property
    def products(self):
        prod_list = []
        for prod in self.__products:
            prod_list.append(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.")
        return prod_list

    def __add__(self, other):
        if not isinstance(other, Category):
            raise TypeError("Можно складывать только категории!")

        this_total_cost = sum(prod.price * prod.quantity for prod in self.__products)
        other_total_cost = sum(prod.price * prod.quantity for prod in other.__products)

        return this_total_cost + other_total_cost