import pygame.font


class Scoreboard:
    """
    Class for handling and visualizing game info.
    """

    def __init__(self, ai_game):
        """Initiates attributes of score counting."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('comicsansms', 36)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Transforms current score into image."""
        round_score = round(self.stats.score, -1)
        score_str = f"{round_score:,}"
        self.score_image = self.font.render(score_str, True,
                            self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Transforms current high-score into image."""
        round_high_score = round(self.stats.high_score, -1)
        high_score_str = f"High-Score: {round_high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """Transforms current level into image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                                self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """Displays the score, high-score, level and number of aliens left."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        """Checks for new high-score and updates it."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()