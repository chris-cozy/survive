import pygame

BLACK = (0, 0, 0)
POWERUP_TYPES = ["speed", "health", "fireRate"]


class Powerup(pygame.sprite.Sprite):

    def __init__(self, type, color):
        super().__init__()
        self.width = 10
        self.height = 10
        self.type = type

        # if (self.type == POWERUP_TYPES[0]):
        #    self.color = COLORS[1]
        # elif (self.type == POWERUP_TYPES[1]):
        #    self.color = COLORS[2]
        # elif (self.type == POWERUP_TYPES[2]):
        #    self.color = COLORS[3]

        self.color = color

        self.bloomWidth = self.width + 2
        self.bloomHeight = self.height + 2
        self.bloom = pygame.Surface([self.bloomWidth, self.bloomHeight])
        self.bloom.set_alpha(75)
        self.bloom.fill(color)
        self.bloom.set_colorkey(BLACK)

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
