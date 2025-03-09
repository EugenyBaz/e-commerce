from src.product import Product


def test_print_mixin_product(capsys):
    """Тест корректности работы миксина"""
    Product(name="Iphone 15", description="512GB, Gray space", price=-210000.0, quantity=8)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, 512GB, Gray space, -210000.0, 8)"
