def test_smartphone(smartphone_list):
    """Тестирование корректности инициализации объектов подкласса Smartphone класса Product"""
    assert smartphone_list.efficiency == "Snapdragon 8"
    assert smartphone_list.model == "C300"
    assert smartphone_list.memory == "512Gb"
    assert smartphone_list.color == "black"
