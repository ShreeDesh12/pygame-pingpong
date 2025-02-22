from enum import Enum
from sys import maxsize


class BatSpeed:
    X_SPEED = 5
    Y_SPEED = 5
    X_MAX_SPEED = 10
    Y_MAX_SPEED = 10


class BatRestrictions:
    X_AXIS = 100
    Y_AXIS = maxsize


class BatDimensions:
    HEIGHT = 40
    WIDTH = 10
    CHARACTER_HEIGHT = 40
    CHARACTER_WIDTH = 20


class Movement(str, Enum):
    UP = "UP"
    DOWN = "DOWN"
    RIGHT = "RIGHT"
    LEFT = "LEFT"

