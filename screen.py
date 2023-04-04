import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 50


class Screen():

    def __init__(self, caption, screenSize, screenWidth, screenHeight):
        super().__init__()

        pygame.display.set_caption(caption)

        self.surface = pygame.display.set_mode(screenSize)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screenColor = BLACK

    def fill(self):
        self.surface.fill(self.screenColor)

    def draw(self, spriteList):
        spriteList.draw(self.surface)

    def display_text(self, player, time):
        font = pygame.font.Font(None, FONT_SIZE)
        text = font.render("Kills: " + str(player.kills), 1, WHITE)
        self.surface.blit(text, (self.screenWidth/4, 10))
        text = font.render("Health: " + str(player.health), 1, WHITE)
        self.surface.blit(text, ((self.screenWidth/4) * 2, 10))
        text = font.render("Time: " + str(time), 1, WHITE)
        self.surface.blit(text, ((self.screenWidth/4) * 3, 10))

    def flip(self):
        pygame.display.flip()
