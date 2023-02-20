import pygame
import utilities.window_gameset as cn
from utilities.button import Button
from gaming.play_online import client_online
from gaming.play_with_bot import client_bot
from gaming.play_with_friend import client_friend
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

dice_img = get_image('dice.png')
pygame.display.set_icon(dice_img)

play_with_bot_img = get_image('play_with_bot.png')
play_with_friend_img = get_image('play_with_friend.png')
play_with_friend_online = get_image('play_online.png')


def menu_screen(surface):
    """
    Основное меню (первый экран)
    :param surface: initialization of game screen
    """
    run = True
    while run:
        CLOCK.tick(FPS)
        surface.blit(background_img, (0, 0))
        draw_text('VKIDUZZI', FONT, (255, 255, 255), surface, (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5))
        draw_text('Press any key to continue', FONT, (255, 255, 255), surface,
                               (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.9))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                play_how(surface)


def play_how(surface):
    """
    тип игры (бот онлайн)
    :param surface:
    :return:
    """
    run = True
    next_win = str()
    play_with_bot_button = Button('Play with bot', SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.5, play_with_bot_img, 0.7)
    play_with_friend_button = Button('Play with friend', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, play_with_friend_img,
                                     0.7)
    play_online_button = Button('Play online', SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.5, play_with_friend_online, 0.7)
    while run:
        CLOCK.tick(FPS)
        surface.blit(background_img, (0, 0))
        play_with_bot_button.draw(surface)
        play_with_friend_button.draw(surface)
        play_online_button.draw(surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_with_friend_button.draw(surface):
                    run = False
                    next_win = 'friend'
                if play_with_bot_button.draw(surface):
                    run = False
                    next_win = 'bot'
                if play_online_button.draw(surface):
                    run = False
                    next_win = 'online'
    if next_win == 'online':
        client_online.play_online(surface)
    elif next_win == 'bot':
        client_bot.play_bot(surface)
    elif next_win == 'friend':
        client_friend.enter_player_1_name(surface)

