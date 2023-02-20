import pygame
import os

def get_image(img_name):
    image_path = os.path.join('pics', img_name)
    return pygame.image.load(image_path)