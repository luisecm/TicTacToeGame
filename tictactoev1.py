values = []
l = 0
contador_o = 0
contador_x = 0
contador_spaces = 0
coordinates = []
mapped_coordinates_x = 0
mapped_coordinates_y = 0
winner_x = False
winner_o = False
latest_player = ' '
turns = 0


def print_table():
    global values
    print("---------")
    print("|" + " " + values[0][0] + " " + values[0][1] + " " + values[0][2] + " |")
    print("|" + " " + values[1][0] + " " + values[1][1] + " " + values[1][2] + " |")
    print("|" + " " + values[2][0] + " " + values[2][1] + " " + values[2][2] + " |")
    print("---------")


def begin_game():
    global cells
    global values
    global l
    cells = "         "
    for i in range(3):
        for k in range(3):
            values.append([])
            values[i].append([])
            values[i][k] = cells[l]
            l += 1


def fill_table_values():
    global contador_o
    global contador_x
    global contador_spaces
    global values
    for z in range(3):
        for y in range(3):
            if values[z][y] == 'O':
                contador_o += 1
            elif values[z][y] == 'X':
                contador_x += 1
            elif values[z][y] == ' ':
                contador_spaces += 1


def next_move():
    global coordinates
    global mapped_coordinates_x
    global mapped_coordinates_y
    user_coordinates = input("Enter the coordinates:")
    coordinates = user_coordinates.split(" ")
    analyze_user_input_x()


def analyze_user_input_x():
    global coordinates
    if int(coordinates[0]) > 3:
        print("Coordinates should be from 1 to 3!")
        next_move()
    elif int(coordinates[0]) == 1 or int(coordinates[0]) == 2 or int(coordinates[0]) == 3:
        analyze_user_input_y()
    else:
        print("You should enter numbers!")
        next_move()


def analyze_user_input_y():
    global coordinates
    if int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        next_move()
    elif int(coordinates[1]) == 1 or int(coordinates[1]) == 2 or int(coordinates[1]) == 3:
        map_coords()
    else:
        print("You should enter numbers!")
        next_move()


def map_coords():
    global coordinates
    global mapped_coordinates_x
    global mapped_coordinates_y
    if coordinates[0] == '1' and coordinates[1] == '3':
        mapped_coordinates_x = 0
        mapped_coordinates_y = 0
    elif coordinates[0] == '2' and coordinates[1] == '3':
        mapped_coordinates_x = 0
        mapped_coordinates_y = 1
    elif coordinates[0] == '3' and coordinates[1] == '3':
        mapped_coordinates_x = 0
        mapped_coordinates_y = 2
    elif coordinates[0] == '1' and coordinates[1] == '2':
        mapped_coordinates_x = 1
        mapped_coordinates_y = 0
    elif coordinates[0] == '2' and coordinates[1] == '2':
        mapped_coordinates_x = 1
        mapped_coordinates_y = 1
    elif coordinates[0] == '3' and coordinates[1] == '2':
        mapped_coordinates_x = 1
        mapped_coordinates_y = 2
    elif coordinates[0] == '1' and coordinates[1] == '1':
        mapped_coordinates_x = 2
        mapped_coordinates_y = 0
    elif coordinates[0] == '2' and coordinates[1] == '1':
        mapped_coordinates_x = 2
        mapped_coordinates_y = 1
    elif coordinates[0] == '3' and coordinates[1] == '1':
        mapped_coordinates_x = 2
        mapped_coordinates_y = 2
    analyze_results()


def analyze_results():
    global mapped_coordinates_x
    global mapped_coordinates_y
    global coordinates
    global values
    global latest_player
    if values[mapped_coordinates_x][mapped_coordinates_y] == 'X':
        print("This cell is occupied! Choose another one!")
        next_move()
    elif values[mapped_coordinates_x][mapped_coordinates_y] == 'O':
        print("This cell is occupied! Choose another one!")
        next_move()
    elif values[mapped_coordinates_x][mapped_coordinates_y] == ' ':
        if latest_player == ' ':
            values[mapped_coordinates_x][mapped_coordinates_y] = 'X'
            latest_player = 'X'
            print_table()
            look_for_winner()
        elif latest_player == 'X':
            values[mapped_coordinates_x][mapped_coordinates_y] = 'O'
            latest_player = 'O'
            print_table()
            look_for_winner()
        elif latest_player == 'O':
            values[mapped_coordinates_x][mapped_coordinates_y] = 'X'
            latest_player = 'X'
            print_table()
            look_for_winner()


def o_wins_horizontal():
    global winner_x
    global winner_o
    if values[0][0] == 'O' and values[0][1] == 'O' and values[0][2] == 'O':
        winner_o = True
    elif values[1][0] == 'O' and values[1][1] == 'O' and values[1][2] == 'O':
        winner_o = True
    elif values[2][0] == 'O' and values[2][1] == 'O' and values[2][2] == 'O':
        winner_o = True


def x_wins_horizontal():
    global winner_x
    if values[0][0] == 'X' and values[0][1] == 'X' and values[0][2] == 'X':
        winner_x = True
    elif values[1][0] == 'X' and values[1][1] == 'X' and values[1][2] == 'X':
        winner_x = True
    elif values[2][0] == 'X' and values[2][1] == 'X' and values[2][2] == 'X':
        winner_x = True


def o_wins_vertical():
    global winner_o
    if values[0][0] == 'O' and values[1][0] == 'O' and values[2][0] == 'O':
        winner_o = True
    elif values[0][1] == 'O' and values[1][1] == 'O' and values[2][1] == 'O':
        winner_o = True
    elif values[0][2] == 'O' and values[1][2] == 'O' and values[2][2] == 'O':
        winner_o = True


def x_wins_vertical():
    global winner_x
    if values[0][0] == 'X' and values[1][0] == 'X' and values[2][0] == 'X':
        winner_x = True
    elif values[0][1] == 'X' and values[1][1] == 'X' and values[2][1] == 'X':
        winner_x = True
    elif values[0][2] == 'X' and values[1][2] == 'X' and values[2][2] == 'X':
        winner_x = True


def win_diagonal_o():
    global winner_o
    if values[0][0] == 'O' and values[1][1] == 'O' and values[2][2] == 'O':
        winner_o = True
    elif values[2][0] == 'O' and values[1][1] == 'O' and values[0][2] == 'O':
        winner_o = True


def win_diagonal_x():
    global winner_x
    if values[0][0] == 'X' and values[1][1] == 'X' and values[2][2] == 'X':
        winner_x = True
    elif values[2][0] == 'X' and values[1][1] == 'X' and values[0][2] == 'X':
        winner_x = True


def look_for_winner():
    global contador_spaces
    while contador_spaces > 0:
        o_wins_horizontal()
        if winner_x:
            print("X wins")
            break
        else:
            x_wins_horizontal()
            if winner_o:
                print("O wins")
                break
            else:
                x_wins_vertical()
                if winner_x:
                    print("X wins")
                    break
                else:
                    o_wins_vertical()
                    if winner_o:
                        print("O wins")
                        break
                    else:
                        win_diagonal_x()
                        if winner_x:
                            print("X wins")
                            break
                        else:
                            win_diagonal_o()
                            if winner_o:
                                print("O wins")
                                break
                            else:
                                if turns == 9:
                                    print("Draw")
                                    break
                                else:
                                    fill_table_values()
                                    next_move()



def main():
    begin_game()
    print_table()
    fill_table_values()
    next_move()


main()











