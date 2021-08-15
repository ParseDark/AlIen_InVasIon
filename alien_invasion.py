import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from utils import Utils

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
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        # 开启游戏循环
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    @staticmethod
    def exit_game():
        sys.exit()

    def _check_key_down_event(self, e):
        dire = Utils.get_the_keyboard_dire(e)
        if dire:
            self.ship.start_move(dire)

    def _check_key_up_event(self, e):
        dire = Utils.get_the_keyboard_dire(e)
        if dire:
            self.ship.stop_move(dire)

    def _check_q_exit_game_event(self, e):
        if Utils.is_q_key(e):
            self.exit_game()

    def _check_blank_fire_event(self, e):
        if Utils.is_blank_key(e):
            new_bullet = Bullet(self)
            if len(self.bullets) < self.settings.bullet_allow_count:
                self.bullets.add(new_bullet)

    def _check_events(self):

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                self._check_key_down_event(e)
                self._check_q_exit_game_event(e)
                self._check_blank_fire_event(e)
            elif e.type == pygame.KEYUP:
                self._check_key_up_event(e)

    def _update_bullets(self):
        for bullet in self.bullets.sprites():
            if bullet.should_delete_it():
                self.bullets.remove(bullet)
            else:
                bullet.draw_bullet()

        self.bullets.update()


    def _update_screen(self):
            # 每次循环重绘屏幕
            # fill: 颜色填充接口， 只接受一个颜色
            self.screen.fill(self.settings.bg_color,)
            self.screen.blit(self.settings.bg_image, (0, 0))
            self.ship.blitme()
            self._update_bullets()


            # 重新渲染屏幕（先擦除再渲染）可以表达位置的移动
            # 使屏幕可见
            pygame.display.flip()


