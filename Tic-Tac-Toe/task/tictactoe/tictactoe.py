o_turn = win_trigger = False
turn_count = 0
cells_matrix = [[" " for j in range(3)] for i in range(3)]


def show():
    global cells_matrix
    print(f"""---------
| {cells_matrix[0][0]} {cells_matrix[0][1]} {cells_matrix[0][2]} |
| {cells_matrix[1][0]} {cells_matrix[1][1]} {cells_matrix[1][2]} |
| {cells_matrix[2][0]} {cells_matrix[2][1]} {cells_matrix[2][2]} |
---------""")


def coord_convert():
    global cells_matrix
    global o_turn, turn_count
    try:
        cor_str = input("Enter the coordinates: ")
        cor_i = int(cor_str.split(" ")[0])
        cor_j = int(cor_str.split(" ")[1])
        if 0 < cor_i < 4 and 0 < cor_j < 4:
            if cells_matrix[3-cor_j][cor_i - 1] == " ":
                if not o_turn:
                    cells_matrix[3 - cor_j][cor_i - 1] = "X"
                    o_turn = True
                    show()
                else:
                    cells_matrix[3 - cor_j][cor_i - 1] = "O"
                    o_turn = False
                    show()
                turn_count += 1
            else:
                print("This cell is occupied! Choose another one!")
                coord_convert()
        else:
            print("Coordinates should be from 1 to 3!")
            coord_convert()
    except ValueError:
        print("You should enter numbers!")
        coord_convert()


def win_check(letter):
    global win_trigger
    win_combination = [ [[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],
                        [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]],
                        [[0,0],[1,1],[2,2]], [[0,2],[1,1],[2,0]] ]

    for i in range(8):
        if cells_matrix[win_combination[i][0][0]][win_combination[i][0][1]] ==\
                cells_matrix[win_combination[i][1][0]][win_combination[i][1][1]] ==\
                cells_matrix[win_combination[i][2][0]][win_combination[i][2][1]] == letter:
            print(f"{letter} wins")
            win_trigger = True
            return True


show()


while True:
    if not win_check("X") and not win_check("O") and not turn_count == 9:
        coord_convert()
    else:
        if turn_count == 9 and not win_trigger:
            print("Draw")
        break
