

class Gamestats:
    """Track stats of Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score, never to be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialise stats that can change diring the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1