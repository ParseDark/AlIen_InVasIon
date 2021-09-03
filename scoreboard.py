import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scoreboard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # setting score text style
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # init the init score image
        self.prep_score()
        self.prep_ships()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        # display the score image on left top.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.right - 100
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.ships.draw(self.screen)

    def prep_ships(self):
        self.ships = Group()
        for ship_num in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_num * 80
            ship.rect.y = 10

            self.ships.add(ship)