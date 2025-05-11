import json
from unittest.mock import patch

from src.utils import load_data_from_json, read_data_json


@patch("json.load")
@patch("builtins.open")
def test_read_data_json(mock_file, mock_json, test_json):
    mock_json.return_value = test_json

    assert read_data_json("") == test_json


@patch("builtins.open")
def test_read_data_json_err_fnf(mock_file):
    mock_file.side_effect = FileNotFoundError
    assert read_data_json("") == []


@patch("json.load")
@patch("builtins.open")
def test_read_data_json_err_decode(mock_file, mock_json):
    mock_json.side_effect = json.JSONDecodeError("", "", 0)
    assert read_data_json("") == []


@patch("src.utils.read_data_json")
def test_load_data_from_json(mock_read, test_json):
    mock_read.return_value = test_json
    result = load_data_from_json("")

    assert len(result) == 1
    assert result[0].name == "Смартфоны"
    assert (
        result[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )

    assert len(result[0].products_in_list) == 3
    assert result[0].products_in_list[0].name == "Samsung Galaxy C23 Ultra"
    assert result[0].products_in_list[0].description == "256GB, Серый цвет, 200MP камера"
    assert result[0].products_in_list[1].price == 210000.0
    assert result[0].products_in_list[2].quantity == 14


@patch("src.utils.read_data_json")
def test_load_data_from_json_empty(mock_read):
    mock_read.return_value = []
    assert load_data_from_json("") == []


@patch("src.utils.read_data_json")
def test_load_data_from_json_not_true(mock_read):
    mock_read.return_value = [
        {
            "name": "Смартфоны",
            "description": "",
        }
    ]
    assert load_data_from_json("") == []
