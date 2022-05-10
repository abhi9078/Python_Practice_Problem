

def print_board(xState, zState):
    """
    function for tic-tac-toe game
    :param xState: first player turn
    :param zState: second player turn
    :return: print out the UI for match
    """
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


def sum_func(a, b, c):
    return a + b + c


def check_win(x_state, z_state):
    """
    function for check winner
    :param x_state: for first player
    :param z_state: for second player
    :return: check for winning
    """
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum_func(x_state[win[0]], x_state[win[1]], x_state[win[2]]) == 3:
            print("Player 1 Won the match")
            return 1
        elif sum_func(z_state[win[0]], z_state[win[1]], z_state[win[2]]) == 3:
            print("Player 2 Won the match")
            return 0
        # else:
        #     print("Match draw")
        #     return -2
    return -1


if __name__ == "__main__":
    player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while True:
        print_board(player1, player2)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            player1[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            player2[value] = 1
        winner = check_win(player1, player2)
        if winner != -1:
            print("Match over")
            break

        turn = 1 - turn
