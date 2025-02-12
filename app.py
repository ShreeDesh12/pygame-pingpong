import pygame

from constants.bat import BatRestrictions
from constants.common import Colors
from constants.screen import SCREEN_WIDTH
from objects.bat import Bat
from objects.screen import Screen


def setup_game():
    # Initialize pygame
    pygame.init()
    screen = Screen()

    # Screen settings
    pygame.display.set_caption("Rolling Ball")

    bat_player_1 = Bat(
        screen=screen,
        max_x_axis=SCREEN_WIDTH,
        min_x_axis=SCREEN_WIDTH - BatRestrictions.X_AXIS,
        left_button=pygame.K_a,
        right_button=pygame.K_d,
        up_button=pygame.K_w,
        down_button=pygame.K_s,
    )
    bat_player_2 = Bat(screen=screen)
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.set_background(color=Colors.WHITE)  # Clear screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys:
            bat_player_1.move(keys=keys)
            bat_player_2.move(keys=keys)

        bat_player_1.display()
        bat_player_2.display()

        # Refresh screen
        pygame.display.flip()

        # Control frame rate
        clock.tick(60)

    pygame.quit()


setup_game()
