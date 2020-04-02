"""Main logic for words-with-enemies."""
import game


def main():
    """Main entry point into the program."""
    print("Welcome to words-with-enemies! The cli for words with friends with")
    print("a solver to defeat your enemies!")
    print("\"help\" for more info.")

    current_game = game.Game()
    current_game.setup()

    while (not current_game.over):
        current_game.print_board()
        current_game.prompt_player()
        user_input = input(">")
        command = user_input.split()[0]
        if command in ("help", "h"):
            print("To make a move, enter:")
            print("play|p word pos orientation")
            print("word         The word you'd like to play.")
            print("pos          The position where you'd like to start your word.")
            print("             Row first, then column. For example 3B")
            print("orientation  The orientation you'd like your word to be in.")
            print("             vertical (or v) or horizontal (or h)")
        if command in ("play", "p"):
            if len(user_input.split()) != 4:
                print("Missing arguments in play command. See \"help\" or try again.")
            word = user_input.split()[1]
            pos = user_input.split()[2]
            orientation = user_input.split()[3]

            if len(pos) != 2:
                print("Invalid position. Try again.")

            print(pos)
            if ord(pos[0]) not in range(ord("A"), ord("O")):
                print("Invalid position. Try again.")
            if int(pos[1]) < 1 or int(pos[1]) > 15:
                print("Invalid position. Try again.")

            if orientation not in ("vertical", "v", "horizontal", "h"):
                print("Invalid orientation. Try again.")
            current_game.current_player.play(word, pos, orientation, current_game)


if __name__ == "__main__":
    main()
