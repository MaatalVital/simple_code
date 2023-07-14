
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

current_player = 'X'


def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def check_win():

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or \
           board[0][i] == board[1][i] == board[2][i] != ' ':
            return True


    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def make_move():
    while True:
        row = int(input("Выберите номер строки (1-3): ")) - 1
        col = int(input("Выберите номер столбца (1-3): ")) - 1

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player
            break
        else:
            print("Некорректный ход. Попробуйте снова.")


while True:
    display_board()
    make_move()

    if check_win():
        print("Игрок", current_player, "победил!")
        break

    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        print("Ничья!")
        break


    current_player = 'O' if current_player == 'X' else 'X'
