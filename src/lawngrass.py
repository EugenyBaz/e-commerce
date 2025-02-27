from src.product import Product


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(self, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
