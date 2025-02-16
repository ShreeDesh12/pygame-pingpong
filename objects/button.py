import pygame

from constants.common import Colors
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT


class Button:
    def __init__(
        self,
        text_str: str,
        text_color: Colors = Colors.WHITE,
        button_color: Colors = Colors.BLUE,
        text_font_size: int = 50,
        button_padding: int = 20,
        toggle_with_mouse: bool = False,
        toggle_button_color: Colors = Colors.RED,
        x_loc: int = SCREEN_WIDTH // 2,
        y_loc: int = SCREEN_HEIGHT // 2,
        is_screen_fill_required: bool = True,
    ):
        self.button_color = button_color
        self.toggle_with_mouse = toggle_with_mouse
        self.toggle_button_color = toggle_button_color
        self.text_color = text_color
        self.text_str = text_str
        self.is_screen_fill_required = is_screen_fill_required

        self.font = pygame.font.Font(None, text_font_size)
        self.button_text = self.font.render(text_str, True, self.text_color)
        self.text_rect = (x_loc, y_loc)
        self.button_rect = self.button_text.get_rect(center=(x_loc, y_loc))
        self.button_padding = button_padding

        self.button_box = self.button_rect.inflate(
            self.button_padding, self.button_padding
        )

    def display(self, screen):
        if self.is_screen_fill_required:
            screen.fill(Colors.BLACK)

        button_color = self.button_color
        if self.toggle_with_mouse and self.button_box.collidepoint(
            pygame.mouse.get_pos()
        ):
            button_color = self.toggle_button_color

        pygame.draw.rect(screen, button_color, self.button_box, border_radius=10)
        pygame.draw.rect(screen, Colors.WHITE, self.button_box, 3, border_radius=10)
        screen.blit(self.button_text, self.button_rect)

    def update_text(self, text_str):
        self.text_str = text_str
        self.button_text = self.font.render(self.text_str, True, self.text_color)
        self.button_rect = self.button_text.get_rect(center=self.text_rect)

        self.button_box = self.button_rect.inflate(
            self.button_padding, self.button_padding
        )
