import pygame.font


class Button:
    """
    Class for representing buttons in game.
    """

    def __init__(self, ai_game, message):
        """Initiates button's attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 60
        self.button_color = (153, 255, 153)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('comicsansms', 40, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prepare_message(message)

    def _prepare_message(self, message):
        """Transforms message into rect and places it in center position."""
        self.msg_image = self.font.render(message, True,
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Shows blank button and outputs message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)