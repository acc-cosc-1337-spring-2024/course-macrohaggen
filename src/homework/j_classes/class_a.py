import random
class die:
    Roll_Value = 0
    def __init__(self) -> None:
        pass
    def roll(self):
        self.Roll_Value = random.randint(1, 6)
    def get_rolled_value(self):
        return self.Roll_Value
    def __str__(self):
        return 'The rolled value is ' + self.Roll_Value