def test_category1(category1, category2):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products_in_list) == 3

    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category2.products_in_list) == 1

    assert category2.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'

    assert category1.category_count == 2
    assert category2.category_count == 2

    assert category1.product_count == 4
    assert category2.product_count == 4


def test_add_product(capsys, category1, product):
    category1.add_product(product)
    assert len(category1.products_in_list) == 4

    text = capsys.readouterr().out.strip().split("\n")

    assert text[-2] == "Товар успешно добавлен"
    assert text[-1] == "Обработка добавления товара завершена"


def test_add_product_err(capsys, category1):
    category1.add_product("Not a product")
    text = capsys.readouterr().out.strip().split("\n")
    assert text[-2] == "Тип добавляемого товара не соответствует типу товар категории"
    assert text[-1] == "Обработка добавления товара завершена"


def test_category(category1):
    assert (
        str(category1)
        == f"{category1.name}, количество продуктов: {sum([prod.quantity for prod in category1.products_in_list])} шт."
    )


def test_add_product_err_zero(capsys, category1, product, product1):
    product.quantity = 0
    category1.add_product(product)
    text = capsys.readouterr().out.strip().split("\n")

    assert text[-2] == "Нулевое количество продукта"
    assert text[-1] == "Обработка добавления товара завершена"


def test_middle_price(category1):
    assert category1.middle_price() == 140333.33


def test_middle_price_err(category3):
    assert category3.middle_price() == 0
