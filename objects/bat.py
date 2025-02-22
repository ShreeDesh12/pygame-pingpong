import math
from typing import Any

import pygame

from constants.bat import BatSpeed, BatRestrictions, BatDimensions
from constants.common import Colors
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.ball import Ball
from objects.screen import Screen


class Bat:
    def __init__(
        self,
        screen: Screen,
        color: str = Colors.BLACK,
        x_axis_loc: int = SCREEN_WIDTH // 3,
        y_axis_loc: int = SCREEN_HEIGHT // 2,
        x_speed: int = BatSpeed.X_SPEED,
        y_speed: int = BatSpeed.Y_SPEED,
        rect_height: int = BatDimensions.HEIGHT,
        rect_width: int = BatDimensions.WIDTH,
        left_button: Any = pygame.K_LEFT,
        right_button: Any = pygame.K_RIGHT,
        down_button: Any = pygame.K_DOWN,
        up_button: Any = pygame.K_UP,
        max_x_axis: int = None,
        max_y_axis: int = None,
        min_x_axis: int = None,
        min_y_axis: int = None,
        ball: Ball = None,
        no_hit_zone: str = "left",
    ):
        self._color = color
        self._rect_height = rect_height
        self._rect_width = rect_width

        self._x_axis_loc = x_axis_loc
        self._y_axis_loc = y_axis_loc

        self._x_speed = x_speed
        self._y_speed = y_speed

        self._max_x_axis = (
            (min(BatRestrictions.X_AXIS, SCREEN_WIDTH) - self._rect_width)
            if max_x_axis is None
            else max_x_axis - self._rect_width
        )
        self._max_y_axis = (
            (min(BatRestrictions.Y_AXIS, SCREEN_HEIGHT) - self._rect_height)
            if max_y_axis is None
            else max_y_axis - self._rect_height
        )
        self._min_x_axis = 0 if min_x_axis is None else min_x_axis
        self._min_y_axis = 0 if min_y_axis is None else min_y_axis

        self._screen = screen.get_screen()
        self._ball = ball
        if ball:
            radius = ball.get_dimensions()["radius"]
            self._ball_x_hit = (self._rect_width) / 2 + radius
            self._ball_y_hit = (self._rect_height) / 2 + radius

        self._left_button = left_button
        self._right_button = right_button
        self._up_button = up_button
        self._down_button = down_button

        self.no_hit_zone = no_hit_zone
        print("Bat constructor is called!")

    def move(self, keys):
        if keys[self._left_button]:
            self.move_left()

        if keys[self._right_button]:
            self.move_right()

        if keys[self._up_button]:
            self.move_up()

        if keys[self._down_button]:
            self.move_down()

    def display(self):
        self._validate_position()
        self._hit_ball()
        pygame.draw.rect(self._screen, self._color, self.get_bat())

    def get_bat(self):
        return (
            self._x_axis_loc,
            self._y_axis_loc,
            self._rect_width,
            self._rect_height,
        )

    def get_boundary(self):
        return {
            "start_x": self._x_axis_loc,
            "start_y": self._y_axis_loc,
            "end_x": self._x_axis_loc,
            "end_y": self._y_axis_loc,
        }

    def get_restrictions(self):
        return {
            "min_x": self._min_x_axis,
            "min_y": self._min_y_axis,
            "max_x": self._max_x_axis,
            "max_y": self._max_y_axis,
        }

    def move_left(self):
        self._x_axis_loc -= self._x_speed

    def move_right(self):
        self._x_axis_loc += self._x_speed

    def move_up(self):
        self._y_axis_loc -= self._y_speed

    def move_down(self):
        self._y_axis_loc += self._y_speed

    def _validate_position(self):
        if self._x_axis_loc < self._min_x_axis:
            self._x_axis_loc = self._min_x_axis

        if self._x_axis_loc > self._max_x_axis:
            self._x_axis_loc = self._max_x_axis

        if self._y_axis_loc < self._min_y_axis:
            self._y_axis_loc = self._min_y_axis

        if self._y_axis_loc > self._max_y_axis:
            self._y_axis_loc = self._max_y_axis

    def _hit_ball(self):
        mid_x_bat_loc = self._x_axis_loc + (self._rect_width) / 2
        mid_y_bat_loc = self._y_axis_loc + (self._rect_height) / 2
        ball_boundary = self._ball.get_dimensions()
        abs_dist_x = abs(ball_boundary["x_loc"] - mid_x_bat_loc)
        abs_dist_y = abs(ball_boundary["y_loc"] - mid_y_bat_loc)

        is_no_hit_zone = (
            self._min_x_axis < ball_boundary["x_loc"] < self._x_axis_loc
            if self.no_hit_zone == "left"
            else (
                self._x_axis_loc + self._rect_width
                < ball_boundary["x_loc"]
                < self._max_x_axis
            )
        )

        if (
            abs_dist_x <= self._ball_x_hit
            and abs_dist_y <= self._ball_y_hit
            and not (is_no_hit_zone)
        ):
            self._ball.hit_vertical_wall()
