board = [1,2,3,4,5,6,7,8,9] # board
turn = 1 # counter

already_used = []
def Check_Tie(): # ha megtelik a lista vege
    if turn == 10:
        Print_Board()
        print("the game is a tie")
        
        exit()
    return None
def Replay():
    answer = input('Do you want a rematch? Y/N')
    if answer == "Y" or "y" :
        Move()
    else: 
        quit()


def check_Win():
# combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 4], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#Print_Board()
    
    if board[0] =='X' and board[1] =='X' and board[2] =='X':
        print('X wins')
        Replay()
    if board[3] =='X' and board[3] =='X' and board[5] =='X':
        print('X wins')
        Replay()
    if board[6] =='X' and board[7] =='X' and board[8] =='X':
        print('X wins')
        Replay()
    if board[0] =='X' and board[3] =='X' and board[4] =='X':
        print('X wins')
        Replay()
    if board[1] =='X' and board[4] =='X' and board[7] =='X':
        print('X wins')
        Replay()
    if board[2] =='X' and board[5] =='X' and board[8] =='X':
        print('X wins')
        Replay()
    if board[0] =='X' and board[4] =='X' and board[8] =='X':
        print('X wins')
        Replay()
    if board[2] =='X' and board[4] =='X' and board[6] =='X':
        print('X wins')
        Replay()
    if board[0] =='O' and board[1] =='O' and board[2] =='O':
        print('O wins')
        Replay()
    if board[3] =='O' and board[4] =='O' and board[5] =='O':
        print('O wins')
        Replay()
    if board[6] =='O' and board[7] =='O' and board[8] =='O':
        print('O wins')
        Replay()
    if board[0] =='O' and board[3] =='O' and board[6] =='O':
        print('O wins')
        Replay()
    if board[1] =='O' and board[4] =='O' and board[7] =='O':
        print('O wins')
        Replay()
    if board[2] =='O' and board[5] =='O' and board[8] =='O':
        print('O wins')
        Replay()
    if board[0] =='O' and board[4] =='O' and board[8] =='O':
        print('O wins')
        Replay()
    if board[2] =='O' and board[4] =='O' and board[6] =='O':
        print('O wins')
        Replay()

def Print_Board():
    print(board[0] ,' | ' , board[1] , ' | ', board[2])
    print("--------------")
    print(board[3], ' | ' , board[4] , ' | ' , board[5])
    print("---------------")
    print(board[6], ' | ', board[7] , ' | ', board[8])
def placing():
    pass


def setup_Board():
    
    
def Player_Turn(a):  # jatekos kor
    global turn
    if turn % 2 != 0: 
        board[a-1] = "X"
        turn += 1
    else: 
        board[a-1] = "O"
        turn += 1
    return None    

def Move():    
    setup_Board()
    while True:
        Print_Board()
        try:
            a =int(input("Where do you want to put ?"))
            if a in already_used:
                print("That place is occupied. Try again") 
            elif  0 < a < 10 :
                already_used.append(a)
                print(already_used)
                
                Player_Turn(a)
                check_Win()
                Check_Tie()
                continue
            else:
                print("That's out of range. Try again.")

        except ValueError:
            print("That's not a number")
Move()