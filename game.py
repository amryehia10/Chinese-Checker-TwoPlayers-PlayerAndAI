import pygame
from alpha_beta import startAlphaBetaAgent
from board_draw import *
from helpers import *
from pygame.locals import *
from board import *
import math


def game(chosen_diff=EASY_MODE):
    import menu

    pygame.display.quit()

    window = init_board_window(difficulty_settings.get(chosen_diff).get('title'))
    board = fill_board()
    #board = build_win_board()
    player_turn = 1
    human_player = False
    clicked_cell = None
    available_moves = []
    cells = []
    start_game = True
    found_winner = False

    clock = pygame.time.Clock()
    while start_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_game = False
            if not found_winner and event.type == pygame.MOUSEBUTTONDOWN:
                clicked_point = pygame.mouse.get_pos()
                for row in range(len(cells)):
                    breakit = False
                    for col in range(len(cells[0])):
                        if cells[row][col].collidepoint(clicked_point):
                            if row % 2 == 0:
                                cell = [row, col*2]
                            else:
                                cell = [row, col*2+1]
                            cellValue = board[cell[0]][cell[1]]

                            if cellValue == player_turn or (clicked_cell and cellValue == 0):
                                if clicked_cell == cell:
                                    clicked_cell = None
                                elif cell in available_moves:
                                    move(board, clicked_cell, cell)
                                    clicked_cell = None
                                    human_player = True
                                elif board[cell[0]][cell[1]] > 0:
                                    clicked_cell = cell
                            breakit = True
                            break
                    if breakit:
                        break
                board[row, col*2] != -1

        # DRAW PHASE
        window.fill(BACKGROUND_COLOR)
        button(window, "back", WINDOW_WIDTH - 475, WINDOW_HEIGHT - 50, 80, 40, DARK_COLOR,
               LIGHT_COLOR, menu.menu)

        if winner_player(board, window) == False:
            message(('Human' if player_turn == 1 else 'Bot') + '\'s turn', WINDOW_WIDTH - (350 if player_turn == 1 else 325), WINDOW_HEIGHT - 100, 50, players_colors.get(player_turn),
                    window)
        else:
            found_winner = True

        if clicked_cell:
            available_moves = get_available_moves(board, clicked_cell)
        else:
            available_moves = []
        cells = draw_board(board, window, clicked_cell, available_moves)
        pygame.display.flip()

        # AI PHASE
        if not found_winner and player_turn == 4:
            depth = difficulty_settings.get(chosen_diff).get('depth')
            _, best_move = startAlphaBetaAgent(board, depth, player_turn)
            move(board, best_move[0], best_move[1])
            player_turn = 1
            human_player = False
        elif human_player:
            player_turn = 4

        clock.tick(20)


def winner_player(board, window):
    first_player = True
    second_player = True
    playersSet = build_players_sets()
    p1, p2, p3, p4, p5, p6 = playersSet

    for i in range(len(p1)):
        if board[p1[i][0]][p1[i][1]] != 4:
            second_player = False
            break
    for i in range(len(p4)):
        if board[p4[i][0]][p4[i][1]] != 1:
            first_player = False
            break

    if second_player == True:
        message('Bot won!', WINDOW_WIDTH - 315,
                WINDOW_HEIGHT - 100, 50, players_colors.get(4), window)
        return True

    elif first_player == True:
        message('Player won!', WINDOW_WIDTH - 330,
                WINDOW_HEIGHT - 100, 50, players_colors.get(1), window)
        return True
    else:
        return False


if __name__ == "__main__":
    game()
