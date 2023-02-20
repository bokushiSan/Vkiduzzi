import os
import pygame
import random
from utilities.button import Button
from utilities.window_gameset import SCREEN_HEIGHT, SCREEN_WIDTH


class Player:
    """
    Player, who has own name, values of start life and gold, list of all dices. Player can throw dice.
    """
    def __init__(self, name, cubes_list, start_life, start_gold):
        """
        Initialize class variables.
        :param name: str | player's name
        :param cubes_list: list | list of dices
        :param start_life: int | value of start life
        :param start_gold: int | value of start gold
        """
        self.name = name
        self.life = start_life
        self.gold = start_gold
        self.cubes_list = cubes_list
        self.dice_sides = list()
        self.dice_buttons = list()

    def throw_cube(self, throw_number):
        """
        A method that allows throwing a dice. Accepts the roll number as an input. If the roll is the first or second,
        it allows to choose which dice the player wants to keep. If the roll is third, then leaves all remaining
        dice on the table.
        :param throw_number: int | number of throw
        """
        self.dice_buttons = list()
        if throw_number < 3:
            pre_dice_sides = list()
            dice_sides_images = list()
            for number, cube_side in enumerate(self.cubes_list):
                cube_side_up = random.choice(cube_side)
                cube_name = cube_side_up.name
                pre_dice_sides.append(cube_side_up)
                img_pathname = os.path.join('pics', cube_name + '.png')
                img = pygame.image.load(img_pathname)
                dice_sides_images.append(img)
            for num, img in enumerate(dice_sides_images):
                but = Button(pre_dice_sides[num], SCREEN_WIDTH * 0.3 + 100 * num, SCREEN_HEIGHT * 0.8, img, 0.7)
                self.dice_buttons.append(but)
        elif throw_number == 3:
            pre_dice_sides = list()
            dice_sides_images = list()
            for number, cube_side in enumerate(self.cubes_list):
                cube_side_up = random.choice(cube_side)
                cube_name = cube_side_up.name
                pre_dice_sides.append(cube_side_up)
                img_pathname = os.path.join('pics', cube_name + '.png')
                img = pygame.image.load(img_pathname)
                dice_sides_images.append(img)
            for num, img in enumerate(dice_sides_images):
                but = Button(pre_dice_sides[num], 500 + 100 * num, SCREEN_HEIGHT * 0.7, img, 0.7)
                self.dice_buttons.append(but)
                self.dice_sides.append(but)
