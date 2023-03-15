import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, BLUE, [0, 0, width, height])

        self.velocity = 5

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move_up(self, pixels):
        self.rect.y -= pixels

    def move_down(self, pixels):
        self.rect.y += pixels

    def move_left(self, pixels):
        self.rect.x -= pixels

    def move_right(self, pixels):
        self.rect.x += pixels

    def check_keys(self, pHeight, roomBottom, roomTop, roomLeft, roomRight):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if (self.rect.y > roomBottom):
                self.move_up(self.velocity)

        if keys[pygame.K_DOWN]:
            if ((self.rect.y + pHeight) < roomTop):
                self.move_down(self.velocity)

        if keys[pygame.K_LEFT]:
            if (self.rect.x > roomLeft):
                self.move_left(self.velocity)

        if keys[pygame.K_RIGHT]:
            if ((self.rect.x + pHeight) < roomRight):
                self.move_right(self.velocity)