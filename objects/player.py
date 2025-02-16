from constants.common import Game, Colors
from constants.screen import SCREEN_HEIGHT, SCREEN_WIDTH
from objects.ball import Ball
from objects.button import Button
from objects.screen import Screen
from objects.bat import Bat


class Player:
    def __init__(
        self,
        screen: Screen,
        bat: Bat,
        button_text: str = None,
        button_color: Colors = Colors.RED,
    ):
        self.__screen = screen
        self.__bat = bat
        self._score = 0
        bat_pos = bat.get_restrictions()

        button_x_loc = (
            bat_pos["min_x"] + SCREEN_WIDTH // 10
            if bat_pos["min_x"] < SCREEN_WIDTH // 2
            else bat_pos["max_x"] - SCREEN_WIDTH // 10
        )
        self.__score_button = (
            Button(
                text_str=button_text,
                button_color=button_color,
                text_font_size=20,
                button_padding=10,
                x_loc=button_x_loc,
                y_loc=SCREEN_HEIGHT - SCREEN_HEIGHT // 10,
                is_screen_fill_required=False,
            )
            if (button_text)
            else None
        )
        self.button_text = button_text

    def set_bat(self, bat: Bat):
        self.__bat = bat

    def check_win_and_increase_score(self, *args):
        if self.winning_condition(*args):
            self.set_score(self._score + 1)

        return self._score == Game.WIN_SCORE

    def move_bat(self, keys):
        self.__bat.move(keys=keys)

    def display(self):
        self.__bat.display()
        self.__button_display()

    def set_score(self, new_score: int):
        self._score = new_score

    def __button_display(self):
        if self.__score_button:
            self.__score_button.update_text(
                text_str=f"{self.button_text}: {self._score} "
            )
            self.__score_button.display(screen=self.__screen)

    def winning_condition(self, *args):
        pass
