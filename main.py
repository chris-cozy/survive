import pygame
import sys
import math
from random import randint
from room import Room
from screen import Screen
from player import Player
from projectile import Projectile
from enemy import Enemy

### CONSTANTS ###
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700
ROOM_WIDTH, ROOM_HEIGHT = 800, 600
BORDER_OFFSET = 15
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 20
ENEMY_WIDTH, ENEMY_HEIGHT = 15, 15
CAPTION = "survive!"
KILL_ADD = 1
SCORE_ADD = 10
MILLI_CONV = 1000
COLORS = [(41, 19, 46), (50, 20, 80), (134, 0, 41),
          (222, 0, 67), (248, 135, 255), (110, 109, 113), (255, 255, 255)]

### GAME SETUP ###
gameState = "startMenu"

difficulties = ["easy", "medium", "hard", "crazy", "impossible"]

### MAIN SCRIPT ###
pygame.init()
clock = pygame.time.Clock()

# Screen Initialization #
screen = Screen(CAPTION, SCREEN_SIZE, SCREEN_WIDTH,
                SCREEN_HEIGHT)

playing = True


### GAME LOOP ###
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False

    if gameState == "startMenu":
        screen.draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            gameState = "inGame"
            gameOver = False

    elif gameState == "inGame":
        # Room Initialization #
        room = Room(ROOM_WIDTH, ROOM_HEIGHT, COLORS[5])
        x_offset = (SCREEN_WIDTH - ROOM_WIDTH)/2
        y_offset = (SCREEN_HEIGHT - ROOM_HEIGHT)/2
        room_bottom = x_offset
        room_top = room_bottom + ROOM_HEIGHT
        room_left = y_offset
        room_right = room_left + ROOM_WIDTH
        room.set_pos(x_offset, y_offset)

        # Border Initialization #
        border = Room(ROOM_WIDTH + BORDER_OFFSET,
                      ROOM_HEIGHT + BORDER_OFFSET, COLORS[6])
        x_offset = (SCREEN_WIDTH - ROOM_WIDTH - (BORDER_OFFSET/2))/2
        y_offset = (SCREEN_HEIGHT - ROOM_HEIGHT - (BORDER_OFFSET/2))/2
        border.set_pos(x_offset, y_offset)

        # Player Initialization #
        player = Player(PLAYER_WIDTH, PLAYER_HEIGHT)
        x_offset = (SCREEN_WIDTH - PLAYER_WIDTH)/2
        y_offset = (SCREEN_HEIGHT - PLAYER_HEIGHT)/2
        player.set_pos(x_offset, y_offset)

        # Player Aim Initialization #
        aim_start = pygame.math.Vector2(player.rect.center)
        aim_end = aim_start
        aim_len = 50

        # Projectile Initialization #
        projectiles = []

        # Enemy Initialization #
        enemies = []

        # Sprite Group Initialization #
        spriteList_Room = pygame.sprite.Group()
        # spriteList_Room.add(border)
        spriteList_Room.add(room)

        spriteList_Ents = pygame.sprite.Group()
        spriteList_Ents.add(player)

        spriteList_Projs = pygame.sprite.Group()

        spriteList_Enemies = pygame.sprite.Group()

        spawnRate = 3
        time = 0
        spawnTime = 0
        hurtTime = 0
        invTime = 2
        fireRate = 1
        fireTime = 0
        inGame = True
        difficultyIndex = 0

        difficultyRate = 10
        difficultyTime = 0

        while inGame:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if((time - fireTime) > fireRate):
                        projectile = Projectile(aim_start, mouse, time)
                        projectiles.append(projectile)
                        spriteList_Projs.add(projectile)
                        fireTime = time
                        print(projectiles)

            # Player Updates #
            player.check_keys(room_bottom, room_top, room_left, room_right)
            if player.dead:
                gameState = "gameOver"
                inGame = False
                gameOver = True

            # Aim Updates #
            mouse = pygame.mouse.get_pos()
            aim_start = pygame.math.Vector2(player.rect.center)
            aim_end = aim_start + (mouse - aim_start).normalize() * aim_len

            # Difficulty Updates #
            difficulty = difficulties[difficultyIndex]
            if (difficulty == difficulties[0]):
                spawnRate = 4
            elif (difficulty == difficulties[1]):
                spawnRate = 3
            elif (difficulty == difficulties[2]):
                spawnRate = 2
            elif (difficulty == difficulties[3]):
                spawnRate = 1

            if((time - difficultyTime) > difficultyRate):
                if difficultyIndex < 4:
                    difficultyIndex += 1
                    difficultyTime = time

            # Enemy Spawn Updates #
            if ((time - spawnTime) > spawnRate):
                enemy = Enemy(ENEMY_WIDTH, ENEMY_HEIGHT)
                enemy.set_spawn(room_left, room_right,
                                room_bottom, room_top, player)
                enemies.append(enemy)
                spriteList_Enemies.add(enemy)
                spawnTime = time
                print(enemies)

            # Projectile, Enemy, and Collision Updates #
            for enem in enemies:
                enem.tracking(player)
                if pygame.sprite.collide_mask(enem, player):
                    if ((time - hurtTime) > invTime):
                        player.damage()
                        hurtTime = time

            for proj in projectiles:
                proj.update_pos()
                if (proj.life_over(time)):
                    proj.damage()
                    projectiles.remove(proj)
                for enem in enemies:
                    if pygame.sprite.collide_mask(proj, enem):
                        player.kills += KILL_ADD
                        player.score += SCORE_ADD
                        enem.damage()
                        proj.damage()
                        enemies.remove(enem)
                        projectiles.remove(proj)

            # Time Updates #
            time = math.trunc(pygame.time.get_ticks()/MILLI_CONV)

            # Screen Logic and Draws #
            screen.fill()
            screen.draw(spriteList_Room)
            screen.draw(spriteList_Ents)
            screen.draw(spriteList_Projs)
            screen.draw(spriteList_Enemies)
            screen.display_text(player, time, difficulty)

            # Draw the Aim for debugging
            # pygame.draw.line(screen.surface, (255, 0, 0), aim_start, aim_end)

            screen.flip()

            clock.tick(60)

    elif gameState == "gameOver":
        screen.draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            gameState = "inGame"
        elif keys[pygame.K_q]:
            playing = False

pygame.quit()
