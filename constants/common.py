from enum import Enum


class Colors:
    BLUE = "blue"
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)


class Game:
    WIN_SCORE: int = 5


class GameMode(str, Enum):
    NOT_SELECTED = "not_selected"
    COMPUTER = "computer"
    TWO_PLAYERS = "2_players"
