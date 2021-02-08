import pygame


class Ship:
    """
    Class for managing behaviour of the player's ship.
    """

    def __init__(self, ai_game):
        """Initializes the ship and sets its initial position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draws the ship in current position."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ship's position according to flags."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1