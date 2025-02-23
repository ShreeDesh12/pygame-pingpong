from constants.ball import BallSpeed
from objects.ball import Ball


def speed_up(ball: Ball):
    x_speed, y_speed = ball.get_speed()
    ball.set_speed(x_speed=x_speed+BallSpeed.POWER_SPEED, y_speed=y_speed+BallSpeed.POWER_SPEED)


def speed_down(ball: Ball):
    x_speed, y_speed = ball.get_speed()
    ball.set_speed(x_speed=x_speed-BallSpeed.POWER_SPEED, y_speed=y_speed-BallSpeed.POWER_SPEED)
