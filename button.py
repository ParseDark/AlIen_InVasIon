import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        """initial the button props"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # setting the size and font eg.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # create a button instance and set the position are center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """render msg as an image on button and center it."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """draw a colorful button  and draw text"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)