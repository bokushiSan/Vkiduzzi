import os
import random
import pygame
import utilities.window_gameset as cn
from utilities.button import Button
from entities.player_vs_player import PVP
from utilities.dice_gameset import list_of_cubes, start_life, number_of_throws, start_gold
from entities.player import Player
from utilities.draw_text import draw_text
from utilities.coin_toss import coin_winner
from utilities.get_image import get_image

pvp_pvp = PVP()

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

back_img = get_image('back_image.png')
enter_img = get_image('enter_image.png')
start_game_img = get_image('start_game_img.png')

next_img = get_image('next_img.png')
prev_img = get_image('prev_img.png')
pick_img = get_image('pick_img.png')
ready_img = get_image('ready_img.png')

throw_img = get_image('throw_dice.png')

helmet_img = get_image('helmet.png')
helmet_plus_img = get_image('helmet++.png')
shield_img = get_image('shield.png')
shield_plus_img = get_image('shield++.png')
axe_img = get_image('axe.png')
axe_plus_img = get_image('axe++.png')
arrow_img = get_image('arrow.png')
arrow_plus_img = get_image('arrow++.png')
thief_img = get_image('thief.png')
thief_plus_img = get_image('thief++.png')
nothing_img = get_image('nothing.png')
nothing_plus_img = get_image('nothing++.png')
finish_img = get_image('finish_move.png')

vkid_coin_img = get_image('VKID_coin.png')
uzzi_coin_img = get_image('UZZI_coin.png')
vkid_btn_img = get_image('vkid_img.png')
uzzi_btn_img = get_image('uzzi_img.png')

throw_button = Button('Throw', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, throw_img, 0.8)
next_button = Button('Next', SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.8, next_img, 0.8)
ready_button = Button('Next', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.9, ready_img, 0.8)
finish_btn = Button('Finish', SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.8, finish_img, 0.5)


vkid_coin = Button('Vkid', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, vkid_coin_img, 0.5)
uzzi_coin = Button('Uzzi', SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, uzzi_coin_img, 0.5)
vkid_button = Button('Vkid', SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.6, vkid_btn_img, 1)
uzzi_button = Button('Uzzi', SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.6, uzzi_btn_img, 1)


