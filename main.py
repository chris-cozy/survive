import pygame
import sys
from random import randint
from room import Room
from screen import Screen

### CONSTANTS ###
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700
ROOM_WIDTH, ROOM_HEIGHT = 800, 600
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
room.set_pos(x_offset, y_offset)

# Sprite Group Setup #
spriteList_Room = pygame.sprite.Group()
spriteList_Room.add(room)

playing = True

### GAME LOOP ###
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False

    # Screen Logic #
    screen.fill()
    screen.draw(spriteList_Room)
    screen.flip()

    clock.tick(60)

pygame.quit()
