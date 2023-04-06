import pygame

BLACK = (0, 0, 0)
SPEED = 5
LIFETIME = 1


class Projectile(pygame.sprite.Sprite):

    def __init__(self, start, mouse, spawnTime, color):
        super().__init__()
        self.width = 5
        self.height = 5
        self.spawnTime = spawnTime

        self.start = start
        self.mouse = mouse
        self.distance = self.mouse - self.start
        self.pos = pygame.math.Vector2(self.start)
        self.speed = self.distance.normalize() * SPEED

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [
                         0, 0, self.width, self.height])
        self.rect = self.image.get_rect()

    def update_pos(self):
        self.pos += self.speed
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def life_over(self, time):
        if ((time - self.spawnTime) > LIFETIME):
            return True
        return False

    def damage(self):
        self.kill()
