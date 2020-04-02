"""Player class logic and information."""
import enchant

DICT = enchant.Dict("en_US")

class Player:
    """Player class."""

    def __init__(self):
        self.name = ""
        self.score = 0
        self.letters = [] # size 7

    def __eq__(self, other):
        return self.name == other.name

    def play(self, word, pos, orientation, game):
        """
        Play a word onto the board. 
        Returns True if successful, False otherwise.
        """
        for letter in word:
            if letter not in self.letters:
                print("Invalid move. You do not have that letter.")
                return False
        
        if not DICT.check(word):
            print("Invalid move. Word does not exist.")
            return False
