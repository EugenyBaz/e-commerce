# E-commerce

Созданы классы Product  и Category. 
Для класса Product  описаны необходимые атрибуты.
Для класса Category  определены необходимые атрибуты
Также реализована функция вывода категорий товаров для подгружаемых файлов json
Добавлен функционал вывода итоговой суммы стоимости склада по категории
Добавлена функциональность сложения таким образом, 
чтобы можно было складывать товары только из одинаковых классов продуктов.
Доработан метод, который добавляет продукт в категорию,
таким образом, чтобы не было возможности добавить вместо продукта или его наследников любой
другой объект.
Добавлен функционал о выводе информации заведенного нового продукта
Добавлен метод подсчета средней стоимости товаров в категории
Добавлен метод на подсчет средней стоимости товаров по категории и вывода значения 0 при заданном пустом списке товаров

## Содержание
...

## Технологии
...

## Использование
...

## Разработка
Созданы классы Product  и Category. 
Для класса Product  описаны необходимые атрибуты.
Для класса Category  определены необходимые атрибуты
Также реализована функция вывода категорий товаров для подгружаемых файлов json
Добавлены методы по строковому представлению Product и Category
Добавлен функционал вывода итоговой суммы "стоимости склада" по категории
Создан абстрактный класс BaseProduct
Добавлен Миксин о выводе информации заведенного нового продукта
Добавлен функционал проверки при добавлении продукта с количеством больше 0
Добавлен метод подсчета товаров по категории на складе
Добавлен метод на подсчет средней стоимости товаров по категории и вывода значения 0 при заданном пустом списке товаров 



### Требования
..

### Установка зависимостей
..
### Запуск Development сервера
..
### Создание билда
..

## Тестирование 

Проект покрыт юнит-тестами Pytest.

- корректность инициализации объектов класса Category,
- корректность инициализации объектов класса Product,,
- подсчет количества продуктов,
- подсчет количества категорий.
- добавлено тестирование пустого списка продуктов.
- добавлены тесты проверки инициализации двух новых категорий "Смартфон" и "Трава газонная"
- добавлен тест на валидность  добавления товаров в категорию
- добавлен htmlcov в репозиторий
- добавлен тест корректности работы миксина - Вывод информации о заведенном новом продукте
- добавлен тест на выброс ошибки при добавлении в категорию товара с количеством = 0
- добавлен тест на подсчет товаров по категории на складе
- добавлен тест на корректный подсчет средней стоимости товаров по категории
- добавлен тест на вывод значения 0 при заданном пустом списке товаров

## Deploy и CI/CD
...

## Contributing
...

## FAQ 
...

## To do
..

## Команда проекта

Евгений Базавод 

## Источники
...