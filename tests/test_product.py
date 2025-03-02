def test_product_init(product_list):
    assert product_list.name == "Iphone 15"
    assert product_list.description == "512GB, Gray space"
    assert product_list.price == 210000.0
    assert product_list.quantity == 8


def test_new_product(product_list):
    assert product_list.name == "Iphone 15"
    assert product_list.description == "512GB, Gray space"
    assert product_list.price == 210000.0
    assert product_list.quantity == 8


def test_price(product_list):
    assert product_list.price == 210000.0


def test_new_price(new_price):
    new_price.price = 500
    assert new_price.price == 500


def test_new_price_invalid(capsys, new_price):
    new_price.price = -200
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_product_str(product_list):
    """Тест на строковое представление в Product"""
    assert str(product_list) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add_(product_list_add1, product_list_add2):
    """Тест на подсчет товаров на складе"""
    assert product_list_add1 + product_list_add2 == 6000
