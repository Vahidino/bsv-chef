import pytest
from src.controllers.recipecontroller import get_available_items

def test_database_whithdrawl():
    database = {
        "item1": 100,
        "item2": 200,
    }
    assert get_available_items(database, "item1") == 100



def test_database_down():

    assert get_available_items(None) == None