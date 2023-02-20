import random

from entities.dice_edges import Helmet, Shield, Axe, Arrow, Thief, Nothing

cube_one = [Helmet(True), Shield(True), Axe(), Arrow(), Thief(), Nothing()]
cube_two = [Helmet(), Shield(), Axe(True), Arrow(True), Thief(), Nothing()]
cube_three = [Helmet(), Shield(), Axe(), Arrow(), Thief(True), Nothing(True)]
cube_four = [Helmet(), Shield(True), Axe(True), Arrow(), Thief(), Nothing()]
cube_five = [Helmet(), Shield(), Axe(), Arrow(True), Thief(True), Nothing()]
cube_six = [Helmet(True), Shield(), Axe(), Arrow(), Thief(), Nothing(True)]

list_of_cubes = [cube_one, cube_two, cube_three, cube_four, cube_five, cube_six]
random.shuffle(list_of_cubes)

start_life = 10
start_gold = 0
number_of_throws = 3

bot_name = ['Vkiddy', 'Pakito Snuesolini', 'Vkridrich Snuestche', 'Tommy Snueselby']