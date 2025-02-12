from typing import Any

from constants.common import Colors
from objects.screen import Screen


class Ball:
    def __init__(
        self,
        screen: Screen,
        speed_x: int,
        speed_y: int,
        x_axis_loc: int,
        y_axis_loc: int,
        color: str = Colors.RED,
    ):
        self.__color = color

        self.__x_speed = speed_x
        self.__y_speed = speed_y

        self.__x_axis_loc = x_axis_loc
        self.__y_axis_loc = y_axis_loc

        self.__screen = screen

    def move(self, object: Any):
        pass
