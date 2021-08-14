import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        # 初始化 pygame对象
        pygame.init()
        self.settings = Settings()
        # 设置屏幕大小
        # set_mode: 屏幕大小设置接口
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 设置游戏窗口标题
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        # 开启游戏循环
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
            # 每次循环重绘屏幕
            # fill: 颜色填充接口， 只接受一个颜色
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # 重新渲染屏幕（先擦除再渲染）可以表达位置的移动
            # 使屏幕可见
            pygame.display.flip()


