from src.product import Product
from src.category import Category
from src.data_upload import read_data_json

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, "
                         "как средство не только коммуникации,"
                         " но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(category1)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)
    print(category1.products)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор,"
                         " который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # Доп задание
    prod_list = read_data_json()

    categories = []
    for category_dict in prod_list:
        products = [Product(product['name'], product['description'], product['price'], product['quantity']) for product
                    in category_dict['products']]
        category = Category(category_dict['name'], category_dict['description'], products)
        categories.append(category)

    print(categories)

    total_cost = category1 + category2
    print(total_cost)
