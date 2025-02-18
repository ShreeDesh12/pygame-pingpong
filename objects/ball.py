import pygame

from constants.ball import BallDimensions, BallSpeed
from constants.bat import BatSpeed
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
    ):
        self.__color = color

        self.__radius = radius

        self.__x_speed = speed_x
        self.__y_speed = speed_y

        self.__x_axis_loc = x_axis_loc
        self.__y_axis_loc = y_axis_loc

        self.__screen = screen

    def get_dimensions(self):
        return {
            "x_loc": self.__x_axis_loc,
            "y_loc": self.__y_axis_loc,
            "radius": self.__radius,
        }

    def move(self):
        self.__x_axis_loc += self.__x_speed
        self.__y_axis_loc += self.__y_speed

    def get_position(self):
        return {
            "start_x": self.__x_axis_loc - self.__radius,
            "start_y": self.__y_axis_loc - self.__radius,
            "end_x": self.__x_axis_loc + self.__radius,
            "end_y": self.__y_axis_loc + self.__radius,
        }

    def hit_horizontal_wall(self):
        self.__y_speed = -self.__y_speed

    def hit_vertical_wall(self):
        self.__x_speed = -self.__x_speed

    def __validate_obstacle(self):
        boundary = self.get_position()
        screen_height, screen_width = self.__screen.get_screen_dimensions()
        if boundary["start_x"] <= 0 or boundary["end_x"] >= screen_width:
            self.__x_axis_loc = screen_width // 2
            self.__y_axis_loc = screen_height // 2

        if boundary["start_y"] <= 0 or boundary["end_y"] >= screen_height:
            self.hit_horizontal_wall()

    def display(self):
        self.__validate_obstacle()
        pygame.draw.circle(
            self.__screen.get_screen(),
            Colors.RED,
            (self.__x_axis_loc, self.__y_axis_loc),
            self.__radius,
        )

    def reset(self):
        self.__x_axis_loc = SCREEN_WIDTH // 2
        self.__y_axis_loc = SCREEN_HEIGHT // 2

    def get_speed(self):
        return self.__x_speed, self.__y_speed
