import unittest
from homework.i_dictionaries_sets.dictionary import add_inventory
from homework.i_dictionaries_sets.dictionary import remove_inventory_widget

class Test_Config(unittest.TestCase):
    def test_add():
        dictionary = {}
        add_inventory(dictionary, "dogs", 10)
        if dictionary.get("dogs") == 10:
            add_inventory(dictionary, "dogs", 25)
            if dictionary.get("dogs") == 35:
                add_inventory(dictionary, "dogs", -10)
                if dictionary.get("dogs") == 25:
                    return True
        return False
    def test_remove():
        dictionary = {}
        add_inventory(dictionary, "dogs", 12)
        add_inventory(dictionary, "cats", 8)
        remove_inventory_widget(dictionary, "dogs")
        if "dogs" not in dictionary:
            return True
        else:
            return False
