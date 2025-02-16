

def test_product_init(product_list):
    assert product_list.name == "Iphone 15"
    assert product_list.description == "512GB, Gray space"
    assert product_list.price == 210000.0
    assert product_list.quantity == 8