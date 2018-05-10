import os
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn = 1

already_used = []


def x_win():
    os.system('clear')
    print("X won! Well played!")
    Replay()


def o_win():
    os.system('clear')
    print("O won! Well played!")
    Replay()


def Check_Tie():  # ha megtelik a lista vege
    if turn == 10:
        Print_Board()
        print("the game is a tie")
        Replay()


def Replay():  # újra kezdés
    Print_Board()
    answer = input('Do you want a rematch? (Y/N): ')
    answer = answer.lower()
    if 'y' in answer:
        os.system('clear')
        global board
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        global turn
        turn = 1
        global already_used
        already_used = []
        Move()
    else:
        exit()


def check_Win():  # ha a listában lévő kombinációk kijönnek a játék közben, akkor kiírja a wint + meghívja a replayt
    combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in combinations:
        if board[i[0]] == board[i[1]] == board[i[2]] == 'X':
            x_win()
    for i in combinations:
        if board[i[0]] == board[i[1]] == board[i[2]] == 'O':
            o_win()
    

    # if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
    #     x_win()
    # if board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
    #     x_win()
    # if board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
    #     x_win()
    # if board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
    #     x_win()
    # if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
    #     x_win()
    # if board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
    #     x_win()
    # if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
    #     x_win()
    # if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
    #     x_win()
    # if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
    #     o_win()
    # if board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
    #     o_win()
    # if board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
    #     o_win()
    # if board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
    #     o_win()
    # if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
    #     o_win()
    # if board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
    #     o_win()
    # if board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
    #     o_win()
    # if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
    #     o_win


def Print_Board():  # a pálya kinézete
    print(board[0], ' | ', board[1], ' | ', board[2])
    print("--------------")
    print(board[3], ' | ', board[4], ' | ', board[5])
    print("--------------")
    print(board[6], ' | ', board[7], ' | ', board[8])


def Player_Turn(a):  # jatekos kor
    global turn
    if turn % 2 != 0:
        board[a - 1] = "X"
        turn += 1
    else:
        board[a - 1] = "O"
        turn += 1


def Move():     # fő függvény, ide van meghívva az összes mellék függvény
    os.system('clear')
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = 1
    print("Welcome to Tic tac toe!\n")
    while True:
        Print_Board()
        try:
            a = int(input("Where do you want to put ?: "))
            if a in already_used:
                os.system('clear')
                print("That place is occupied. Try again")

            elif 0 < a < 10:
                already_used.append(a)
                print(already_used)

                Player_Turn(a)
                check_Win()
                Check_Tie()
                os.system('clear')
                continue
            else:
                os.system('clear')
                print("That's out of range. Try again.")
        except ValueError:
            print("That's not a number")


Move()
