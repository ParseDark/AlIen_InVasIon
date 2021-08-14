import sys

import pygame


class AlienInvasion:
    def __init__(self):
        # 初始化 pygame对象
        pygame.init()

        # 设置屏幕大小
        self.screen = pygame.display.set_mode((1200, 800))
        # 设置游戏窗口标题
        pygame.display.set_caption("Alien Invasion")

    @staticmethod
    def run_game():
        # 开启游戏循环
        while True:
            # 监听键盘事件
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
            # 重新渲染屏幕（先擦出再渲染）可以表达位置的移动
            pygame.display.flip()


