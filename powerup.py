import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
COLORS = [(41, 19, 46), (50, 20, 80), (134, 0, 41),
          (222, 0, 67), (248, 135, 255)]
POWERUP_TYPES = ["speed", "health", "fireRate"]


class Powerup(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()
        self.width = 10
        self.height = 10
        self.type = type

        if (self.type == POWERUP_TYPES[0]):
            self.color = COLORS[1]
        elif (self.type == POWERUP_TYPES[1]):
            self.color = COLORS[2]
        elif (self.type == POWERUP_TYPES[2]):
            self.color = COLORS[3]

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, self.color, [
                         0, 0, self.width, self.height])
        self.rect = self.image.get_rect()

    def set_pos(self, enem):
        self.rect.x = enem.rect.x
        self.rect.y = enem.rect.y

    def damage(self):
        self.kill()
