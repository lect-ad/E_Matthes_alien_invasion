import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """
    Class for managing behaviour of the player's ship.
    """

    def __init__(self, ai_game):
        """Initializes the ship and sets its initial position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draws the ship at current position."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ship's position according to flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_dynamic
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_dynamic
        self.rect.x = self.x

    def center_ship(self):
        """Places ship in the bottom-center of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
