from typing import Any

import pygame

from constants.bat import BatSpeed, BatRestrictions, BatDimensions
from constants.common import Colors
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT
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

        self.__left_button = left_button
        self.__right_button = right_button
        self.__up_button = up_button
        self.__down_button = down_button

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
        pygame.draw.rect(self.__screen, self.__color, self.get_bat())

    def get_bat(self):
        return (
            self.__x_axis_loc,
            self.__y_axis_loc,
            self.__rect_width,
            self.__rect_height,
        )

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
