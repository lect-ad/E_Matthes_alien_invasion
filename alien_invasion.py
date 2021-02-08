import sys
import pygame


class AlienInvasion:
    """
    Class for managing a game.
    """

    def __init__(self):
        """
        Initializes game and creates game resources.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (25, 25, 112)

    def run_game(self):
        """
        Launches main game cycle.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()