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
        no_hit_zone: str = "left"
    ):
        self.__color = color
        self.__rect_height = rect_height
        self.__rect_width = rect_width

        self.__x_axis_loc = x_axis_loc
        self.__y_axis_loc = y_axis_loc

        self.__x_speed = x_speed
        self.__y_speed = y_speed

        self.__max_x_axis = (
            (min(BatRestrictions.X_AXIS, SCREEN_WIDTH) - self.__rect_width)
            if max_x_axis is None
            else max_x_axis - self.__rect_width
        )
        self.__max_y_axis = (
            (min(BatRestrictions.Y_AXIS, SCREEN_HEIGHT) - self.__rect_height)
            if max_y_axis is None
            else max_y_axis - self.__rect_height
        )
        self.__min_x_axis = 0 if min_x_axis is None else min_x_axis
        self.__min_y_axis = 0 if min_y_axis is None else min_y_axis

        self.__screen = screen.get_screen()
        self.__ball = ball
        if ball:
            radius = ball.get_dimensions()['radius']
            self._ball_x_hit = (self.__rect_width) / 2 + radius
            self._ball_y_hit = (self.__rect_height) / 2 + radius

        self.__left_button = left_button
        self.__right_button = right_button
        self.__up_button = up_button
        self.__down_button = down_button

        self.no_hit_zone = no_hit_zone

    def move(self, keys):
        if keys[self.__left_button]:
            self.__move_left()

        if keys[self.__right_button]:
            self.__move_right()

        if keys[self.__up_button]:
            self.__move_up()

        if keys[self.__down_button]:
            self.__move_down()

    def display(self):
        self.__validate_position()
        self.__hit_ball()
        pygame.draw.rect(self.__screen, self.__color, self.get_bat())

    def get_bat(self):
        return (
            self.__x_axis_loc,
            self.__y_axis_loc,
            self.__rect_width,
            self.__rect_height,
        )

    def get_boundary(self):
        return {
            "start_x": self.__x_axis_loc,
            "start_y": self.__y_axis_loc,
            "end_x": self.__x_axis_loc,
            "end_y": self.__y_axis_loc,
        }

    def __move_left(self):
        self.__x_axis_loc -= self.__x_speed

    def __move_right(self):
        self.__x_axis_loc += self.__x_speed

    def __move_up(self):
        self.__y_axis_loc -= self.__y_speed

    def __move_down(self):
        self.__y_axis_loc += self.__y_speed

    def __validate_position(self):
        if self.__x_axis_loc < self.__min_x_axis:
            self.__x_axis_loc = self.__min_x_axis

        if self.__x_axis_loc > self.__max_x_axis:
            self.__x_axis_loc = self.__max_x_axis

        if self.__y_axis_loc < self.__min_y_axis:
            self.__y_axis_loc = self.__min_y_axis

        if self.__y_axis_loc > self.__max_y_axis:
            self.__y_axis_loc = self.__max_y_axis

    def __hit_ball(self):
        mid_x_bat_loc = self.__x_axis_loc + (self.__rect_width) / 2
        mid_y_bat_loc = self.__y_axis_loc + (self.__rect_height) / 2
        ball_boundary = self.__ball.get_dimensions()
        abs_dist_x = abs(ball_boundary["x_loc"] - mid_x_bat_loc)
        abs_dist_y = abs(ball_boundary["y_loc"] - mid_y_bat_loc)

        is_no_hit_zone = self.__min_x_axis<ball_boundary['x_loc']<self.__x_axis_loc if self.no_hit_zone=="left" else (
                self.__x_axis_loc+self.__rect_width<ball_boundary['x_loc']<self.__max_x_axis)

        if abs_dist_x <= self._ball_x_hit and abs_dist_y <= self._ball_y_hit and not (is_no_hit_zone):
            self.__ball.hit_vertical_wall()
