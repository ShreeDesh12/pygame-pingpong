from typing import Any

import pygame

from constants.common import Colors


class ImageButton:
    def __init__(
        self,
        image_file: str, screen: Any,
        image_center: tuple,
        semi_transparent: bool = False,
        image_size: tuple = (40, 40),
        border: Colors = None,
        operation: callable = None,
        timer: int = None
    ):
        image = pygame.image.load(image_file)
        if semi_transparent:
            image = image.convert_alpha()

        self.__image = pygame.transform.scale(image, image_size)
        self.image_rect = self.__image.get_rect(center=image_center)
        self.screen = screen
        self.border = border
        self.radius = max(image_size)
        self.operation = operation
        self.timer = timer
        self.last_triggered_at = None
        self.is_enabled = True

    def display(self):
        self.is_enabled = self.is_button_enabled()
        if self.is_enabled and self.border:
            pygame.draw.circle(self.screen, self.border, self.image_rect.center, self.radius, 5)  # Green outline

        self.screen.blit(self.__image, self.image_rect.topleft)

    def perform_movement(self, mouse_pos, **kwargs):
        self.is_enabled = self.is_button_enabled()
        if self.image_rect.collidepoint(mouse_pos) and self.is_enabled:
            self.last_triggered_at = pygame.time.get_ticks()

            if self.operation:
                self.operation()

    def is_button_enabled(self):
        return self.last_triggered_at is None or pygame.time.get_ticks() - self.last_triggered_at > self.timer
