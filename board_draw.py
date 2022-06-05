from turtle import back
import pygame
from board import *

# -1 =background or invalid space
BACKGROUND_COLOR = (255, 229, 204)
EMPTY_CELL = (192, 192, 192)
HUMAN_COLOR = (255, 51, 51)
AI_COLOR = (0, 0, 153)

# HIGHLIGHT
HIGHLIGHT = (255, 255, 255, 80)

X_WINDOW_PADDING = 15
Y_WINDOW_PADDING = 15
X_CELL_MARGIN = 6
Y_CELL_MARGIN = 1

CIRCLE_RADIUS = 15
CIRCLE_DIAMETER = 2 * CIRCLE_RADIUS
BOARD_BOTTOM_MARGIN = 200

WINDOW_WIDTH = (X_WINDOW_PADDING * 2) + \
    (CIRCLE_DIAMETER * 13) + (X_CELL_MARGIN * 12)
WINDOW_HEIGHT = (Y_WINDOW_PADDING * 2) + \
    (CIRCLE_DIAMETER * 17) + (Y_CELL_MARGIN * 16) + BOARD_BOTTOM_MARGIN


players_colors = {
    -1: BACKGROUND_COLOR,
    0: EMPTY_CELL,
    1: HUMAN_COLOR,
    4: AI_COLOR,

}


def init_board_window(title='CHINESE-CHECKERS'):
    pygame.init()
    window = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(title)
    return window


def draw_board(board, window, clickedCell=None, availableMoves=None):
    if availableMoves is None:
        availableMoves = []
    cells = []
    playersSet = build_players_sets()
    p1, p2, p3, p4, p5, p6 = playersSet

    y_coord = Y_WINDOW_PADDING + CIRCLE_RADIUS

    for row in range(0, 17):
        x_even_rows = X_WINDOW_PADDING + CIRCLE_RADIUS
        x_odd_rows = int(X_WINDOW_PADDING +
                         CIRCLE_DIAMETER + (X_CELL_MARGIN / 2))
        rowCells = []
        for col in range(0, 13):
            if row % 2 == 0:
                board_value = board[row][col * 2]
                cell = draw_cell(board_value, window,
                                 x_even_rows, y_coord, clickedCell and clickedCell == [row, col*2])
                # draw target cells
                if [row, col*2] in p1:
                    pygame.draw.circle(window, players_colors.get(
                        4), (x_even_rows, y_coord), CIRCLE_RADIUS, 1)
                if [row, col*2] in p4:
                    pygame.draw.circle(window, players_colors.get(
                        1), (x_even_rows, y_coord), CIRCLE_RADIUS, 1)

                x_even_rows = x_even_rows + CIRCLE_DIAMETER + X_CELL_MARGIN
            elif row % 2 != 0 and col != 12:
                board_value = board[row][col * 2 + 1]
                cell = draw_cell(board_value, window,
                                 x_odd_rows, y_coord, clickedCell and clickedCell == [row, col*2+1])

                # draw target cells
                if [row, col*2+1] in p1:
                    pygame.draw.circle(window, players_colors.get(
                        4), (x_odd_rows, y_coord), CIRCLE_RADIUS, 1)
                if [row, col*2+1] in p4:
                    pygame.draw.circle(window, players_colors.get(
                        1), (x_odd_rows, y_coord), CIRCLE_RADIUS, 1)

                x_odd_rows = x_odd_rows + CIRCLE_DIAMETER + X_CELL_MARGIN
            rowCells.append(cell)
        y_coord = y_coord + CIRCLE_DIAMETER + Y_CELL_MARGIN
        cells.append(rowCells)

    for [i, j] in availableMoves:
        j = int(j/2)

        y_circle = Y_WINDOW_PADDING + CIRCLE_RADIUS + \
            i * (CIRCLE_DIAMETER + Y_CELL_MARGIN)

        if i % 2 == 0:
            x_circle = X_WINDOW_PADDING + CIRCLE_RADIUS + j * (CIRCLE_DIAMETER +
                                                               X_CELL_MARGIN)
        else:
            x_circle = int(X_WINDOW_PADDING +
                           CIRCLE_DIAMETER + (X_CELL_MARGIN / 2)) + j * (CIRCLE_DIAMETER + X_CELL_MARGIN)

        outline = pygame.image.load('outline.png')
        outline = pygame.transform.scale(
            outline, (CIRCLE_DIAMETER+4, CIRCLE_DIAMETER+4))

        rotate_angle = pygame.time.get_ticks() % 360
        outline, outlineRect = rotate_center(
            outline, rotate_angle, x_circle, y_circle)
        window.blit(outline, outlineRect)
    return cells


def rotate_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect


def draw_cell(board_value, window, cx, cy, highlight=False):
    color = players_colors.get(board_value)
    cell = pygame.draw.circle(window, color, (cx, cy), CIRCLE_RADIUS, 0)

    if highlight:
        surface = pygame.Surface(
            (CIRCLE_DIAMETER, CIRCLE_DIAMETER), pygame.SRCALPHA)
        pygame.draw.circle(
            surface, HIGHLIGHT, (CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS, 0)
        window.blit(surface, (cx-CIRCLE_RADIUS, cy-CIRCLE_RADIUS))

    return cell
