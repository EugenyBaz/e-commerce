

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
        if product_list:
            Category.product_count += len(product_list)

    def __repr__(self):
        return f"Category(name='{self.name}', description='{self.description}')"



