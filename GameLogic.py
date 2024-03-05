class Player:
    itsTheTurnOfPlayerX = True
    number_of_turns = 0

    def __init__(self, player_symbol):
        self.whichPlayer = player_symbol

    def get_which_player(self):
        return self.whichPlayer
    
class GameLogic:
        
    player_x = Player("x")
    player_o = Player("o")
    chosen_field = ""
    play_board = [
        ["0", "1", "2"],
        ["3", "4", "5"],
        ["6", "7", "8"]
    ]

    @staticmethod
    def show_the_field():
        for row in GameLogic.play_board:
            print("\t".join(row))
        print()

    @staticmethod
    def choose_a_field():
        print("Choose a field number!")
        GameLogic.chosen_field = input()

    @staticmethod
    def manipulate_the_board(player_x_or_o):
        for i in range(len(GameLogic.play_board)):
            for j in range(len(GameLogic.play_board[i])):
                if GameLogic.play_board[i][j] == GameLogic.chosen_field:
                    GameLogic.play_board[i][j] = player_x_or_o.get_which_player()

    @staticmethod
    def a_player_manipulates_the_board():
        if Player.itsTheTurnOfPlayerX:
            print("Player x")
            GameLogic.choose_a_field()
            GameLogic.manipulate_the_board(GameLogic.player_x)
        else:
            print("Player o")
            GameLogic.choose_a_field()
            GameLogic.manipulate_the_board(GameLogic.player_o)

    @staticmethod
    def change_2D_array_in_1D_array(was_play_board):
        a_1D_array = []
        for row in was_play_board:
            a_1D_array.extend(row)
        return a_1D_array

    @staticmethod
    def check_winner(was_1D_array, which_player_x_or_o):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combination in win_combinations:
            counter = 0
            for index in combination:
                if was_1D_array[index] == which_player_x_or_o.get_which_player():
                    counter += 1
                    if counter == 3:
                        return True
        return False

    @staticmethod
    def game_on(was_play_board):
        if GameLogic.check_winner(GameLogic.change_2D_array_in_1D_array(was_play_board), GameLogic.player_x) or \
                GameLogic.check_winner(GameLogic.change_2D_array_in_1D_array(was_play_board), GameLogic.player_o):
            return False
        elif Player.number_of_turns == 9:
            return False
        else:
            return True

    @staticmethod
    def who_won(was_play_board):
        if GameLogic.check_winner(GameLogic.change_2D_array_in_1D_array(was_play_board), GameLogic.player_x):
            return "Player X won!"
        elif GameLogic.check_winner(GameLogic.change_2D_array_in_1D_array(was_play_board), GameLogic.player_o):
            return "Player O won!"
        elif Player.number_of_turns == 9:
            return "Draw!"
        else:
            return "Whatever, we broke down."  # todo exception handling

    @staticmethod
    def who_shall_start():
        print("Hello, and welcome to Alex TicTacToe Game!\nWho shall start the game? Please enter either 'x' or 'o'.")

    @staticmethod
    def choose_starting_player():
        try:
            GameLogic.who_shall_start()
            this_is_the_starting_player = input()[0]

            if this_is_the_starting_player == 'x':
                Player.itsTheTurnOfPlayerX = True
                print(f"Player-{this_is_the_starting_player} starts.")
            elif this_is_the_starting_player == 'o':
                Player.itsTheTurnOfPlayerX = False
                print(f"Player-{this_is_the_starting_player} starts.")
            else:
                raise ValueError("Please insert either 'x' or 'o'.")
        except Exception as e:
            print(f"Error: {e}")  # new input advice

    @staticmethod
    def change_player():
        Player.itsTheTurnOfPlayerX = not Player.itsTheTurnOfPlayerX

    @staticmethod
    def the_game():
        GameLogic.choose_starting_player()
        while GameLogic.game_on(GameLogic.play_board):
            GameLogic.show_the_field()
            GameLogic.a_player_manipulates_the_board()
            GameLogic.change_player()
            Player.number_of_turns += 1
        print(GameLogic.who_won(GameLogic.play_board))

GameLogic.the_game()
