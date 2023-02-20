import os
import pygame


def get_image(img_name):
    """
    Getting image from pics folder.
    :param img_name: name of image
    :return img_load: loaded image
    """
    image_path = os.path.join('pics', img_name)
    img_load = pygame.image.load(image_path)
    return img_load
