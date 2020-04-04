"""Player class logic and information."""

class Player:
    """Player class."""

    def __init__(self):
        self.name = ""
        self.score = 0
        self.letters = [] # size 7

    def __eq__(self, other):
        return self.name == other.name
