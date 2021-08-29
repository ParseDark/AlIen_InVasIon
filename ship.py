import pygame.image


class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images/ghost.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # move props
        self.enable_update = False
        self.speed = 15
        self.dire = {
            'L': False,
            'R': False,
            'T': False,
            'D': False,
        }

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def x_dire_move(self, dire):
        x = None
        if dire == 'L':
            x = self.rect.x - self.speed
        elif dire == 'R':
            x = self.rect.x + self.speed
        else:
            return None

        if x and (self.screen_rect.left < x < self.screen_rect.right - self.rect.width):
            self.rect.x = x

    def y_dire_move(self, dire):
        y = None
        if dire == 'T':
            y = self.rect.y - self.speed
        elif dire == 'D':
            y = self.rect.y + self.speed
        else:
            return None

        if y and (self.screen_rect.top < y < self.screen_rect.bottom - self.rect.height):
            self.rect.y = y


    def render(self, dire):
        # render logic
        self.x_dire_move(dire)
        self.y_dire_move(dire)
        self.blitme()

    def update(self):
        for k in self.dire:
            v = self.dire.get(k)
            if v:
                self.render(k)

    def start_move(self, dire):
        if dire is not None:
            self.dire[dire] = True

    def stop_move(self, dire):
        if dire is not None:
            self.dire[dire] = False

    def center_ship(self):
        """put the ship on screen bottom center"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)





