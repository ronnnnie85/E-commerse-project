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

    assert category2.products == '55" QLED 4K, 123000.0 руб. Остаток 7 шт.\n'

    assert category1.category_count == 2
    assert category2.category_count == 2

    assert category1.product_count == 4
    assert category2.product_count == 4


def test_add_product(category1, product):
    category1.add_product(product)
    assert len(category1.products_in_list) == 4
