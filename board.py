import numpy

moves_index = [[-1, -1], [-1, 1], [0, 2], [1, 1], [1, -1], [0, -2]]


def build_empty_board():
    board = numpy.ones((17, 25))
    board *= -1
    board_index = [1, 2, 3, 4, 13, 12, 11, 10, 9]
    marble_no = 9
    for i in range(marble_no):
        j = 12
        flag = True
        while board_index[i] > 0:
            if (i % 2 == 0) and flag:
                flag = False
                board[i][j] = board[16 - i][j] = 0
                board_index[i] -= 1
            else:
                j -= 1
                board[i][j] = board[i][24 - j] = board[16 -
                                                       i][j] = board[16 - i][24 - j] = 0
                board_index[i] -= 2
            j -= 1
    return board


def build_board():
    empty_board = build_empty_board()
    return empty_board


def build_player_set(triRoot, isTriLookUp):
    player_set = [triRoot]
    for rowCounter in range(2, 5):
        row = triRoot[0] + rowCounter - \
              1 if isTriLookUp else triRoot[0] - rowCounter + 1
        firstCol = triRoot[1] - (rowCounter - 1)
        lastCol = triRoot[1] + (rowCounter - 1)
        for col in range(firstCol, lastCol + 1, 2):
            player_set.append([row, col])

    return player_set


def build_players_sets():
    players_sets = []
    for i in range(1, 6 + 1):
        players = build_player_set(
            get_player_set_root(i), is_player_set_tri_up(i))

        players_sets.append(players)

    return players_sets


def get_player_set_root(player_number):
    sets_roots = {
        1: [0, 12],
        2: [7, 21],
        3: [9, 21],
        4: [16, 12],
        5: [9, 3],
        6: [7, 3],
    }

    return sets_roots.get(player_number)


def is_player_set_tri_up(player_number):
    return True if player_number in [1, 3, 5] else False


def put_players_on_board(playerCount=2):
    empty_board = build_board()
    playersSet = build_players_sets()
    p1, p2, p3, p4, p5, p6 = playersSet

    if playerCount >= 2:
        for j in range(len(p1)):
            empty_board[p1[j][0]][p1[j][1]] = 1
        for j in range(len(p4)):
            empty_board[p4[j][0]][p4[j][1]] = 4

    return empty_board


def fill_board():
    filled_board = put_players_on_board(2)
    return filled_board


def get_available_moves(board, cell_coordinates):
    validMove_index = []
    for i in range(len(moves_index)):
        x_coordinates = cell_coordinates[0] + moves_index[i][0]
        y_coordinates = cell_coordinates[1] + moves_index[i][1]
        if [x_coordinates, y_coordinates] not in moves_index:
            if -1 < x_coordinates < 17 and -1 < y_coordinates < 25:
                if board[x_coordinates][y_coordinates] == 0:
                    validMove_index.append([x_coordinates, y_coordinates])
                elif board[x_coordinates][y_coordinates] > 0:
                    check_path(board, moves_index[i], x_coordinates, y_coordinates, validMove_index)

    return validMove_index


def check_path(board, path_coordinates, x, y, moves_array):
    x2 = x + path_coordinates[0]
    y2 = y + path_coordinates[1]
    new_coordinates = [x2, y2]
    if new_coordinates not in moves_array:
        if -1 < x2 < 17 and -1 < y2 < 25:
            if board[x2][y2] == 0:
                moves_array.append(new_coordinates)
                for j in range(len(moves_index)):
                    x3 = x2 + moves_index[j][0]
                    y3 = y2 + moves_index[j][1]
                    if [x3, y3] not in moves_array:
                        if -1 < x3 < 17 and -1 < y3 < 25:
                            if board[x3][y3] > 0:
                                check_path(board, moves_index[j], x3, y3, moves_array)


def move(board, player_pos, target):
    temp = board[player_pos[0]][player_pos[1]]
    board[player_pos[0]][player_pos[1]] = 0
    board[target[0]][target[1]] = temp


def build_win_board():
    import numpy as np

    board = np.zeros((17, 25))

    board[:][:] = -1

    board[0][12] = 4
    board[1][11] = 4
    board[1][13] = 4
    board[2][10] = 4
    board[2][12] = 4
    board[2][14] = 4
    board[3][9] = 4
    board[3][11] = 4
    board[3][13] = 4
    board[3][15] = 0

    board[4][18] = 0
    board[4][20] = 0
    board[4][22] = 0
    board[4][24] = 0
    board[5][19] = 0
    board[5][21] = 0
    board[5][23] = 0
    board[6][20] = 0
    board[6][22] = 0
    board[7][21] = 0

    board[9][21] = 0
    board[10][20] = 0
    board[10][22] = 0
    board[11][19] = 0
    board[11][21] = 0
    board[11][23] = 0
    board[12][18] = 0
    board[12][20] = 0
    board[12][22] = 0
    board[12][24] = 0

    board[13][9] = 0
    board[13][11] = 1
    board[13][13] = 1
    board[13][15] = 1
    board[14][10] = 1
    board[14][12] = 1
    board[14][14] = 1
    board[15][11] = 1
    board[15][13] = 1
    board[16][12] = 1

    board[9][3] = 0
    board[10][2] = 0
    board[10][4] = 0
    board[11][1] = 0
    board[11][3] = 0
    board[11][0] = 0
    board[12][0] = 0
    board[12][2] = 0
    board[12][4] = 0
    board[12][6] = 0

    board[4][0] = 0
    board[4][2] = 0
    board[4][4] = 0
    board[4][6] = 0
    board[5][1] = 0
    board[5][3] = 0
    board[5][5] = 0
    board[6][2] = 0
    board[6][4] = 0
    board[7][3] = 0

    board[4][8] = 0
    board[4][10] = 0
    board[4][12] = 0
    board[4][14] = 0
    board[4][16] = 4

    board[5][7] = 0
    board[5][9] = 0
    board[5][11] = 0
    board[5][13] = 0
    board[5][15] = 0
    board[5][17] = 0

    board[6][6] = 0
    board[6][8] = 0
    board[6][10] = 0
    board[6][12] = 0
    board[6][14] = 0
    board[6][16] = 0
    board[6][18] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[8][4] = 0
    board[8][6] = 0
    board[8][8] = 0
    board[8][10] = 0
    board[8][12] = 0
    board[8][14] = 0
    board[8][16] = 0
    board[8][18] = 0
    board[8][20] = 0

    board[9][5] = 0
    board[9][7] = 0
    board[9][9] = 0
    board[9][11] = 0
    board[9][13] = 0
    board[9][15] = 0
    board[9][17] = 0
    board[9][19] = 0

    board[10][6] = 0
    board[10][8] = 0
    board[10][10] = 0
    board[10][12] = 0
    board[10][14] = 0
    board[10][16] = 0
    board[10][18] = 0

    board[11][5] = 0
    board[11][7] = 0
    board[11][9] = 0
    board[11][11] = 0
    board[11][13] = 0
    board[11][15] = 0
    board[11][17] = 0

    board[12][8] = 0
    board[12][10] = 1
    board[12][12] = 0
    board[12][14] = 0
    board[12][16] = 0

    return board

