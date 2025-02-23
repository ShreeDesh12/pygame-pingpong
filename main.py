import asyncio
import pygame

from constants.ball import PowerEvent, BallSpeed
from constants.bat import BatRestrictions
from constants.common import Colors, GameMode
from constants.screen import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.ball_object import BallObject
from objects.button import Button
from objects.characters import Character
from objects.movement_joystick import MovementJoystick
from objects.player import Player
from objects.power import Power
from objects.screen import Screen
from stratergy.autoplay import autoplay
from stratergy.gamemode import GameModeStrategy
from stratergy.pingpong import (
    winning_strategy_for_right_player,
    winning_strategy_for_left_player,
)
from stratergy.power import speed_up


async def async_setup_game():
    # Initialize pygame
    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load("music/naruto-background-music.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    play_against_computer = Button(text_str="1 Player", x_loc=SCREEN_WIDTH//2, y_loc=SCREEN_HEIGHT//3,
                                   toggle_with_mouse=True)
    two_player = Button(text_str="2 Player", x_loc=SCREEN_WIDTH//2, y_loc=2*SCREEN_HEIGHT//3, toggle_with_mouse=True, is_screen_fill_required=False)

    end_button = None

    screen = Screen(start_buttons=[{
        "button": play_against_computer,
        "operation": GameModeStrategy.set_game_against_computer
    },{
        "button": two_player,
        "operation": GameModeStrategy.set_game_against_player
    }],
        end_button=None
    )

    # Screen settings
    pygame.display.set_caption("PingPong")

    ball = BallObject(screen=screen, image_loc="images/ball/shiruken.png")
    power = Power(event=PowerEvent.SPEED_UP, strategy=speed_up, ball=ball, ball_img="images/ball/rasengan.png")

    bat_player_1 = Character(
        screen=screen,
        image_loc="images/characters/naruto/naruto-basic.png",
        max_x_axis=SCREEN_WIDTH,
        min_x_axis=SCREEN_WIDTH - BatRestrictions.X_AXIS,
        ball=ball,
        no_hit_zone="right",
        hit_character_img="images/characters/naruto/naruto-attack-2.png",
        power=power,
        power_button=pygame.K_SPACE
    )
    player_1 = Player(
        screen=screen.get_screen(),
        bat=bat_player_1,
        button_text="Player1 Score",
        button_color=Colors.RED,
    )
    player_1.winning_condition = winning_strategy_for_right_player

    bat_player_2 = Character(
        screen=screen,
        left_button=pygame.K_a,
        right_button=pygame.K_d,
        up_button=pygame.K_w,
        down_button=pygame.K_s,
        power_button=pygame.K_r,
        ball=ball,
        image_loc="images/characters/sasuke/sasuke-basic.png",
        hit_character_img="images/characters/sasuke/sasuke-attack.png",
    )
    joystick_player1 = MovementJoystick(player=player_1, screen=screen.get_screen())

    player_2 = Player(
        screen=screen.get_screen(),
        bat=bat_player_2,
        button_text="Player2 Score",
        button_color=Colors.BLUE,
    )
    player_2.winning_condition = winning_strategy_for_left_player
    joystick_player2 = MovementJoystick(player=player_2, screen=screen.get_screen())

    clock = pygame.time.Clock()

    game_mode = GameMode.NOT_SELECTED

    mouse_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        screen.set_background(color=Colors.WHITE)
        if game_mode == GameMode.NOT_SELECTED:
            game_mode = screen.start_screen()

        elif end_button is not None:
            screen.set_end_button(end_button=end_button)
            game_restarted = screen.end_screen()
            if game_restarted:
                game_mode = GameMode.NOT_SELECTED
                end_button = None
                player_1.set_score(0)
                player_2.set_score(0)
                ball.reset()

        else:
            joystick_player1.display()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

            joystick_player1.perform_movement(mouse_pos=mouse_pos)

            keys = pygame.key.get_pressed()
            if keys:
                player_1.move_bat(keys=keys)
                if game_mode == GameMode.TWO_PLAYERS:
                    player_2.move_bat(keys=keys)

            if game_mode == GameMode.COMPUTER:
                autoplay(bat=bat_player_2, ball=ball)

            if game_mode == GameMode.TWO_PLAYERS:
                joystick_player2.display()
                joystick_player2.perform_movement(mouse_pos=mouse_pos)

            player_1.display()
            player_2.display()

            ball.move()

            if player_1.check_win_and_increase_score(ball):
                end_button = Button(text_str="Player 1 Won!", toggle_with_mouse=True)

            if player_2.check_win_and_increase_score(ball):
                end_button = Button(text_str="Player 2 Won!", toggle_with_mouse=True)

            ball.display()

        # Refresh screen
        pygame.display.flip()

        # Control frame rate
        clock.tick(30)
        await asyncio.sleep(0)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(async_setup_game())
