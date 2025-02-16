import pygame

from constants.common import Colors
from constants.screen import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_COLOR
from objects.button import Button


class Screen:
    def __init__(
        self,
        height: int = SCREEN_HEIGHT,
        width: int = SCREEN_WIDTH,
        color: str = SCREEN_COLOR,
        start_button: Button = None,
        end_button: Button = None,
    ):
        self.__width = width
        self.__height = height
        self.__color = color
        self.__screen_obj = pygame.display.set_mode((self.__width, self.__height))
        self.__start_button = start_button
        self.__end_button = end_button

    def get_screen(self):
        return self.__screen_obj

    def set_background(self, color):
        self.__screen_obj.fill(color=color)

    def get_screen_dimensions(self):
        return self.__height, self.__width

    def render_text(self, text, text_rect):
        print("Rendering text")
        self.__screen_obj.blit(text, text_rect)

    def set_start_button(self, start_button: Button):
        self.__start_button = start_button

    def set_end_button(self, end_button: Button):
        self.__end_button = end_button

    def start_screen(self):
        self.__start_button.display(screen=self.__screen_obj)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__start_button.button_box.collidepoint(event.pos):
                    return True

        return False

    def end_screen(self):
        self.__end_button.display(screen=self.__screen_obj)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__end_button.button_box.collidepoint(event.pos):
                    return True

        return False
