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
