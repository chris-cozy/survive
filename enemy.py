import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

        self.velocity = 0
        self.speed = 3

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, RED, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(self.rect.center)

        self.dead = False

    def __del__(self):
        print("Enemy destroyed")

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.pos = pygame.math.Vector2(self.rect.center)

    def tracking(self, player):
        self.distance = pygame.math.Vector2(
            player.rect.center) - pygame.math.Vector2(self.rect.center)
        self.velocity = self.distance.normalize() * self.speed

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.pos += self.rect.center

    def die(self):
        if self.dead == True:
            self.kill()
