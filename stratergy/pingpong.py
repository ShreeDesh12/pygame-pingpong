from constants.screen import SCREEN_WIDTH
from objects.ball import Ball

MARGIN_OF_ERROR = 5


def winning_strategy_for_right_player(ball: Ball):
    ball_boundary = ball.get_position()
    if (
        ball_boundary["start_x"] <= MARGIN_OF_ERROR
        or ball_boundary["end_x"] <= MARGIN_OF_ERROR
    ):
        return True

    return False


def winning_strategy_for_left_player(ball: Ball):
    ball_boundary = ball.get_position()
    if (
        ball_boundary["start_x"] >= SCREEN_WIDTH - MARGIN_OF_ERROR
        or ball_boundary["end_x"] >= SCREEN_WIDTH - MARGIN_OF_ERROR
    ):
        return True

    return False
