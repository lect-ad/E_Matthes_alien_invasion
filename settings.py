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

        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)