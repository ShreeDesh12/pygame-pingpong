import pygame
from typing import Dict

from constants.ball import BallDimensions, BallSpeed
from constants.common import Colors
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.screen import Screen


class Ball:
    def __init__(
        self,
        screen: Screen,
        speed_x: int = BallSpeed.X_SPEED,
        speed_y: int = BallSpeed.Y_SPEED,
        x_axis_loc: int = SCREEN_WIDTH // 2,
        y_axis_loc: int = SCREEN_HEIGHT // 2,
        radius: int = BallDimensions.RADIUS,
        color: str = Colors.RED,
        **kwargs
    ):
        self._color = color

        self._radius = radius

        self._x_speed = speed_x
        self._y_speed = speed_y

        self._x_axis_loc = x_axis_loc
        self._y_axis_loc = y_axis_loc

        self._screen = screen

    def get_dimensions(self):
        return {
            "x_loc": self._x_axis_loc,
            "y_loc": self._y_axis_loc,
            "radius": self._radius,
        }

    def move(self):
        self._x_axis_loc += self._x_speed
        self._y_axis_loc += self._y_speed

    def get_position(self):
        return {
            "start_x": self._x_axis_loc - self._radius,
            "start_y": self._y_axis_loc - self._radius,
            "end_x": self._x_axis_loc + self._radius,
            "end_y": self._y_axis_loc + self._radius,
        }

    def hit_horizontal_wall(self):
        self._y_speed = -self._y_speed

    def hit_vertical_wall(self):
        self._x_speed = -self._x_speed

    def _validate_obstacle(self):
        boundary = self.get_position()
        screen_height, screen_width = self._screen.get_screen_dimensions()
        if boundary["start_x"] <= 0 or boundary["end_x"] >= screen_width:
            self._x_axis_loc = screen_width // 2
            self._y_axis_loc = screen_height // 2

        if boundary["start_y"] <= 0 or boundary["end_y"] >= screen_height:
            self.hit_horizontal_wall()

    def display(self):
        self._validate_obstacle()
        pygame.draw.circle(
            self._screen.get_screen(),
            Colors.RED,
            (self._x_axis_loc, self._y_axis_loc),
            self._radius,
        )

    def reset(self):
        self._x_axis_loc = SCREEN_WIDTH // 2
        self._y_axis_loc = SCREEN_HEIGHT // 2

    def get_speed(self):
        return self._x_speed, self._y_speed

    def set_speed(self, x_speed: int, y_speed: int):
        self._x_speed = x_speed
        self._y_speed = y_speed

    def update_speed(self, inc_speed_x: int = None, inc_speed_y: int = None):
        if inc_speed_x is not None:
            self._x_speed += inc_speed_x

        if inc_speed_y is not None:
            self._y_speed += inc_speed_y
