import pygame

BLACK = (0, 0, 0)
GREY = (128, 128, 128)


class Room(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, GREY, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
