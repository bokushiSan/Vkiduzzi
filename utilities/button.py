import pygame


class Button:
    """
    Drawing the button in the xy coordinates using image.
    """
    def __init__(self, name, x, y, image, scale):
        """
        Initialize class variables.
        :param name: str | name of the button
        :param x: int | x-coordinate
        :param y: int | y-coordinate
        :param image: image to use as button
        :param scale: float | scale of image
        """
        width = image.get_width()
        height = image.get_height()
        self.name = name
        self.image = image
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, surface):
        """
        Drawing the button.
        :param surface: surface to draw
        :return action: bool | True if button is clicked
        """
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
