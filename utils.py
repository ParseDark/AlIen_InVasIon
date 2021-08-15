import pygame

class Utils:

    @staticmethod
    def get_the_keyboard_dire(e):
        if e.key == pygame.K_RIGHT:
            dire = 'R'
        elif e.key == pygame.K_LEFT:
            dire = 'L'
        elif e.key == pygame.K_UP:
            dire = 'T'
        elif e.key == pygame.K_DOWN:
            dire = 'D'
        else:
            dire = None

        return dire

    @staticmethod
    def is_q_key(e):
        if e.key == pygame.K_q:
            return True
        return False

    @staticmethod
    def is_blank_key(e):
        if e.key == pygame.K_SPACE:
            return True
        return False