from objects.ball import Ball
from objects.bat import Bat


def autoplay(bat: Bat, ball: Ball, defending_left_side: bool = True):
    ball_position = ball.get_position()
    _, bat_y, _, bat_height = bat.get_bat()

    x_speed, _ = ball.get_speed()

    ball_mid = (ball_position['start_y'] + ball_position['end_y'])//2
    bat_mid = bat_y + (bat_height//2)

    if defending_left_side and x_speed < 0:
        if ball_mid < bat_mid:
            bat.move_up()
        elif ball_mid > bat_mid:
            bat.move_down()

    elif defending_left_side is False and x_speed > 0:
        if ball_mid < bat_mid:
            bat.move_down()

        elif ball_mid > bat_mid:
            bat.move_up()
