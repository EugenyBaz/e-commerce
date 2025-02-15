

class Category:
    name: str
    description: str
    products: list
    quantity_cat = 0
    quantity_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        quantity_cat += 1
        quantity_products += len(products) if products else 0

if __name__ == "__main__"

