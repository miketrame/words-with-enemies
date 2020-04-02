"""
Main game logistics taken
from https://en.wikipedia.org/wiki/Scrabble_letter_distributions.
"""
import player
import random

LETTER_POINTS = {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4,
                 "I":1, "J":8, "K":5, "L":1, "M":3, "N":1, "O":1, "P":3,
                 "Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, "W":4, "X":8,
                 "Y":4, "Z":10, }

class Game:
    """Game class."""
    def __init__(self):
        self.board = []
        self.bonus = []
        for i in range(15):
            row = []
            for j in range(15):
                row.append(" ")
            self.board.append(row)
            self.bonus.append(row)

        self.player1 = player.Player()
        self.player2 = player.Player()

        self.letters = []
        self.letters += ["A" for i in range(9)]
        self.letters += ["B" for i in range(2)]
        self.letters += ["C" for i in range(2)]
        self.letters += ["D" for i in range(4)]
        self.letters += ["E" for i in range(12)]
        self.letters += ["F" for i in range(2)]
        self.letters += ["G" for i in range(3)]
        self.letters += ["H" for i in range(2)]
        self.letters += ["I" for i in range(9)]
        self.letters.append("J")
        self.letters.append("K")
        self.letters += ["L" for i in range(4)]
        self.letters += ["M" for i in range(2)]
        self.letters += ["N" for i in range(6)]
        self.letters += ["O" for i in range(8)]
        self.letters += ["P" for i in range(2)]
        self.letters += ["P" for i in range(2)]
        self.letters.append("Q")
        self.letters += ["R" for i in range(6)]
        self.letters += ["S" for i in range(4)]
        self.letters += ["T" for i in range(6)]
        self.letters += ["U" for i in range(4)]
        self.letters += ["V" for i in range(2)]
        self.letters += ["W" for i in range(2)]
        self.letters.append("X")
        self.letters += ["Y" for i in range(2)]
        self.letters.append("Z")

        random.shuffle(self.letters)

        self.current_player = self.player1
        self.over = False

    def setup(self):
        """Setup the game."""
        print("Player 1, enter name:")
        self.player1.name = input()

        print("Player 2, enter name:")
        self.player2.name = input()

        self.player1.letters += [self.letters.pop() for i in range(7)]
        self.player2.letters += [self.letters.pop() for i in range(7)]

    def print_board(self):
        """Print board in a readable fashion."""
        print("  ", end='')
        for i in range(15):
            letter = "A"
            print(" %s" % chr(ord(letter) + i), end='')
        print()

        print("  " + "-" * 31)
        for row in range(15):
            if row < 9:
                print("%i " % (row + 1), end='')
            else:
                print(row + 1, end='')
            for col in range(14):
                print("|%s" % (self.board[row][col]), end='')
            print("|%s|" % (self.board[row][14]))
        print("  " + "-" * 31)

    def prompt_player(self):
        """Prompt the appropriate player for their move."""
        print("Your turn, ", self.current_player.name)
        print(' '.join(self.current_player.letters))

    def change_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
