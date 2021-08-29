import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from utils import Utils
from alien import Alien
from game_stats import GameState
from time import sleep

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

        # init the GameState
        self.stats = GameState(self)

        # init the ship
        self.ship = Ship(self)
        # init the bullets
        self.bullets = pygame.sprite.Group()
        # init the aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        # 开启游戏循环
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


    @staticmethod
    def exit_game():
        sys.exit()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (2 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        number_aliens_x = available_space_x // alien_width
        # 创建外星人群
        for raw_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, raw_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """when alien hit the screen edge will change the group direction"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        print("in the edge")
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

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
        # remove out of screen bullets
        for bullet in self.bullets.sprites():
            if bullet.should_delete_it():
                self.bullets.remove(bullet)
            else:
                bullet.draw_bullet()

        self._check_bullet_alien_collisions()

        self.bullets.update()

    def _check_bullet_alien_collisions(self):
        """will remove bullet and alien when bullet collisions with alien"""
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _ship_hit(self):
        """when ship hit the alien"""

        # limit reduce 1
        self.stats.ships_left -= 1

        # clean the rest bullets and aliens
        self.aliens.empty()
        self.bullets.empty()

        # create a new group aliens and init the ship
        self._create_fleet()
        self.ship.center_ship()

        sleep(0.5)


    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _render_alien(self):
        self.aliens.draw(self.screen)


    def _update_screen(self):
            # 每次循环重绘屏幕
            # fill: 颜色填充接口， 只接受一个颜色
            self.screen.fill(self.settings.bg_color,)
            self.screen.blit(self.settings.bg_image, (0, 0))
            self.ship.blitme()
            self._update_bullets()
            self._render_alien()
            self._update_aliens()

            # 重新渲染屏幕（先擦除再渲染）可以表达位置的移动
            # 使屏幕可见
            pygame.display.flip()


