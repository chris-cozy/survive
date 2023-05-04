# SURVIVE
<img src="media\survive.png" width="500"/>

### Setup Instructions

In order to run the game, `python 3.8.3`, and `pygame 2.1.2` are needed. Once those are installed, follow these commands:

- To play the game, first download the codebase as a zip file from the github page.
- Using your pc terminal, navigate to the game’s directory `survive`.
- Once in the directory, run the command `python main.py`

### Game Controls

To move, use the `WASD` keyset, for `Up, Left, Down, Right`, respectively.

To aim, use the mouse.

To shoot a projectile, click the left mouse button.

## Game Design

This game is designed to be a simple yet difficult 2D roguelike, with the gameplay being reminiscent of the flash game era. The game contains a cyberpunk style theme, which can be seen in the stylization and color choices. Due to limited pygame knowledge and experience, understandin the library was the main focus during development, with visuals taking a lower priority. All entities in the game are simple squares. Ironically this contributed to the game’s flash era inspiration and was not changed.

There is no storyline, and the gameplay loop is simple, yet true to the game’s type. The protagonist of the game is the player, and their goal is to survive as long as possible. The player spawns in a single room and must kill the enemies as they spawn in. To do this, they aim and shoot projectiles. If the player is touched by an enemy, they will lose health. As they kill enemies, there is a chance for each enemy to spawn a randomized powerup on death. The player can collect these powerups to gain strengthas they fight. The longer they survive, the greater their score. Once the player’s health reaches zero, the game is over and they can choose to start again and quit.

The sole goal of the game is to amass the highest score.

While the player is alive, their fire rate, speed, score, time survived, and health can be viewed at the top of the screen.

The available power-ups are:

- Fire rate upgrade - Decreases firing cooldown
- Damage upgrade - Increases shot damage
- Speed upgrade- Increases movement speed
- Health upgrade - Increases health amount

As time progresses, the number of enemies will increase, as well as their strength and

health. There are multiple enemy types as well.

- Base enemy - Small and weak, and moves faster
- Turret enemy - Stationary, periodically firing projectiles at the player
- Miniboss - Large and strong, and moves slow

The gimmick is the enemy system, with different enemy classes, spawn percentages, and powerup drop rates. Another gimmick could be the makeshift bloom added to the entities. Another gimmick could be the difficulty system, which is similar to RoR2’s in the fact that the difficulty is tier structured, and increases with time.

## Game Design Changes

The game has not strayed too far from its original design, but there have been a few changes throughout development.

When proposed, the plan was for the setting to be a procedurally generated multi-room dungeon, with procedurally generated obstacles in the room. Due to limited time and pygame knowledge, these features were removed, as well as the distraction item powerup idea. The breakaway enemy type was also removed, due to the setting now being a single room. This enemy type was replaced with the stationary turret enemy type. These changes also rendered the minimap feature unnecessary, so that was removed as well. The UI now consists of the time survived and the player’s score, health, and statistics.

The gimmick of the game is no longer procedural map generation, but rather the enemy system, with different enemy classes, spawn percentages, and powerup drop rates.

Another gimmick could be the difficulty system, which takes inspiration from Risk of Rain 2. The difficulty is tier structured, and increases with time. Another gimmick could be the makeshift bloom added to the entities.

The title and end game screens became solidified as development continued, and the main game loop was restructured to support them.

## Game Documentation

### Classes

Enemy

- __init__
- set_spawn
- tracking
- damage

Miniboss

- __init__
- set_spawn
- tracking
- damage

Turret

- __init__
- set_spawn
- tracking
- damage

Player

- __init__
- set_pos
- move_up
- move_down
- move_left
- move_right
- check_keys
- damage
- add_powerup

Powerup

- __init__
- set_pos
- damage

Projectile

- __init__
- update_pos
- life_over
- damage

Room

- __init__
- set_pos

Screen

- __init__
- fill
- draw
- blit
- display_text
- draw_start_menu
- draw_game_over_screen
- flip

### MVC
The game takes player input through the mouse and keyboard, which is handled within `main.py` by the respective objects.

`main.py` is the model and handles all game logic.

Output to the screen is handled by a `screen` object, which draws spirites and displays text.

### Bugs and Flaws

There is currently a bug with the game timer, as it doesn’t reset when the game restarts. This is likely a simple code logic fix.

Sometimes when screen recording, the game will spontaneously crash.

### Tools

The tools used during development:

- Git/Github - version control
- VSCode - code implementation

## Developer Contributions

There was only one developer working on this project, which is me.

### Timeline

Milestone 1: March 29

- Base game screen and player movement mechanics implemented.
    - Game screen - March 12, 2023
    - Player movement mechanics - March 22, 2023

Milestone 2: April 6

- Player shooting mechanics and base enemy implemented.
    - Shooting mechanics - April 6, 2023
        - Aim system completed
    - Base enemy - April 6, 2023

Milestone 3: April 12

- Timer, score, powerups implemented
    - Timer and score - April 5, 2023
    - Powerups - April 12, 2023

Final Game Submission: May 3rd

- Completed and polished game - May 2, 2023
- Completed Game Document game - May 2, 2023

Final Exam Presentation & Submission: May 4

- Presentation materials (e.g. slides, videos)
