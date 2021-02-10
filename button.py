import pygame.font


class Button:
    """
    Class for representing buttons in game.
    """

    def __init__(self, ai_game, message, width=300, height=60, offset=0,
                 button_color=(153, 255, 153), text_color=(0, 0, 0)):
        """Initiates button's attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width = width
        self.height = height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont('comicsansms', 36, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.centerx, \
                           self.screen_rect.centery + offset

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