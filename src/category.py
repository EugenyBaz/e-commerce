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
        self.products = product_list if product_list else []
        Category.category_count += 1
        Category.product_count += len(product_list) if product_list else 0

    def __repr__(self):
        return f"Category(name='{self.name}', description='{self.description}')"


if __name__ == "__main__":
    product_list1 = Product("телефон", "черный, 100Гб", 100000.0, 1)
    category1 = Category("Телевизоры", "SMART телевизоры", [product_list1])
    print(category1.name)
    print(category1.description)
    print(category1.products)
