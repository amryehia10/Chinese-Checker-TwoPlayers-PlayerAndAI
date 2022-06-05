from copy import copy
import math
from board import *


def startAlphaBetaAgent(board, depth, player_turn, ai_player=4):
    return alphabeta(board, depth, player_turn, ai_player, -1000, 1000)


def alphabeta(board, depth, player_turn, ai_player, alpha, beta):
    p1Pieces = getPlayerPieces(board, 1)
    p4Pieces = getPlayerPieces(board, 4)

    # base condition when depth is 0
    if depth == 0:
        board_score = calculate_board_score(
            player_turn, ai_player, p1Pieces, p4Pieces)
        return board_score, None

    # get valid_moves
    all_valid_moves = get_all_posible_moves(
        board, p1Pieces if player_turn == 1 else p4Pieces)

    scores = []
    moves = []
    # iterate over valid moves and call alpha beta
    for valid_move in all_valid_moves:
        board_copy = copy(board)
        move(board_copy, valid_move[0], valid_move[1])

        next_player = 4 if player_turn == 1 else 1

        score, _ = alphabeta(board_copy, depth-1,
                             next_player, ai_player, alpha, beta)
        scores.append(score)
        moves.append(valid_move)

        # check if current player is ai_player: change beta or alpha accodingly
        if player_turn == ai_player:
            alpha = max(score, alpha)
            if beta <= alpha:
                break
        else:
            beta = min(score, beta)
            if beta <= alpha:
                break

    if len(scores) == 0:
        return

    final_score_index = scores.index(
        max(scores) if player_turn == ai_player else min(scores))
    return scores[final_score_index], moves[final_score_index]


def get_all_posible_moves(board, pieces):
    all_moves = []
    for piece in pieces:
        distenations_cells = get_available_moves(board, piece)
        for dist_cell in distenations_cells:
            all_moves.append([piece, dist_cell])

    return all_moves


def calculate_board_score(board, player_turn, p1Pieces, p4Pieces):
    p4Targets, p2, p3, p1Targets, p5, p6 = build_players_sets()

    p1_avg_dist = getAvgDistance(p1Pieces, p1Targets)
    p4_avg_dist = getAvgDistance(p4Pieces, p4Targets)

    VD = getVerticalDisplacement(
        player_turn, p1_avg_dist, p4_avg_dist)

    HD = getHorizentalDisplacement(
        p1Pieces if player_turn == 1 else p4Pieces)

    HDW = 0.2

    return VD + HD*HDW


def getHorizentalDisplacement(pieces):
    total_dist = 0
    for [_, j] in pieces:
        total_dist += abs(j - 12)
    return 1 / (total_dist / len(pieces))


def getVerticalDisplacement(player_turn, p1_avg_dist, p4_avg_dist):
    if player_turn == 1:
        return p4_avg_dist - p1_avg_dist
    if player_turn == 4:
        return p1_avg_dist - p4_avg_dist


def getPlayerPieces(board, player):
    pieces = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                pieces.append([i, j])
    return pieces


def getAvgDistance(pieces, targets):
    dis_target = chooseDisplacemntTargetCell(pieces, targets)

    total_dist = 0
    for p in pieces:
        [x, y] = p
        [tx, ty] = dis_target

        total_dist += math.sqrt(((tx - x) ** 2) + ((ty - y) ** 2))

    return total_dist / len(pieces)


def chooseDisplacemntTargetCell(pieces, targets):
    disTarget = targets[0]

    for target in targets:
        if target not in pieces:
            disTarget = target

    return disTarget
