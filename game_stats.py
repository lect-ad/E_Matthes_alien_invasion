class GameStats:
    """
    Class for maintaining game statistics.
    """

    def __init__(self, ai_game):
        """Initiates overall game statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Starts new game statistics."""
        self.ships_left = self.settings.ship_limit