class GamePVP:

    def __init__(self, surface, players, god_wills):
        self.surface = surface
        self.players = players
        self.god_wills = god_wills
        self.winner = None
        self.loser = None
        self.side = None
        self.lifes = [0, 0]
        self.golds = [0, 0]

    def coin_toss(self):
        run = True
        player1, player2 = self.players
        player_throw = random.choice([player1, player2])
        player_not_throw = [i for i in [player1, player2] if i != player_throw][0]
        throw_txt = 'Player ' + player_throw + ' throwing coin'
        while run:
            CLOCK.tick(FPS)
            self.surface.blit(background_img, (0, 0))
            vkid_button.draw(self.surface)
            uzzi_button.draw(self.surface)
            draw_text(throw_txt, FONT, (0, 0, 0), self.surface, (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.4))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if vkid_button.draw(self.surface):
                        self.winner, self.loser, self.side = coin_winner('Vkid', player_throw, player_not_throw)
                        self.game_window(1)
                    if uzzi_button.draw(self.surface):
                        self.winner, self.loser, self.side = coin_winner('Uzzi', player_throw, player_not_throw)
                        self.game_window(1)

    @staticmethod
    def info(surface, rnd, winner, loser, p1, p2, p1_life, p2_life, p1_gold, p2_gold):
        round_txt = 'Round number ' + str(rnd)
        p1_life_txt = 'Life ' + str(p1_life)
        p2_life_txt = 'Life ' + str(p2_life)
        p1_gold_txt = 'Gold ' + str(p1_gold)
        p2_gold_txt = 'Gold ' + str(p2_gold)
        if rnd % 2 == 1:
            who_moves_txt = 'Player ' + winner + ' moves'
        else:
            who_moves_txt = 'Player ' + loser + ' moves'
        draw_text(round_txt, FONT, (10, 10, 60), surface, (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.1))
        draw_text(who_moves_txt, FONT, (10, 10, 60), surface,
                               (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.15))
        draw_text(p1.name, FONT, (10, 10, 60), surface,
                               (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.8))
        draw_text(p1_life_txt, FONT, (10, 10, 60), surface,
                               (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.85))
        draw_text(p1_gold_txt, FONT, (10, 10, 60), surface, (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.9))
        draw_text(p2.name, FONT, (10, 10, 60), surface,
                               (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.1))
        draw_text(p2_life_txt, FONT, (10, 10, 60), surface,
                               (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.15))
        draw_text(p2_gold_txt, FONT, (10, 10, 60), surface, (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.2))


    def game_window(self, rnd):
        run = True
        if rnd == 1:
            p1_life = p2_life = start_life
            p1_gold = p2_gold = start_gold
        else:
            p1_life, p2_life = self.lifes
            p1_gold, p2_gold = self.golds
        p1 = Player(self.players[0], list_of_cubes, p1_life, p1_gold)
        p2 = Player(self.players[1], list_of_cubes, p2_life, p2_gold)
        while run:
            CLOCK.tick(FPS)
            self.surface.blit(background_img, (0, 0))
            self.info(self.surface, rnd, self.winner, self.loser, p1, p2, p1_life, p2_life, p1_gold, p2_gold)
            throw_button.draw(self.surface)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if throw_button.draw(self.surface):
                        if (rnd % 2 == 1 and self.winner == p1.name) or (rnd % 2 == 0 and self.loser == p1.name):
                            self.throwing(rnd, 1, p1, p2, 1, True)
                        elif (rnd % 2 == 1 and self.loser == p1.name) or (rnd % 2 == 0 and self.winner == p1.name):
                            self.throwing(rnd, 1, p2, p1, 1, False)

    def throwing(self, rnd, th, player_turn, player_chill, duo, how):
        run = True
        if rnd == 1:
            p1_life = p2_life = start_life
            p1_gold = p2_gold = start_gold
        else:
            p1_life, p2_life = self.lifes
            p1_gold, p2_gold = self.golds
        move1 = player_turn
        move2 = player_chill
        if th < number_of_throws:
            move1.throw_cube(th)
            picked_sides = list()
            while run:
                CLOCK.tick(FPS)
                self.surface.blit(background_img, (0, 0))
                if how:
                    self.info(self.surface, rnd, self.winner, self.loser, move1, move2, p1_life, p2_life, p1_gold, p2_gold)
                else:
                    self.info(self.surface, rnd, self.winner, self.loser, move2, move1, p1_life, p2_life, p1_gold, p2_gold)
                ready_button.draw(self.surface)
                draw_text(move1.name, FONT, (10, 10, 60), self.surface, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
                for idx, img in enumerate(move1.dice_sides):
                    img_pathname = os.path.join('pics', img.name.name + '.png')
                    image = pygame.image.load(img_pathname)
                    self.surface.blit(image, (200 * idx, 200))
                for but in move1.dice_buttons:
                    but.draw(self.surface)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for num_of_dice, dice in enumerate(move1.dice_buttons):
                            if dice.draw(self.surface):
                                picked_sides.append(num_of_dice)
                        if ready_button.draw(self.surface):
                            th += 1
                            for ps in set(picked_sides):
                                move1.dice_sides.append(move1.dice_buttons[ps])
                            move1.cubes_list = [i for j, i in enumerate(move1.cubes_list) if j not in picked_sides]
                            self.throwing(rnd, th, move1, move2, duo, how)
        elif th == number_of_throws:
            move1.throw_cube(th)
            picked_sides = list()
            while run:
                CLOCK.tick(FPS)
                self.surface.blit(background_img, (0, 0))
                if how:
                    self.info(self.surface, rnd, self.winner, self.loser, move1, move2, p1_life, p2_life, p1_gold,
                              p2_gold)
                else:
                    self.info(self.surface, rnd, self.winner, self.loser, move2, move1, p1_life, p2_life, p1_gold,
                              p2_gold)
                if duo == 1:
                    finish_btn.draw(self.surface)
                if duo == 2:
                    next_button.draw(self.surface)
                for idx, img in enumerate(move1.dice_sides):
                    img_pathname = os.path.join('pics', img.name.name + '.png')
                    image = pygame.image.load(img_pathname)
                    self.surface.blit(image, (200 * idx, 200))
                for but in move1.dice_buttons:
                    but.draw(self.surface)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for num_of_dice, dice in enumerate(move1.dice_buttons):
                            if dice.draw(self.surface):
                                picked_sides.append(num_of_dice)
                        if duo == 1:

                            if finish_btn.draw(self.surface):
                                if how:
                                    self.throwing(rnd, 1, move2, move1, 2, False)
                                else:
                                    self.throwing(rnd, 1, move2, move1, 2, True)
                        if duo == 2:
                            # print('m1 sides', [i.name.name for i in move1.dice_sides])
                            # print('m2 sides', [i.name.name for i in move2.dice_sides])
                            if how:
                                pvp_pvp.pvp(move1, move2)
                                # print('Игрок', move1.name, 'кинул', [i.name.name for i in move1.dice_sides])
                                # print('Игрок', move2.name, 'кинул', [i.name.name for i in move2.dice_sides])
                                # print('Игрок', move1.name, 'наносит урон', pvp_pvp.powaaa(move1, move2)[0])
                                # print('Игрок', move2.name, 'наносит урон', pvp_pvp.powaaa(move1, move2)[1])
                                # p1_life = move1.life
                                # p2_life = move2.life
                            else:
                                pvp_pvp.pvp(move2, move1)
                            print('Игрок', move1.name, 'кинул', [i.name.name for i in move1.dice_sides])
                            print('Игрок', move2.name, 'кинул', [i.name.name for i in move2.dice_sides])
                            print('Игрок', move1.name, 'наносит урон', pvp_pvp.powaaa(move1, move2)[0])
                            print('Игрок', move2.name, 'наносит урон', pvp_pvp.powaaa(move1, move2)[1])
                            p1_life = move1.life
                            p2_life = move2.life
                            if next_button.draw(self.surface):
                                rnd += 1
                                self.lifes[0] = p1_life
                                self.lifes[1] = p2_life
                                self.golds[0] = p1_gold
                                self.golds[1] = p2_gold
                                self.game_window(rnd)
