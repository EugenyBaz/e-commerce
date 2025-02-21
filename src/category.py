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

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        prod_list = []
        for prod in self.__products:
            prod_list.append(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.")
        return prod_list
