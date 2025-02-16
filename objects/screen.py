import pygame

from constants.common import Colors
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

    def render_text(self, text, text_rect):
        print("Rendering text")
        self.__screen_obj.blit(text, text_rect)

    def start_screen(self):
        font = pygame.font.Font(None, 50)
        button_text = font.render("START", True, Colors.WHITE)
        button_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        button_padding = 20
        button_box = button_rect.inflate(button_padding * 2, button_padding * 2)

        self.__screen_obj.fill(Colors.BLACK)
        mouse_pos = pygame.mouse.get_pos()

        button_color = Colors.BLUE if button_box.collidepoint(mouse_pos) else Colors.RED
        pygame.draw.rect(self.__screen_obj, button_color, button_box, border_radius=10)
        pygame.draw.rect(self.__screen_obj, Colors.WHITE, button_box, 3, border_radius=10)
        self.__screen_obj.blit(button_text, button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_box.collidepoint(event.pos):
                    return True

        return False
