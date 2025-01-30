import allure
from praktikum.bun import Bun
import data


class TestBun:
    @allure.title("Проверка правильного названия булки")
    def test_get_name_bun(self):
        bun = Bun(data.name, data.price)
        assert bun.get_name() == data.name

    @allure.title("Проверка отображения корректной стоимости булки")
    def test_get_name_price(self):
        bun = Bun(data.name, data.price)
        assert bun.get_price() == data.price
