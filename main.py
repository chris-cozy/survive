import pygame
import sys
from random import randint
from room import Room
from screen import Screen
from player import Player
from projectile import Projectile

### CONSTANTS ###
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700
ROOM_WIDTH, ROOM_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 20
CAPTION = "survive!"

pygame.init()
clock = pygame.time.Clock()

# Screen Initialization #
screen = Screen(CAPTION, SCREEN_SIZE, SCREEN_WIDTH,
                SCREEN_HEIGHT)

# Room Initialization #
room = Room(ROOM_WIDTH, ROOM_HEIGHT)
x_offset = (SCREEN_WIDTH - ROOM_WIDTH)/2
y_offset = (SCREEN_HEIGHT - ROOM_HEIGHT)/2
room_bottom = x_offset
room_top = room_bottom + ROOM_HEIGHT
room_left = y_offset
room_right = room_left + ROOM_WIDTH
room.set_pos(x_offset, y_offset)

# Player Setup #
player = Player(PLAYER_WIDTH, PLAYER_HEIGHT)
x_offset = (SCREEN_WIDTH - PLAYER_WIDTH)/2
y_offset = (SCREEN_HEIGHT - PLAYER_HEIGHT)/2
player.set_pos(x_offset, y_offset)

# Debug Player Aim Setup #
aim_start = pygame.math.Vector2(player.rect.center)
aim_end = aim_start
aim_len = 50
PROJ_SPEED = 5

projectiles = []

# Sprite Group Setup #
spriteList_Room = pygame.sprite.Group()
spriteList_Room.add(room)

spriteList_Ents = pygame.sprite.Group()
spriteList_Ents.add(player)

spriteList_Projs = pygame.sprite.Group()

playing = True

### GAME LOOP ###
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            projectile = Projectile(aim_start, mouse)
            projectiles.append(projectile)
            spriteList_Projs.add(projectile)

    # Player Updates #
    player.check_keys(room_bottom, room_top, room_left, room_right)

    # Aim Updates #
    mouse = pygame.mouse.get_pos()
    aim_start = pygame.math.Vector2(player.rect.center)
    aim_end = aim_start + (mouse - aim_start).normalize() * aim_len

    # Projectile Updates
    for proj in projectiles:
        proj.update_pos()

    # Screen Logic and Draws #
    screen.fill()
    screen.draw(spriteList_Room)
    screen.draw(spriteList_Ents)
    screen.draw(spriteList_Projs)

    # Draw the Aim
    pygame.draw.line(screen.surface, (255, 0, 0), aim_start, aim_end)

    screen.flip()

    clock.tick(60)

pygame.quit()
