"""This is the popular noughts & crosses game implemented using 2d lists"""


def display_banner():
    print("XOXOXOXOXOXOXOOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
    print("O                                           X")
    print("X           Noughts & Crosses               O")
    print("O                                           X")
    print("XOXOXOXOXOXOXOOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
    print()


display_banner()
#  define the grid of 2D arrays (3 X 3)
grid = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

# above grid represents sketch below and indexes
#  grid = [["[0][0]", "[0][1]", "[0][2]"],
#          ["[1][0]", "[1][1]", "[1][2]"],
#          ["[2][0]", "[2][1]", "[2][2]"]]


def display_grid(grid):
    print(grid[0][0] + "|"+grid[0][1] + "|"+grid[0][2])
    print("-----")
    print(grid[1][0] + "|"+grid[1][1] + "|"+grid[1][2])
    print("-----")
    print(grid[2][0] + "|"+grid[2][1] + "|"+grid[2][2])
    print()


display_grid(grid)


def player_X():
    print("Player X, Its your turn")
    row = int(input("enter row index: 0, 1 or 2:  "))
    column = int(input("enter column index: 0, 1 or 2:  "))

    while grid[row][column] != " ":
        print("Cell taken...Try again!")
        row = int(input("enter row index: 0, 1 or 2:  "))
        column = int(input("enter column index: 0, 1 or 2:  "))

    grid[row][column] = "X"
    display_grid(grid)


def player_O():
    print("Player O, Its your turn")
    row = int(input("enter row index: 0, 1 or 2:  "))
    column = int(input("enter column index: 0, 1 or 2:  "))

    while grid[row][column] != " ":
        print("Cell taken...Try again!")
        row = int(input("enter row index: 0, 1 or 2:  "))
        column = int(input("enter column index: 0, 1 or 2:  "))

    grid[row][column] = "O"
    display_grid(grid)


def check_winner(grid):
    # CHECK FOR ROW 0
    if grid[0][0] == grid[0][1] == grid[0][2] == "X":
        print("Three Xs in a row. Player X wins!!!")
        exit()
    elif grid[0][0] == grid[0][1] == grid[0][2] == "O":
        print("Three Os in a row. Player O wins!!!")
        exit()
    # CHECK FOR ROW 1
    elif grid[1][0] == grid[1][1] == grid[1][2] == "X":
        print("Three Xs in a row. Player X wins!!!")
        exit()
    elif grid[1][0] == grid[1][1] == grid[1][2] == "O":
        print("Three Os in a row. Player O wins!!!")
        exit()
    # CHECK FOR ROW 2
    elif grid[2][0] == grid[2][1] == grid[2][2] == "X":
        print("Three Xs in a row. Player X wins!!!")
        exit()
    elif grid[2][0] == grid[2][1] == grid[2][2] == "O":
        print("Three Os in a row. Player O wins!!!")
        exit()
    # CHECK FOR COLUMN 0
    elif grid[0][0] == grid[1][0] == grid[2][0] == "X":
        print("Three Xs in a row. Player X wins!!!")
        exit()
    elif grid[0][0] == grid[1][0] == grid[2][0] == "O":
        print("Three Os in a row. Player O wins!!!")
        exit()
    # CHECK FOR COLUMN 1
    elif grid[0][1] == grid[1][1] == grid[2][1] == "X":
        print("Three Xs in a row. Player X wins!!!")
        exit()
    elif grid[0][1] == grid[1][1] == grid[2][1] == "O":
        print("Three Os in a row. Player O wins!!!")
        exit()
    # CHECK FOR COLUMN 2
    elif grid[0][2] == grid[1][2] == grid[2][2] == "X":
        print("Three Xs in a row. Player X wins!!!")
        exit()
    elif grid[0][2] == grid[1][2] == grid[2][2] == "O":
        print("Three Os in a row. Player O wins!!!")
        exit()
    # CHECK FOR DIAGONAL 1 (LEFT-RIGHT)
    elif grid[0][0] == grid[1][1] == grid[2][2] == "X":
        print("Three Xs in a row diagonally. Player X wins!!!")
        exit()
    elif grid[0][0] == grid[1][1] == grid[2][2] == "O":
        print("Three Os in a row diagonally. Player O wins!!!")
        exit()
    # CHECK FOR DIAGONAL 2 (RIGHT - LEFT)
    elif grid[0][2] == grid[1][1] == grid[2][0] == "X":
        print("Three Xs in a row diagonally. Player X wins!!!")
        exit()
    elif grid[0][2] == grid[1][1] == grid[2][0] == "O":
        print("Three Os in a row diagonally. Player O wins!!!")
        exit()

# An iterative to loop game between Player X and O.
# For each player turn, game checks grid for winner


for i in range(0, 9):
    if i % 2 == 0:
        player_X()
        check_winner(grid)
    else:
        player_O()
        check_winner(grid)
