from typing import Any

import pygame

from constants.screen import SCREEN_WIDTH


class ImageButton:
    def __init__(self, image_file: str, screen: Any,
                 image_center: tuple, semi_transparent: bool = False, image_size: tuple = (40, 40),
                 ):
        image = pygame.image.load(image_file)
        if semi_transparent:
            image = image.convert_alpha()

        self.__image = pygame.transform.scale(image, image_size)
        self.image_rect = self.__image.get_rect(center=image_center)
        self.screen = screen

    def display(self):
        self.screen.blit(self.__image, self.image_rect.topleft)
