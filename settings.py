import pygame.image


class Settings:
    # 存游戏中所有的设置类

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load("images/bgImage.png")

        # bullet setting
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_allow_count = 3
        self.bullet_color = (60, 60, 60)

        # alien setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 30
        # 1 => right || -1 => left
        self.fleet_direction = 1

        # ship setting
        self.ship_limit = 3
        self.ship_speed = 1.5

        # boostrap the game speed.
        self.speedup_scale = 1.1
        self.scoreup_scale = 2

        # an alien socre
        self.alien_points = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 2
        self.bullet_speed = 10.0
        self.alien_speed = 5.0

        # change the  alien move direction
        self.fleet_direction = 1

    def inscreese_speed(self):
        """improve the ship speed."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.scoreup_scale)

