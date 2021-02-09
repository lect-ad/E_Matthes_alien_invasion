class Settings:
    """
    Class holding all the settings of Alien Invasion game
    """

    def __init__(self):
        """Initializes game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 25, 112)

        self.ship_speed = 1.5
        self.ship_limit = 3

        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        self.alien_speed = 1
        self.alien_drop_speed = 10
        self.aliens_direction = 1