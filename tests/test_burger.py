from praktikum.burger import Burger
import allure
from conftest import mock_bun,mock_ingredient
from praktikum.database import Database
class TestBurger:
    @allure.title('Выбор булки')
    def test_set_buns(self,mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    @allure.title('Добавление ингредиентов')
    def test_add_ingredient(self,mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
    @allure.title("Удаление ингредиентов")
    def test_remove_ingredient(self,mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        index = burger.ingredients.index(mock_ingredient)
        burger.remove_ingredient(index)
        assert mock_ingredient not in burger.ingredients

    @allure.title("Перемещение ингредиентов")
    def test_moving_ingredients(self,mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        ingredient = burger.ingredients[0]
        burger.move_ingredient(0,1)
        assert burger.ingredients[1] == ingredient
    @allure.title("Цена бургера")
    def test_price_burger(self,mock_bun,mock_ingredient):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[1])
        burger.add_ingredient(database.available_ingredients()[1])
        assert burger.get_price() == 600.0

    @allure.title("Получение рецепта")
    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[1])
        burger.add_ingredient(database.available_ingredients()[1])
        receipt = "(==== white bun ====)\n"\
                  "= sauce sour cream =\n"\
                  "(==== white bun ====)\n\n"\
                  "Price: 600"
        assert receipt == burger.get_receipt()
