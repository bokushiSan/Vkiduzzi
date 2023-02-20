from gaming.main_menu import menu_screen
import utilities.window_gameset as cn
import pygame

pygame.init()

SCREEN_WIDTH = cn.SCREEN_WIDTH
SCREEN_HEIGHT = cn.SCREEN_HEIGHT

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def start_game():
    """
    Start game
    """
    while True:
        menu_screen(window)
