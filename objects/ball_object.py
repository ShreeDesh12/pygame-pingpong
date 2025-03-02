import pygame

from objects.ball import Ball


class BallObject(Ball):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.character_img_loc = kwargs.get("image_loc")
        self.character_img = pygame.image.load(kwargs.get("image_loc")).convert_alpha()
        self.character_img = pygame.transform.scale(self.character_img, (self._radius*2, self._radius*2))
        self.rotated_img = pygame.transform.rotate(self.character_img, 45)
        self.rotated_img_time = pygame.time.get_ticks()

    def set_character_img(self, character_img: str):
        self.character_img = pygame.image.load(character_img).convert_alpha()
        self.character_img = pygame.transform.scale(self.character_img, (self._radius * 2, self._radius * 2))

    def set_rotated_img(self):
        self.rotated_img = pygame.transform.rotate(self.character_img, 45)

    def unset_rotated_img(self):
        self.rotated_img = None

    def get_character_img(self):
        return self.character_img_loc

    def display(self):
        self._validate_obstacle()
        curr_time = pygame.time.get_ticks()
        if self.rotated_img:
            if curr_time - self.rotated_img_time < 200:
                self._screen.get_screen().blit(self.rotated_img, (self._x_axis_loc, self._y_axis_loc))
            elif 200 < curr_time - self.rotated_img_time < 400:
                self._screen.get_screen().blit(self.character_img, (self._x_axis_loc, self._y_axis_loc))
            else:
                self.rotated_img_time = curr_time
                self._screen.get_screen().blit(self.rotated_img, (self._x_axis_loc, self._y_axis_loc))

        else:
            self._screen.get_screen().blit(self.character_img, (self._x_axis_loc, self._y_axis_loc))
