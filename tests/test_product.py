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

def test_new_price_invalid(capsys,new_price):
    new_price.price = -200
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"




