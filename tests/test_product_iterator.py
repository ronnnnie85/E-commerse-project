from src.product_iterator import ProductIterator


def test_iterator(category1):
    iterator = ProductIterator(category1)
    assert str(next(iterator)) == str(category1.products_in_list[0])
    assert str(next(iterator)) == str(category1.products_in_list[1])

    res = ""
    for prod in iterator:
        res += f"{str(prod)}\n"

    assert res == category1.products
