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

    def prep_score(self):
        """Transforms current score into image."""
        round_score = round(self.stats.score, -1)
        score_str = f"{round_score:,}"
        self.score_image = self.font.render(score_str, True,
                            self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Vizualizes the score."""
        self.screen.blit(self.score_image, self.score_rect)