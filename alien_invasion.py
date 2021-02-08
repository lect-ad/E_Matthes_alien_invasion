import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Class for managing a game.
    """

    def __init__(self):
        """Initializes game and creates game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # typo found in the book code (was undefined variable screen
        # instead of AlienInvasion instance)
        self.ship = Ship(self)

    def run_game(self):
        """Launches main game cycle."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()