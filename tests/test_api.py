from unittest.mock import patch

from requests import Response

from src.api import HHApi


@patch("requests.get")
def test_connect(mock_get):
    hh = HHApi()
    response = Response()
    response.status_code = 200
    mock_get.return_value = response
    mock_get.return_value.status_code = response.status_code
    assert hh._connect("test") == response
    mock_get.assert_called_once()