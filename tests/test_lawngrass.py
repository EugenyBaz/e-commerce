def test_lawngrass(lawngrass_list):
    """Тестирование корректности инициализации объектов подкласса LawnGrass класса Product"""
    assert lawngrass_list.country == "Russia"
    assert lawngrass_list.germination_period == "1 months"
    assert lawngrass_list.color == "green"
