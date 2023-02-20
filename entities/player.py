import random
import pygame
import os
from utilities.button import Button
from utilities.dice_gameset import number_of_throws
from utilities.window_gameset import SCREEN_HEIGHT, SCREEN_WIDTH


class Player:

    def __init__(self, name, cubes_list, start_life, start_gold):
        self.name = name
        self.start_first = False
        self.life = start_life
        self.gold = start_gold
        self.cubes_list = cubes_list
        self.dice_sides = list()
        self.dice_buttons = list()

    def throw_cube(self, throw_number):
        self.dice_buttons = list()
        if throw_number < number_of_throws:
            pre_dice_sides = list()
            dice_sides_imgs = list()
            for number, cube_side in enumerate(self.cubes_list):
                cube_side_up = random.choice(cube_side)
                cube_name = cube_side_up.name
                pre_dice_sides.append(cube_side_up)
                img_pathname = os.path.join('pics', cube_name + '.png')
                img = pygame.image.load(img_pathname)
                dice_sides_imgs.append(img)
            for num, img in enumerate(dice_sides_imgs):
                but = Button(pre_dice_sides[num], SCREEN_WIDTH * 0.3 + 100 * num, SCREEN_HEIGHT * 0.8, img, 0.7)
                self.dice_buttons.append(but)
        elif throw_number == number_of_throws:
            pre_dice_sides = list()
            dice_sides_imgs = list()
            for number, cube_side in enumerate(self.cubes_list):
                cube_side_up = random.choice(cube_side)
                cube_name = cube_side_up.name
                pre_dice_sides.append(cube_side_up)
                img_pathname = os.path.join('pics', cube_name + '.png')
                img = pygame.image.load(img_pathname)
                dice_sides_imgs.append(img)
            for num, img in enumerate(dice_sides_imgs):
                but = Button(pre_dice_sides[num], 500 + 100 * num, SCREEN_HEIGHT * 0.7, img, 0.7)
                self.dice_buttons.append(but)
                self.dice_sides.append(but)
        else:
            print('Ошибка')
            exit()