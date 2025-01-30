import pytest
import data
from praktikum.ingredient import Ingredient
import allure

class TestIngredient:

    @allure.title('Тип ингредиента')
    @pytest.mark.parametrize('ingredient_type,name,price',data.INGREDIENTS)
    def test_get_type_correct_ingredient(self,ingredient_type,name,price):
        ingredient = Ingredient(ingredient_type,name,price)
        assert ingredient.get_type() == ingredient_type

    @allure.title('Цена ингредиента')
    @pytest.mark.parametrize('ingredient_type,name,price',data.INGREDIENTS)
    def test_get_type_correct_price(self,ingredient_type,name,price):
        ingredient = Ingredient(ingredient_type,name,price)
        assert ingredient.get_price() == price

    @allure.title('Наименование ингредиента')
    @pytest.mark.parametrize('ingredient_type,name,price',data.INGREDIENTS)
    def test_get_type_correct_name(self,ingredient_type,name,price):
        ingredient = Ingredient(ingredient_type,name,price)
        assert ingredient.get_name() == name
