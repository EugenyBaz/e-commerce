from src.category import Category
from src.product import Product

def test_category_init(category_list):
    """Тестирование корректности инициализации объектов класса Category"""
    assert category_list.name == "Смартфоны"
    assert category_list.description == "Самые лучшие"


    """Тестирование корректности подсчета категорий и продуктов"""
    assert category_list.category_count == 1
    assert category_list.product_count == 4


def test_add_product(product_list):
    """Тестирование добавления товаров в категорию"""
    category = Category(name="Electronics", description="All kinds of electronics")
    category.add_product(product_list)
    expected_product = [f'{product_list.name}, {product_list.price} руб. Остаток: {product_list.quantity} шт.']
    assert expected_product == category.products

    """Тестирование счетчика добавления товаров в категорию"""
    assert Category.product_count == 1





    # def add_product(self, product):
    #     self.__products.append(product)
    #     Category.product_count +=1
    #
    # @property
    # def products(self):
    #     prod_list = []
    #     for prod in self.__products:
    #         prod_list.append(f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.')
    #     return prod_list
