from src.product import Product


class Smartphone(Product):
    efficiency: str
    model: str
    memory: str
    color: str

    def __init__(self, efficiency, model, memory, color):

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
