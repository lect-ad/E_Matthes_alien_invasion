import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        self.stats = GameStats(self)

        # Found typo in the book code (was undefined variable 'screen'
        # instead of AlienInvasion instance in the code line below.)
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play")

    def run_game(self):
        """Launches main game cycle."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Processes kbd and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button(mouse_position)

    def _check_play_button(self, mouse_position):
        """Starts new game on Play button clicking."""
        if self.play_button.rect.collidepoint(mouse_position):
            self.stats.game_active = True

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
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)
        available_space_y = self.settings.screen_height - \
                            self.ship.rect.height - 3 * alien_height
        number_rows_y = available_space_y // (2 * alien_height)
        for row_number in range(number_rows_y):
            for alien_number in range(number_aliens_x):
                self._create_single_alien(row_number, alien_number)

    def _create_single_alien(self, row_number, alien_number):
        """Creates one single alien ship and places it in the row of ships."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Handles fleet's reaching screen edge."""
        for alien in self.aliens:
            if alien.check_edges():
                self._change_aliens_direction()
                break

    def _change_aliens_direction(self):
        """Drops the fleet down and changes its moving direction."""
        for alien in self.aliens:
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.aliens_direction *= -1

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
        self._check_bullet_alien_collision()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Updates all the aliens' positions."""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _update_screen(self):
        """Refreshes screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw_bullet()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _check_bullet_alien_collision(self):
        """Handles collisions between bullets and aliens."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens:
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Handles ship-alien collisions."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
        else:
            self.stats.game_active = False

        sleep(1)




if __name__ == '__main__':
    ai_game = AlienInvasion()
    ai_game.run_game()