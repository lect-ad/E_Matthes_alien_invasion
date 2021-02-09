import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from  alien import Alien


class AlienInvasion:
    """
    Class for managing a game.
    """

    def __init__(self):
        """Initializes game and creates game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        # Found typo in the book code (was undefined variable 'screen'
        # instead of AlienInvasion instance in the code line below.)
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Launches main game cycle."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Processes kbd and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Processes key pressings."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Processes key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Creates alien intruders' fleet."""
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)
        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _fire_bullet(self):
        """Creates a new bullet and incorporates it into 'bullets' group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates bullets' positions and eliminates bullets out of screen."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Refreshes screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    ai_game = AlienInvasion()
    ai_game.run_game()