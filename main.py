import pygame
import sys
from random import randint
from room import Room
from screen import Screen
from player import Player

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

# Sprite Group Setup #
spriteList_Room = pygame.sprite.Group()
spriteList_Room.add(room)

spriteList_Ents = pygame.sprite.Group()
spriteList_Ents.add(player)

playing = True

### GAME LOOP ###
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False

    player.check_keys(room_bottom, room_top, room_left, room_right)

    # Screen Logic #
    screen.fill()
    screen.draw(spriteList_Room)
    screen.draw(spriteList_Ents)
    screen.flip()

    clock.tick(60)

pygame.quit()
