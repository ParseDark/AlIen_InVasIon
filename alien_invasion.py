import sys

import pygame


class AlienInvasion:
    def __init__(self):
        # 初始化 pygame对象
        pygame.init()

        # 设置屏幕大小
        # set_mode: 屏幕大小设置接口
        self.screen = pygame.display.set_mode((1200, 800))
        # 设置游戏窗口标题
        pygame.display.set_caption("Alien Invasion")

        # 设置游戏背景色
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # 开启游戏循环
        while True:
            # 监听键盘事件
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()

            # 每次循环重绘屏幕
            # fill: 颜色填充接口， 只接受一个颜色
            self.screen.fill(self.bg_color)

            # 重新渲染屏幕（先擦出再渲染）可以表达位置的移动
            # 使屏幕可见
            pygame.display.flip()


