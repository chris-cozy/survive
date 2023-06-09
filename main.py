import pygame
import sys
import math
from random import randint
from room import Room
from screen import Screen
from player import Player
from projectile import Projectile
from enemy import Enemy
from powerup import Powerup
from miniboss import Miniboss
from turret import Turret

### CONSTANTS ###
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700
ROOM_WIDTH, ROOM_HEIGHT = 800, 600
BORDER_OFFSET = 15
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 20
ENEMY_WIDTH, ENEMY_HEIGHT = 15, 15
MINIBOSS_WIDTH, MINIBOSS_HEIGHT = 25, 25
TURRET_WIDTH, TURRET_HEIGHT = 20, 20
CAPTION = "survive!"
KILL_ADD = 1
MILLI_CONV = 1000
COLORS = [(41, 19, 46), (50, 20, 80), (134, 0, 41),
          (222, 0, 67), (248, 135, 255), (110, 109, 113), (255, 255, 255)]
COLOR_DICT = {
    "neon blue": (31, 81, 255),
    "neon red": (255, 49, 49),
    "violet": (127, 0, 255),
    "neon orange": (255, 95, 31),
    "golden yellow": (255, 192, 0)
}

### GAME SETUP ###
gameState = "startMenu"
difficulties = ["easy", "medium", "hard", "crazy", "impossible"]
powerupTypes = ["speed", "health", "fireRate"]

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
        player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, COLOR_DICT["neon blue"])
        x_offset = (SCREEN_WIDTH - PLAYER_WIDTH)/2
        y_offset = (SCREEN_HEIGHT - PLAYER_HEIGHT)/2
        player.set_pos(x_offset, y_offset)

        # Player Aim Initialization #
        aim_start = pygame.math.Vector2(player.rect.center)
        aim_end = aim_start
        aim_len = 50

        # Projectile Initialization #
        playerProjectiles = []
        enemyProjectiles = []

        # Enemy Initialization #
        enemies = []

        # Powerup Initialization #
        powerups = []

        # Sprite Group Initialization #
        spriteList_Room = pygame.sprite.Group()
        # spriteList_Room.add(border)
        spriteList_Room.add(room)

        spriteList_Ents = pygame.sprite.Group()
        spriteList_Ents.add(player)

        spriteList_Projs = pygame.sprite.Group()

        spriteList_Enemies = pygame.sprite.Group()

        spriteList_Powerups = pygame.sprite.Group()

        spawnRate = 3
        time = 0
        rawTime = 0
        spawnTime = 0
        inGame = True

        difficultyIndex = 0
        difficultyRate = 10
        difficultyTime = 0

        while inGame:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        gameState = "gameOver"
                        inGame = False
                        gameOver = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if((rawTime - player.fireTime) > player.fireRate):
                        projectile = Projectile(
                            aim_start, mouse, time, COLOR_DICT["neon blue"])
                        playerProjectiles.append(projectile)
                        spriteList_Projs.add(projectile)
                        player.fireTime = rawTime
                        print(playerProjectiles)

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
                enemType = randint(1, 10)
                if(enemType > 6):
                    enemy = Enemy(ENEMY_WIDTH, ENEMY_HEIGHT,
                                  COLOR_DICT["neon red"])
                    enemy.set_spawn(room_left, room_right,
                                    room_bottom, room_top, player)
                    enemies.append(enemy)
                    spriteList_Enemies.add(enemy)
                    spawnTime = time
                elif(6 >= enemType > 2):
                    enemy = Turret(TURRET_WIDTH, TURRET_HEIGHT,
                                   COLOR_DICT["neon red"])
                    enemy.set_spawn(room_left, room_right,
                                    room_bottom, room_top, player)
                    enemies.append(enemy)
                    spriteList_Enemies.add(enemy)
                    spawnTime = time
                else:
                    enemy = Miniboss(
                        MINIBOSS_WIDTH, MINIBOSS_HEIGHT, COLOR_DICT["violet"])
                    enemy.set_spawn(room_left, room_right,
                                    room_bottom, room_top, player)
                    enemies.append(enemy)
                    spriteList_Enemies.add(enemy)
                    spawnTime = time
                print(enemies)

            # Projectile, Enemy, and Collision Updates #
            for enem in enemies:
                enem.tracking(player)
                if (enem.type == 'turret'):
                    if((rawTime - enem.fireTime) > enem.fireRate):
                        projectile = Projectile(
                            enem.aim_start, player.rect.center, time, COLOR_DICT["neon red"])
                        enemyProjectiles.append(projectile)
                        spriteList_Projs.add(projectile)
                        enem.fireTime = rawTime
                        print(enemyProjectiles)
                if pygame.sprite.collide_mask(enem, player):
                    if ((time - player.hurtTime) > player.invTime):
                        player.damage()
                        player.hurtTime = time

            for proj in playerProjectiles:
                proj.update_pos()
                if (proj.life_over(time)):
                    proj.damage()
                    playerProjectiles.remove(proj)
                    continue
                for enem in enemies:
                    if pygame.sprite.collide_mask(proj, enem):
                        enem.damage(player)
                        proj.damage()
                        playerProjectiles.remove(proj)
                        if enem.dead == True:
                            player.kills += KILL_ADD
                            player.score += enem.score

                            # 20% chance to spawn a random powerup
                            if (randint(0, 100) < enem.powerupChance):
                                powerup = Powerup(powerupTypes[randint(
                                    0, 2)], COLOR_DICT["golden yellow"])
                                powerup.set_pos(enem)
                                powerups.append(powerup)
                                spriteList_Powerups.add(powerup)
                                print(powerups)
                            enemies.remove(enem)

            for proj in enemyProjectiles:
                proj.update_pos()
                if (proj.life_over(time)):
                    proj.damage()
                    enemyProjectiles.remove(proj)
                if pygame.sprite.collide_mask(proj, player):
                    player.damage()
                    proj.damage()
                    enemyProjectiles.remove(proj)

         # Powerup Updates #
            for pow in powerups:
                if pygame.sprite.collide_mask(pow, player):
                    player.add_powerup(pow)
                    pow.damage()
                    powerups.remove(pow)

            # Time Updates #
            time = math.trunc(pygame.time.get_ticks()/MILLI_CONV)
            rawTime = pygame.time.get_ticks()/MILLI_CONV

            # Screen Logic and Draws #
            screen.fill()
            screen.draw(spriteList_Room)
            screen.draw(spriteList_Ents)
            screen.draw(spriteList_Projs)
            screen.draw(spriteList_Enemies)
            screen.draw(spriteList_Powerups)
            screen.display_text(player, time, difficulty)
            screen.blit(player.bloom, (pygame.math.Vector2(
                player.rect.center) - pygame.math.Vector2((player.bloomWidth)/2.0)))

            for enem in enemies:
                screen.blit(enem.bloom, (pygame.math.Vector2(
                    enem.rect.center) - pygame.math.Vector2((enem.bloomWidth)/2.0)))

            for pow in powerups:
                screen.blit(pow.bloom, (pygame.math.Vector2(
                    pow.rect.center) - pygame.math.Vector2((pow.bloomWidth)/2.0)))

            # Draw the Aim for debugging
            # pygame.draw.line(screen.surface, (255, 0, 0), aim_start, aim_end)

            screen.flip()

            clock.tick(60)

    elif gameState == "gameOver":
        screen.draw_game_over_screen(player)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            gameState = "inGame"
        elif keys[pygame.K_q]:
            playing = False

pygame.quit()
