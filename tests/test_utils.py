from unittest.mock import patch

from src.utils import read_data_json


@patch("json.load")
@patch("builtins.open")
def test_read_data_json(mock_open, mock_json, test_json):
    mock_json.return_value = test_json

    assert read_data_json("") == test_json


