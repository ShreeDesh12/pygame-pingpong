import pygame


class BallDimensions:
    RADIUS = 7
    CHARACTER_RADIUS = 10


class BallSpeed:
    X_SPEED = 8
    Y_SPEED = 8
    POWER_SPEED = 10


class PowerEvent:
    SPEED_UP = pygame.USEREVENT + 1
