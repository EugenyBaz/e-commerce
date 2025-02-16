class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'name="{self.name}", description="{self.description}", price={self.price}, quantity={self.quantity})'


if __name__ == "__main__":
    product1 = Product("телефон", "черный, 100Гб", 100000.0, 1)
    product2 = Product("холодильник", "белый", 60000.0, 1)
    product3 = Product("наушники", "красные, BT", 45000.0, 1)
    product4 = Product("кофеварка", "черный", 78000.0, 1)
    print(product1.name)
    print(product2.description)
    print(product3.price)
    print(product4.quantity)
