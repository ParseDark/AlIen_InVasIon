import pygame.image


class Settings:
    # 存游戏中所有的设置类

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load("images/bgImage.png")