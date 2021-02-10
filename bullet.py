import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Class for managing bullets fired by player's ship.
    """

    def __init__(self, ai_game):
        """Creates bullet object at the current ship position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Moves bullet across the screen upwards."""
        self.y -= self.settings.bullet_speed_dynamic
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws bullet at its current position."""
        pygame.draw.rect(self.screen, self.color, self.rect)