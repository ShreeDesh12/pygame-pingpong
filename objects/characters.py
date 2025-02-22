from typing import Any, Optional

import pygame

from constants.bat import BatSpeed, BatDimensions
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.ball import Ball
from objects.bat import Bat
from objects.screen import Screen


class Character(Bat):
    def __init__(
            self,
            screen: Screen,
            image_loc: str,
            x_axis_loc: int = SCREEN_WIDTH // 3,
            y_axis_loc: int = SCREEN_HEIGHT // 2,
            x_speed: int = BatSpeed.X_SPEED,
            y_speed: int = BatSpeed.Y_SPEED,
            rect_height: int = BatDimensions.CHARACTER_HEIGHT,
            rect_width: int = BatDimensions.CHARACTER_WIDTH,
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
            hit_character_img: Optional[str] = None
            ):
        super().__init__(
            screen=screen,
            x_axis_loc=x_axis_loc,
            y_axis_loc=y_axis_loc,
            x_speed=x_speed,
            y_speed=y_speed,
            rect_width=rect_width,
            rect_height=rect_height,
            left_button=left_button,
            right_button=right_button,
            down_button=down_button,
            up_button=up_button,
            max_x_axis=max_x_axis,
            max_y_axis=max_y_axis,
            min_x_axis=min_x_axis,
            min_y_axis=min_y_axis,
            ball=ball,
            no_hit_zone=no_hit_zone,
        )
        self._hit_time = None
        self.character_img = pygame.image.load(image_loc).convert_alpha()
        self.character_img = pygame.transform.scale(self.character_img, (rect_width, rect_height))

        if hit_character_img:
            self.hit_character_img = pygame.image.load(hit_character_img).convert_alpha()
            self.hit_character_img = pygame.transform.scale(self.hit_character_img, (rect_width, rect_height))

    def set_image(self, image_loc: str):
        self.character_img = pygame.image.load(image_loc)
        self.character_img = pygame.transform.scale(self.character_img, (self._rect_width, self._rect_height))

    def display(self):
        self._validate_position()
        if self._hit_ball():
            self._hit_time = pygame.time.get_ticks()

        if self._hit_time and pygame.time.get_ticks() - self._hit_time < 500:
            self._display_hit_character()
        else:
            self._display_character()

    def _display_character(self):
        self._screen.blit(self.character_img, (self._x_axis_loc, self._y_axis_loc))

    def _display_hit_character(self):
        self._screen.blit(self.hit_character_img, (self._x_axis_loc, self._y_axis_loc))
