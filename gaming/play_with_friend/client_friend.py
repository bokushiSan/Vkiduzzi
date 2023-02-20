import pygame
import utilities.window_gameset as cn
from utilities.button import Button
from gaming import main_menu
from gaming.play_with_friend import pick_boosters
from utilities.textbox import TextInputBox
from utilities.draw_text import draw_text
from utilities.get_image import get_image
from utilities import dice_gameset as dice_gs

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


def enter_player_1_name(surface):
    run = True
    back_button = Button('Back', SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.75, back_img, 1)
    enter_button = Button('Enter', SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.75, enter_img, 1)
    text_input_box_p1 = TextInputBox(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.5, SCREEN_WIDTH * 0.5, FONT)
    group_1 = pygame.sprite.Group(text_input_box_p1)
    while run:
        CLOCK.tick(FPS)
        surface.blit(background_img, (0, 0))
        draw_text('Enter player 1 name', FONT, (0, 0, 0), surface, (SCREEN_WIDTH * 0.5,
                                                                                 SCREEN_HEIGHT * 0.4))
        enter_button.draw(surface)
        back_button.draw(surface)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.draw(surface):
                    main_menu.play_how(surface)
                if enter_button.draw(surface):
                    entered_txt_p1 = text_input_box_p1.text
                    enter_player_2_name(surface, entered_txt_p1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    entered_txt_p1 = text_input_box_p1.text
                    enter_player_2_name(surface, entered_txt_p1)
        group_1.update(event_list)
        group_1.draw(surface)
        pygame.display.flip()


def enter_player_2_name(surface, name_player_1):
    run = True
    back_button = Button('Back', SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.75, back_img, 1)
    enter_button = Button('Enter', SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.75, enter_img, 1)
    text_input_box_p2 = TextInputBox(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.5, SCREEN_WIDTH * 0.5, FONT)
    group_1 = pygame.sprite.Group(text_input_box_p2)
    while run:
        CLOCK.tick(FPS)
        surface.blit(background_img, (0, 0))
        draw_text('Enter player 2 name', FONT, (0, 0, 0), surface, (SCREEN_WIDTH * 0.5,
                                                                                 SCREEN_HEIGHT * 0.4))
        enter_button.draw(surface)
        back_button.draw(surface)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.draw(surface):
                    main_menu.play_how(surface)
                if enter_button.draw(surface):
                    entered_txt_p2 = text_input_box_p2.text
                    if entered_txt_p2 == name_player_1:
                        draw_text('Same as P1. Change your name', FONT, (0, 0, 0), surface,
                                               (SCREEN_WIDTH * 0.5,
                                                SCREEN_HEIGHT * 0.4))
                    else:
                        game_options(surface, [name_player_1, entered_txt_p2])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    entered_txt_p2 = text_input_box_p2.text
                    if entered_txt_p2 == name_player_1:
                        draw_text('Same as P1. Change your name', FONT, (0, 0, 0), surface,
                                               (SCREEN_WIDTH * 0.5,
                                                SCREEN_HEIGHT * 0.4))
                    else:
                        game_options(surface, [name_player_1, entered_txt_p2])
        group_1.update(event_list)
        group_1.draw(surface)
        pygame.display.flip()


def game_options(surface, players: []):
    run = True
    player1, player2 = players
    start_life_txt = str(dice_gs.start_life)
    start_gold_txt = str(dice_gs.start_gold)
    start_game_button = Button('Start game', SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.75, start_game_img, 0.5)
    while run:
        CLOCK.tick(FPS)
        surface.blit(background_img, (0, 0))
        start_game_button.draw(surface)
        draw_text('Player 1 name:', FONT, (10, 10, 60), surface, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4))
        draw_text(player1, FONT, (0, 0, 0), surface, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2))
        draw_text('Player 2 name:', FONT, (10, 10, 60), surface, (SCREEN_WIDTH * 3 / 4, SCREEN_HEIGHT / 4))
        draw_text(player2, FONT, (0, 0, 0), surface, (SCREEN_WIDTH * 3 / 4, SCREEN_HEIGHT / 2))
        draw_text('Start life', FONT, (0, 0, 0), surface, (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 5))
        draw_text(start_life_txt, FONT, (0, 0, 0), surface, (SCREEN_WIDTH * 3 / 4, SCREEN_HEIGHT * 3 / 5))
        draw_text('Start gold', FONT, (0, 0, 0), surface, (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 4 / 5))
        draw_text(start_gold_txt, FONT, (0, 0, 0), surface, (SCREEN_WIDTH * 3 / 4, SCREEN_HEIGHT * 4 / 5))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_button.draw(surface):
                    pick_boosters.current_options_gods_will(surface, players, 0, None)
