import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.smartphone import Smartphone
from src.product import Product


@pytest.fixture
def product_list():
    Category.product_count = 0
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def category_list():
    Category.product_count = 0
    return Category(
        name="Смартфоны", description="Самые лучшие", product_list=["Samsung", "Улучшенная версия", 1000, 1]
    )


@pytest.fixture
def category_empty_prod_list():
    return Category(name="Смартфоны", description="Самые лучшие", product_list=[])


@pytest.fixture
def new_price():
    return Product(name="Iphone 15", description="512GB, Gray space", price=-210000.0, quantity=8)


@pytest.fixture
def category_list_str():
    Category.product_count = 0
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category(name="Смартфоны", description="Самые лучшие", product_list=[product2])


@pytest.fixture
def category_list_add1():
    Category.product_count = 0
    product1 = Product("Samsung", "Улучшенная версия", 1000, 1)
    return Category(name="Смартфоны", description="Самые лучшие", product_list=[product1])


@pytest.fixture
def category_list_add2():
    Category.product_count = 0
    product2 = Product("Gnusmas", "Ухудшенная версия", 500, 11)
    return Category(name="Смартфоны", description="Не самые лучшие", product_list=[product2])


@pytest.fixture
def product_list_add1():
    return Product("Gnusmas", "Ухудшенная версия", 500, 10)


@pytest.fixture
def product_list_add2():
    return Product("Samsung", "Улучшенная версия", 1000, 1)


@pytest.fixture
def lawngrass_list():
    return LawnGrass("Russia", "1 months", "green")


@pytest.fixture
def smartphone_list():
    return Smartphone("Snapdragon 8", "C300", "512Gb", "black")
