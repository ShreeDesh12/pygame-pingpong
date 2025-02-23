import pygame

from constants.ball import BallSpeed, BallDimensions
from constants.power import POWER_TIME, BALL_RADIUS
from objects.ball import Ball
from objects.ball_object import BallObject


class Power:
    def __init__(self, strategy: callable, event: pygame.USEREVENT, ball: BallObject, ball_img: str=None):
        self.power_up_time = None
        self.strategy = strategy
        self.ball_img = ball_img
        self.event = event
        self.ball = ball
        self.powered_up: bool = False
        self._original_ball_character_img = None

    def use(self):
        x_speed, y_speed = self.ball.get_speed()
        x_speed = BallSpeed.X_SPEED+BallSpeed.POWER_SPEED if x_speed > 0 else -BallSpeed.X_SPEED-BallSpeed.POWER_SPEED
        y_speed = BallSpeed.Y_SPEED+BallSpeed.POWER_SPEED if y_speed > 0 else -BallSpeed.Y_SPEED-BallSpeed.POWER_SPEED

        self.ball.set_speed(x_speed=x_speed, y_speed=y_speed)
        self._original_ball_character_img = self.ball.get_character_img()
        self.ball.set_character_img(character_img=self.ball_img)
        self.ball.unset_rotated_img()
        self.power_up_time = pygame.time.get_ticks()
        self.ball.update_radius(radius=BALL_RADIUS)
        self.powered_up = True

    def is_still_power_up(self):
        if self.powered_up and pygame.time.get_ticks() - self.power_up_time < POWER_TIME:
            return True

        if self.powered_up is False:
            return False

        self.powered_up = False
        x_speed, y_speed = self.ball.get_speed()
        x_speed = BallSpeed.X_SPEED if x_speed > 0 else -BallSpeed.X_SPEED
        y_speed = BallSpeed.Y_SPEED if y_speed > 0 else -BallSpeed.Y_SPEED
        self.ball.set_speed(x_speed=x_speed, y_speed=y_speed)
        self.ball.update_radius(radius=BallDimensions.RADIUS)
        self.ball.set_character_img(character_img=self._original_ball_character_img)
        self.ball.set_rotated_img()

        return False




