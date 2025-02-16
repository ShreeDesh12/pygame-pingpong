from constants.common import Game
from objects.ball import Ball
from objects.screen import Screen
from objects.bat import Bat


class Player:
    def __init__(self, screen: Screen, bat: Bat):
        self.__screen = screen
        self.__bat = bat
        self._score = 0

    def set_bat(self, bat: Bat):
        self.__bat = bat

    def check_win_and_increase_score(self, *args):
        if self.winning_condition(*args):
            self.set_score(self._score + 1)
            print(f"goal scored: {self._score}")

        return self._score == Game.WIN_SCORE

    def move_bat(self, keys):
        self.__bat.move(keys=keys)

    def display(self):
        self.__bat.display()

    def set_score(self, new_score: int):
        self._score = new_score
        print(f"Setting new score: {self._score}")

    def winning_condition(self, *args):
        pass
