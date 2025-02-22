import pytest

from src.category import Category
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
