import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_list():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
    return Product(name = "Iphone 15",
        description = "512GB, Gray space",
        price = 210000.0,
        quantity = 8)


@pytest.fixture
def category_list():
    return Category(
        name="Смартфоны", description="Самые лучшие", product_list=["Samsung", "Улучшенная версия", 1000, 1]
    )

@pytest.fixture
def category_empty_prod_list():
    return Category(
        name="Смартфоны", description="Самые лучшие", product_list=[]
    )
    return Category (
    name = "Смартфоны",
    description = "Самые лучшие",
    product_list = ["Samsung", "Улучшенная версия", 1000, 1])
