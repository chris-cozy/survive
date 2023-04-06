import pygame
from random import randint

BLACK = (0, 0, 0)


class Turret(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.type = "turret"

        self.velocity = 0
        self.speed = 3

        self.bloomWidth = width + 4
        self.bloomHeight = height + 4
        self.bloom = pygame.Surface([self.bloomWidth, self.bloomHeight])
        self.bloom.set_alpha(75)
        self.bloom.fill(color)
        self.bloom.set_colorkey(BLACK)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [
                         0, 0, self.width, self.height])

        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(self.rect.center)

        self.fireTime = 0
        self.fireRate = 2
        self.aim_start = 0
        self.aim_end = 0
        self.powerupChance = 50
        self.health = 30
        self.score = 25
        self.dead = False

    def set_spawn(self, room_left, room_right, room_bottom, room_top, player):
        self.spawnX = randint(room_left, room_right)
        self.spawnY = randint(room_bottom, room_top)

        self.distanceFromPlayer = pygame.math.Vector2(
            player.rect.center).distance_to((self.spawnX, self.spawnY))

        while (abs(self.distanceFromPlayer) < 50):
            self.spawnX = randint(room_left, room_right)
            self.spawnY = randint(room_bottom, room_top)

        self.rect.x = self.spawnX
        self.rect.y = self.spawnY
        self.pos = pygame.math.Vector2(self.rect.center)

    def tracking(self, player):
        # Aim Initialization #
        self.aim_start = pygame.math.Vector2(self.rect.center)
        self.aim_len = 30

        self.player_pos = pygame.math.Vector2(player.rect.center)
        self.aim_end = self.aim_start + \
            (self.player_pos - self.aim_start).normalize() * self.aim_len

    def damage(self, player):
        self.health -= player.attackPower
        if (self.health <= 0):
            self.dead = True
            self.kill()
