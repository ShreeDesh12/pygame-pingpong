import pygame

from constants.screen import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_COLOR


class Screen:
    def __init__(
        self,
        height: int = SCREEN_HEIGHT,
        width: int = SCREEN_WIDTH,
        color: str = SCREEN_COLOR,
    ):
        self.__width = width
        self.__height = height
        self.__color = color
        self.__screen_obj = pygame.display.set_mode((self.__width, self.__height))

    def get_screen(self):
        return self.__screen_obj

    def set_background(self, color):
        self.__screen_obj.fill(color=color)

    def get_screen_dimensions(self):
        return self.__height, self.__width
