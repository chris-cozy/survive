import pygame
from random import randint

BLACK = (0, 0, 0)
RED = (255, 0, 0)
COLORS = [(41, 19, 46), (50, 20, 80), (134, 0, 41),
          (222, 0, 67), (248, 135, 255)]


class Enemy(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.type = "base"

        self.velocity = 0
        self.speed = 3

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, COLORS[3], [
                         0, 0, self.width, self.height])

        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(self.rect.center)

        self.powerupChance = 20
        self.health = 10
        self.score = 10
        self.dead = False

    def set_spawn(self, room_left, room_right, room_bottom, room_top, player):
        self.spawnX = randint(room_left, room_right)
        self.spawnY = randint(room_bottom, room_top)

        self.distanceFromPlayer = pygame.math.Vector2(
            player.rect.center).distance_to((self.spawnX, self.spawnY))

        while (abs(self.distanceFromPlayer) < 30):
            self.spawnX = randint(room_left, room_right)
            self.spawnY = randint(room_bottom, room_top)

        self.rect.x = self.spawnX
        self.rect.y = self.spawnY
        self.pos = pygame.math.Vector2(self.rect.center)

    def tracking(self, player):
        self.safe_net = (player.width/2) + (self.width/2)
        self.distance = pygame.math.Vector2(
            player.rect.center) - pygame.math.Vector2(self.rect.center)

        if (self.distance.length() > self.safe_net):
            self.velocity = self.distance.normalize() * self.speed
            self.rect.x += self.velocity.x
            self.rect.y += self.velocity.y

            self.pos += self.rect.center

    def damage(self, player):
        self.health -= player.attackPower
        if (self.health <= 0):
            self.dead = True
            self.kill()
