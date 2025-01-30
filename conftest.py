from unittest.mock import Mock
import pytest
from data import INGREDIENTS,name,price

@pytest.fixture(scope = 'function')
def mock_bun():
    mock_bun = Mock
    mock_bun.name = name
    mock_bun.price = price
    return mock_bun
@pytest.fixture()
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = INGREDIENTS[0][0]
    mock_ingredient.get_name.return_value = INGREDIENTS[0][1]
    mock_ingredient.get_price.return_value = INGREDIENTS[0][2]
    return mock_ingredient

