
class GameState:
    """track game runtime statistics info"""

    def __init__(self, ai_game):
        """init the statistics state"""

        self.settings = ai_game.settings
        self.game_activate = True
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit