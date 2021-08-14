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

    def render(self, dire):
        # render logic
        if dire == 'L':
            self.rect.x -= self.speed
        elif dire == 'R':
            self.rect.x += self.speed
        elif dire == 'T':
            self.rect.y -= self.speed
        elif dire == 'D':
            self.rect.y += self.speed
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



