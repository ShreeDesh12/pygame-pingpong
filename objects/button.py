import pygame

from constants.common import Colors
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT


class Button:
    def __init__(
        self,
        text_str: str,
        text_color: Colors = Colors.WHITE,
        button_color: Colors = Colors.BLUE,
        button_padding: int = 20,
        toggle_with_mouse: bool = False,
        toggle_button_color: Colors = Colors.RED,
    ):
        self.button_color = button_color
        self.toggle_with_mouse = toggle_with_mouse
        self.toggle_button_color = toggle_button_color

        font = pygame.font.Font(None, 50)
        self.button_text = font.render(text_str, True, text_color)
        self.button_rect = self.button_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )

        self.button_box = self.button_rect.inflate(
            button_padding * 2, button_padding * 2
        )

    def display(self, screen):
        screen.fill(Colors.BLACK)

        button_color = self.button_color
        if self.toggle_with_mouse and self.button_box.collidepoint(
            pygame.mouse.get_pos()
        ):
            button_color = self.toggle_button_color

        pygame.draw.rect(screen, button_color, self.button_box, border_radius=10)
        pygame.draw.rect(screen, Colors.WHITE, self.button_box, 3, border_radius=10)
        screen.blit(self.button_text, self.button_rect)
