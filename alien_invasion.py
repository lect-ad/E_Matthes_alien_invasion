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
        # Found typo in the book code (was undefined variable 'screen'
        # instead of AlienInvasion instance in the code line below.)
        self.ship = Ship(self)

    def run_game(self):
        """Launches main game cycle."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Processes kbd and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Refreshes screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()