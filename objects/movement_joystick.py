from typing import Any

from constants.bat import Movement
from constants.screen import SCREEN_HEIGHT, SCREEN_WIDTH
from objects.image_button import ImageButton
from objects.player import Player


class MovementJoystick:
    def __init__(self, player: Player, screen: Any):
        image_center_x, image_center_y = (player.max_x + player.min_x)//2, SCREEN_HEIGHT - 100

        self.move_up = ImageButton(image_file="images/up-arrow.png", image_center=(image_center_x, image_center_y-20), screen=screen)
        self.move_down = ImageButton(image_file="images/down-arrow.png", image_center=(image_center_x, image_center_y+20),
                                     screen=screen)
        self.move_left = ImageButton(image_file="images/left-arrow.png", image_center=(image_center_x-20,
                                                                                      image_center_y), screen=screen)
        self.move_right = ImageButton(image_file="images/right-arrow.png", image_center=(image_center_x+20,
                                                                                        image_center_y), screen=screen)
        self.player = player

    def display(self):
        self.move_up.display()
        self.move_down.display()
        self.move_right.display()
        self.move_left.display()

    def perform_movement(self, mouse_pos: tuple):
        if self.move_up.image_rect.collidepoint(mouse_pos):
            self.player.move_bat_using_joystick(movement=Movement.UP)

        if self.move_down.image_rect.collidepoint(mouse_pos):
            self.player.move_bat_using_joystick(movement=Movement.DOWN)

        if self.move_right.image_rect.collidepoint(mouse_pos):
            self.player.move_bat_using_joystick(movement=Movement.RIGHT)

        if self.move_left.image_rect.collidepoint(mouse_pos):
            self.player.move_bat_using_joystick(movement=Movement.LEFT)
