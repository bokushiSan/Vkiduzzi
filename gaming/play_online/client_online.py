import pygame
import utilities.window_gameset as cn
from utilities.button import Button
from gaming import main_menu
from utilities.draw_text import draw_text
from utilities.get_image import get_image

pygame.init()

SCREEN_WIDTH = cn.SCREEN_WIDTH
SCREEN_HEIGHT = cn.SCREEN_HEIGHT
FONTNAME = cn.FONTNAME
FPS = cn.FPS
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont(FONTNAME, 40)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(cn.GAME_NAME)
background_img = cn.BACKGROUND_IMG


play_with_bot_img = get_image('play_bot_image.png')
play_with_friend_img = get_image('play_friend_image.png')
play_with_friend_online = get_image('play_online_image.png')
back_img = get_image('back_image.png')
enter_img = get_image('enter_image.png')
vkid_coin_img = get_image('VKID_coin.png')
uzzi_coin_img = get_image('UZZI_coin.png')
start_game_img = get_image('start_game_img.png')


def play_online(surface):
    """
    окно игры онлайн (надо переместить)
    :param surface:
    :return:
    """
    run = True
    back_button = Button('Back', SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.75, back_img, 0.5)
    while run:
        CLOCK.tick(FPS)
        surface.blit(background_img, (0, 0))
        draw_text('WORK IN PROGRESS', FONT, (0, 0, 0), surface, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        back_button.draw(surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.draw(surface):
                    main_menu.play_how(surface)
