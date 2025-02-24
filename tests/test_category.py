from src.category import Category


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
    expected_product = [f"{product_list.name}, {product_list.price} руб. Остаток: {product_list.quantity} шт."]
    assert expected_product == category.products

    """Тестирование счетчика добавления товаров в категорию"""
    assert Category.product_count == 1


def test_add_product_valid(capsys, category_list):
    """Тестирование на валидность  добавления товаров в категорию"""
    category = Category(name="Electronics", description="All kinds of electronics")
    category.add_product(category_list)
    message = capsys.readouterr()
    assert message.out.strip() == "Продукт не является экземпляром класса Product или любого его подкласса"


def test_category_str(category_list_str):
    """Тест на строковое представление в Category"""
    assert str(category_list_str) == "Смартфоны, Количество продуктов: 8 шт."


def test_category_add_(category_list_add1, category_list_add2):
    """Тест на подсчет товаров по категории на складе"""
    assert category_list_add1 + category_list_add2 == 6500
