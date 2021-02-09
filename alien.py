import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Class for instantiating one single alien.
    """

    def __init__(self, ai_game):
        """Initiates single alien and sets its initial position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("images/ufo.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if an alien is next to the screen edge."""
        if self.rect.right >= self.settings.screen_width \
                or self.rect.left <= 0:
            return True

    def update(self):
        """Moves alien towards right or left screen edge."""
        self.x += self.settings.alien_speed * self.settings.aliens_direction
        self.rect.x = self.x
