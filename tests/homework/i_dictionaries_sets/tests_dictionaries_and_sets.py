import unittest
from homework.i_dictionaries_sets.dictionary import add_inventory
from homework.i_dictionaries_sets.dictionary import remove_inventory_widget
from homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_or_prog2, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog2_not_prog_1
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
    def test_get_students_who_took_prog1_and_prog2():
        prog1 = {"Student1","Student2","Student3"}
        prog2 = {"Student3","Student4","Student5"}
        if get_students_who_took_prog1_and_prog2(prog1, prog2) == {"Student3"}:
            return True
        else:
            return False
    def test_get_students_who_took_prog1_or_prog2():
        prog1 = {"Student1","Student2","Student3"}
        prog2 = {"Student3","Student4","Student5"}
        if get_students_who_took_prog1_or_prog2(prog1, prog2) == {"Student1","Student2","Student3","Student4","Student5"}:
            return True
        else:
            return False
    def test_get_students_who_took_prog1_not_prog_2():
        prog1 = {"Student1","Student2","Student3"}
        prog2 = {"Student3","Student4","Student5"}
        if get_students_who_took_prog1_not_prog_2(prog1, prog2) == {"Student1","Student2"}:
            return True
        else:
            return False
    def test_get_students_who_took_prog2_not_prog_1():
        prog1 = {"Student1","Student2","Student3"}
        prog2 = {"Student3","Student4","Student5"}
        if get_students_who_took_prog2_not_prog_1(prog1, prog2) == {"Student4","Student5"}:
            return True
        else:
            return False