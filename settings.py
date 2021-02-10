class Settings:
    """
    Class holding all the settings of Alien Invasion game
    """

    def __init__(self):
        """Initializes static game settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 25, 112)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        self.alien_drop_speed = 10

        self.speedup_scale = 1.1

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Initializes dynamic game settings."""
        self.ship_speed_dynamic = 1.5
        self.bullet_speed_dynamic = 1
        self.alien_speed_dynamic = 1

        self.aliens_direction = 1

    def increase_speed(self):
        """Increases dynamic speed settings."""
        self.ship_speed_dynamic *= self.speedup_scale
        self.bullet_speed_dynamic *= self.speedup_scale
        self.alien_speed_dynamic *= self.speedup_scale