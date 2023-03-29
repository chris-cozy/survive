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

# Projectile Setup #
proj_start = pygame.math.Vector2(player.rect.center)
proj_end = proj_start
proj_len = 50
PROJ_SPEED = 5

projectiles = []

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
        elif event.type == pygame.MOUSEMOTION:
            continue
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            proj_distance = mouse - proj_start
            pos = pygame.math.Vector2(proj_start)
            proj_speed = proj_distance.normalize() * PROJ_SPEED
            projectiles.append([pos, proj_speed])

            # Updates #
    player.check_keys(room_bottom, room_top, room_left, room_right)
    # update aim
    proj_start = pygame.math.Vector2(player.rect.center)
    mouse = pygame.mouse.get_pos()
    proj_end = proj_start + (mouse - proj_start).normalize() * proj_len
    # updates all projectiles toward their destinations
    for pos, speed in projectiles:
        pos += speed

    # Screen Logic and Draws #
    screen.fill()
    screen.draw(spriteList_Room)
    screen.draw(spriteList_Ents)
    # aim
    pygame.draw.line(screen.surface, (255, 0, 0), proj_start, proj_end)
    # projectiles
    for pos, speed in projectiles:
        pos_x = int(pos.x)
        pos_y = int(pos.y)
        pygame.draw.line(screen.surface, (0, 0, 255),
                         (pos_x, pos_y), (pos_x, pos_y))

    screen.flip()

    clock.tick(60)

pygame.quit()
