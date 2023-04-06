import pygame
from random import randint

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(41, 19, 46), (50, 20, 80), (134, 0, 41),
          (222, 0, 67), (248, 135, 255), (14, 217, 246)]
FONT_SIZE = 35


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

    def display_text(self, player, time, difficulty):
        font = pygame.font.Font("cyber.ttf", FONT_SIZE)
        text = font.render(str(player.score) + "  score", 1, WHITE)
        self.surface.blit(text, ((self.screenWidth/8), 10))

        pygame.draw.rect(self.surface, (255, 0, 0),
                         [((self.screenWidth/4) * 2) - (player.maxHealth/2), 10, player.maxHealth, 15])
        pygame.draw.rect(self.surface, (0, 128, 0),
                         [((self.screenWidth/4) * 2) - (player.maxHealth/2), 10, player.maxHealth - (1 * ((player.maxHealth - player.health))), 15])

        text = font.render(str(time) + "  seconds", 1, WHITE)
        self.surface.blit(text, ((self.screenWidth/4) * 3, 10))

        text = font.render(difficulty, 1, WHITE)
        self.surface.blit(
            text, ((self.screenWidth/2) - (text.get_width()/2), (self.screenHeight - 50)))

    def draw_start_menu(self):
        self.surface.fill((0, 0, 0))
        font = pygame.font.Font("cyber.ttf", FONT_SIZE)
        title = font.render('SURV!V3', True, COLORS[randint(0, 5)])
        start_button = font.render(
            'Press Space to Start', True, WHITE)
        self.surface.blit(title, (self.screenWidth/2 - title.get_width() /
                                  2, self.screenHeight/2 - title.get_height()/2))
        self.surface.blit(start_button, (self.screenWidth/2 - start_button.get_width() /
                                         2, self.screenHeight/2 + start_button.get_height()/2))
        pygame.display.update()

    def draw_game_over_screen(self):
        self.surface.fill((0, 0, 0))
        font = pygame.font.Font("cyber.ttf", FONT_SIZE)
        title = font.render('Game Over', True, (255, 255, 255))
        restart_button = font.render('R - Restart', True, (255, 255, 255))
        quit_button = font.render('Q - Quit', True, (255, 255, 255))
        self.surface.blit(title, (self.screenWidth/2 - title.get_width() /
                                  2, self.screenHeight/2 - title.get_height()/3))
        self.surface.blit(restart_button, (self.screenWidth/2 - restart_button.get_width() /
                                           2, self.screenHeight/1.9 + restart_button.get_height()))
        self.surface.blit(quit_button, (self.screenWidth/2 - quit_button.get_width() /
                                        2, self.screenHeight/2 + quit_button.get_height()/2))
        pygame.display.update()

    def flip(self):
        pygame.display.flip()
