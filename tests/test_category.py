def test_category_init(category_list):
    """Тестирование корректности инициализации объектов класса Category"""
    assert category_list.name == "Смартфоны"
    assert category_list.description == "Самые лучшие"
    assert category_list.products == ["Samsung", "Улучшенная версия", 1000, 1]

    """Тестирование корректности подсчета категорий и продуктов"""
    assert category_list.category_count == 1
    assert category_list.product_count == 4
