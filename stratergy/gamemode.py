from constants.common import GameMode


class GameModeStrategy:
    @staticmethod
    def set_game_against_computer():
        return GameMode.COMPUTER

    @staticmethod
    def set_game_against_player():
        return GameMode.TWO_PLAYERS
