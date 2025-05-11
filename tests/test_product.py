from unittest.mock import patch

from src.product import Product


def test_product(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.quantity == 5


def test_new_product(new_product_dct):
    product1 = Product.new_product(new_product_dct)
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 160000.0
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.quantity == 5


def test_new_product_lst(new_product_dct, product):
    product1 = Product.new_product(new_product_dct, [product])
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.quantity == 10


def test_product_price(product, capsys):
    product.price = -1000
    assert capsys.readouterr().out == "Цена не должна быть нулевая или отрицательная\n"


@patch("builtins.input")
def test_product_price_low(mock_input, product, capsys):
    product.price = 1000
    mock_input.return_value = "n"
    mock_input.assert_called_once_with("Вы уверены что цена должна быть понижена?(y/n)")


def test_product_add(product, product1):
    assert product + product1 == product1.price * product1.quantity + product.quantity * product.price