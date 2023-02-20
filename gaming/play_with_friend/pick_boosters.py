import pygame
import utilities.window_gameset as cn
from utilities.button import Button
from gaming.play_with_friend import client_friend
from gaming.play_with_friend.game_process import GamePVP
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

gw1 = get_image('gw1.png')
gw2 = get_image('gw2.png')
gw3 = get_image('gw3.png')
gw4 = get_image('gw4.png')
gw5 = get_image('gw5.png')
gw6 = get_image('gw6.png')
gw7 = get_image('gw7.png')
gw8 = get_image('gw8.png')
gw9 = get_image('gw9.png')
gw10 = get_image('gw10.png')
next_img = get_image('next_img.png')
prev_img = get_image('prev_img.png')
pick_img = get_image('pick_img.png')
ready_img = get_image('ready_img.png')


gw1_button = Button('Gw1', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw1, 0.5)
gw2_button = Button('Gw2', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw2, 0.5)
gw3_button = Button('Gw3', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw3, 0.5)
gw4_button = Button('Gw4', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw4, 0.5)
gw5_button = Button('Gw5', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw5, 0.5)
gw6_button = Button('Gw6', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw6, 0.5)
gw7_button = Button('Gw7', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw7, 0.5)
gw8_button = Button('Gw8', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw8, 0.5)
gw9_button = Button('Gw9', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw9, 0.5)
gw10_button = Button('Gw10', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, gw10, 0.5)
godwills_list_p1 = [gw1_button, gw2_button, gw3_button, gw4_button, gw5_button, gw6_button, gw7_button, gw8_button,
                     gw9_button, gw10_button]
godwills_list_p2 = [gw1_button, gw2_button, gw3_button, gw4_button, gw5_button, gw6_button, gw7_button, gw8_button,
                     gw9_button, gw10_button]


p1_picked_gods_wills = list()
p2_picked_gods_wills = list()


def current_options_gods_will(surface, players, godwill, picked_godwill):
    if len(p1_picked_gods_wills) < 3:
        if picked_godwill is not None:
            p1_picked_gods_wills.append(picked_godwill)
        print('p1 list', p1_picked_gods_wills)
        pick_gods_will_main(surface, players, godwill, 0)
    elif len(p1_picked_gods_wills) == 3:
        if len(p2_picked_gods_wills) < 3:
            if picked_godwill is not None:
                p2_picked_gods_wills.append(picked_godwill)
            print('p2 list', p2_picked_gods_wills)
            pick_gods_will_main(surface, players, godwill, 1)
        elif len(p2_picked_gods_wills) == 3:
            c = GamePVP(window, players, [p1_picked_gods_wills, p2_picked_gods_wills])
            c.coin_toss()
    else:
        c = GamePVP(window, players, [p1_picked_gods_wills, p2_picked_gods_wills])
        c.coin_toss()


def pick_gods_will_main(surface, players: [], godwill, player_to_pick_id):
    run = True
    next_but = Button('Next', SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.75, next_img, 0.5)
    prev_but = Button('Previous', SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.75, prev_img, 0.5)
    back_button = Button('Back', SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.25, back_img, 0.5)
    ready_button = Button('Ready', SCREEN_WIDTH * 0.85, SCREEN_HEIGHT * 0.85, ready_img, 0.5)

    if player_to_pick_id == 0:
        godwills_list = godwills_list_p1
    elif player_to_pick_id == 1:
        godwills_list = godwills_list_p2
    gd_pick = godwills_list[godwill]
    print('------------')
    print('gd_pick', gd_pick)
    gd_index = godwills_list.index(gd_pick)
    print('gd_index', gd_index)
    print('------------')
    current_player = players[player_to_pick_id]
    while run:
        CLOCK.tick(FPS)
        surface.blit(background_img, (0, 0))
        back_button.draw(surface)
        next_but.draw(surface)
        prev_but.draw(surface)
        gd_pick.draw(surface)
        ready_button.draw(surface)
        draw_text('Pick gods will', FONT, (0, 0, 0), surface, (200, 200))
        draw_text(current_player, FONT, (0, 0, 0), surface, (700, 100))
        draw_text('Opisanie', FONT, (0, 0, 0), surface, (100, 600))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gd_pick.draw(surface):
                    godwills_list.remove(gd_pick)
                    current_options_gods_will(surface, players, gd_index, gd_pick)
                    if current_player == players[0]:
                        p1_picked_gods_wills.append(gd_pick.name)
                    elif current_player == players[1]:
                        p2_picked_gods_wills.append(gd_pick.name)
                if next_but.draw(surface):
                    if gd_index == len(godwills_list) - 1:
                        current_options_gods_will(surface, players, 0, None)
                    else:
                        current_options_gods_will(surface, players, gd_index + 1, None)
                if prev_but.draw(surface):
                    if gd_index == 0:
                        current_options_gods_will(surface, players, len(godwills_list) - 1, None)
                    else:
                        current_options_gods_will(surface, players, gd_index - 1, None)
                if back_button.draw(surface):
                    client_friend.game_options(surface, players)



