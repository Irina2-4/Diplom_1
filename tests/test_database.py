from praktikum.database import Database

class TestDatabase:
    def test_available_buns(self):
        buns = Database()
        available_buns = buns.available_buns()
        assert len(available_buns) == 3

    def test_available_ingredients(self):
        ingredients = Database()
        available_ingredients = ingredients.available_ingredients()
        assert len(available_ingredients) == 6