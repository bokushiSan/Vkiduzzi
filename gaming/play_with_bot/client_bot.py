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


def play_bot(surface):
    """
    игра с ботом
    :param surface:
    :return:
    """
    run = True
    # next_win = str()
    # winner = 999
    # player_id = 1
    # bot_id = 0
    back_button = Button('Back', SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT / 2, back_img, 0.5)
    # enter_button = Button('Enter', SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2, enter_img, 0.5)
    # text_input_box = helper_funcs.TextInputBox(20, 20, 500, FONT)
    # group = pygame.sprite.Group(text_input_box)
    while run:
        CLOCK.tick(60)
        surface.blit(background_img, (0, 0))
        back_button.draw(surface)
        # enter_button.draw(surface)
        event_list = pygame.event.get()
        draw_text('WORK IN PROGRESS', FONT, (0, 0, 0), surface, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.draw(surface):
                    main_menu.play_how(surface)
                # if enter_button.draw(surface):
                #     entered_txt = text_input_box.text
                #     next_window(surface, entered_txt)
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_RETURN:
            #         entered_txt = text_input_box.text
            #         next_window(surface, entered_txt)
        # group.update(event_list)
        # group.draw(surface)
        pygame.display.flip()