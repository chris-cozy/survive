import pygame

BLACK = (0, 0, 0)

HEALTH = 100
ENEMY_DAMAGE = 50
POWERUP_TYPES = ["speed", "health", "fireRate"]


class Player(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
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

        self.velocity = 5
        self.kills = 0
        self.score = 0
        self.maxHealth = HEALTH
        self.health = HEALTH
        self.attackPower = 10
        self.dead = False
        self.fireRate = 1
        self.fireTime = 0

        self.invTime = 1
        self.hurtTime = 0

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    # MOVEMENT #

    def move_up(self, pixels):
        self.rect.y -= pixels

    def move_down(self, pixels):
        self.rect.y += pixels

    def move_left(self, pixels):
        self.rect.x -= pixels

    def move_right(self, pixels):
        self.rect.x += pixels

    def check_keys(self, roomBottom, roomTop, roomLeft, roomRight):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if (self.rect.y > roomBottom):
                self.move_up(self.velocity)

        if keys[pygame.K_s]:
            if ((self.rect.y + self.height) < roomTop):
                self.move_down(self.velocity)

        if keys[pygame.K_a]:
            if (self.rect.x > roomLeft):
                self.move_left(self.velocity)

        if keys[pygame.K_d]:
            if ((self.rect.x + self.width) < roomRight):
                self.move_right(self.velocity)

    # COMBAT #

    def damage(self):
        self.health -= ENEMY_DAMAGE
        if self.health <= 0:
            self.dead = True
            self.kill()

    def add_powerup(self, pow):
        if (pow.type == POWERUP_TYPES[0]):
            self.velocity += 2
        elif (pow.type == POWERUP_TYPES[1]):
            self.health += 25
        elif (pow.type == POWERUP_TYPES[2]):
            self.fireRate -= 0.10
