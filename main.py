import math
import pygame
import random
from pygame import mixer 
from character import Character

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# screen initializtion
screen_width = 800
screen_height = 600
background_color = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))

# title and icon
pygame.display.set_caption("Space Cop")
icon = pygame.image.load("image/galaxy.png")
pygame.display.set_icon(icon)

current_score = 0


# player
player_img = pygame.image.load("image/battleship.png")
player_x = 370
player_y = 480
player_x_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))

# enemy
enemy_img = pygame.image.load("image/enemy.png")
enemy_x = random.randint(0,780)
enemy_y = random.randint(20,50)
enemy_x_change = 0.3
enemy_y_change = 5

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

# bullet 
bullet_state = "ready"
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 1
bullet_img = pygame.image.load("image/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (bullet_img.get_width()*2, bullet_img.get_height()*2))
bullet_rect = bullet_img.get_rect()

# bullet = None

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img,(x,y))

def spawn_enemy():
    enemy(enemy_x, enemy_y)

def collision(x1, y1, x2, y2):
    distance = math.sqrt( math.pow(x2-x1,2) + math.pow(y2-y1,2))
    if distance < 10:
        return True
    return False

def show_score(score):
    textsurface = myfont.render('Score: '+str(score), False, (255, 255, 255))
    screen.blit(textsurface, (10,10))

# infinite game loop 
run = True
while run:
    
    screen.fill(background_color)

    show_score(current_score)

    enemy_x += enemy_x_change
    if enemy_x >= 780:
        enemy_x = 780
        enemy_x_change = -0.3
    if enemy_x <= 1:
        enemy_x = 4
        enemy_x_change = 0.3
     

    player_x += player_x_change
    if player_x >= 770:
        player_x = 770
    if player_x <= 0:
        player_x = 0
    
   
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= 2
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state == "ready":
        bullet_sound = mixer.Sound("sounds/laser.wav")
        bullet_sound.play()
        bullet_x = player_x
        fire_bullet(bullet_x, bullet_y)  

    if collision(enemy_x, enemy_y,bullet_x, bullet_y):
        current_score += 1
        spawn_enemy()

    # event check
    for event in pygame.event.get():
        # cross button click event
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_LEFT:
                player_x_change = -2
            if event.key == pygame.K_RIGHT:
                player_x_change = 2
            if event.key == pygame.K_SPACE:
                pass                 
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0   

    enemy(enemy_x, enemy_y)
    player(player_x,player_y)

    pygame.display.update()
    
# quit game outside of the loop
pygame.quit()

# import math
# import random

# import pygame
# from pygame import mixer

# # Intialize the pygame
# pygame.init()

# # create the screen
# screen = pygame.display.set_mode((800, 600))

# # Background
# background = (0,0,0) # pygame.image.load('background.png')

# # Sound
# # mixer.music.load("background.wav")
# # mixer.music.play(-1)

# # Caption and Icon
# pygame.display.set_caption("Space Invader")
# icon = pygame.image.load('image/galaxy.png')
# pygame.display.set_icon(icon)

# # Player
# playerImg = pygame.image.load('image/battleship.png')
# playerX = 370
# playerY = 480
# playerX_change = 0

# # Enemy
# enemyImg = []
# enemyX = []
# enemyY = []
# enemyX_change = []
# enemyY_change = []
# num_of_enemies = 2

# for i in range(num_of_enemies):
#     enemyImg.append(pygame.image.load('image/enemy.png'))
#     enemyX.append(random.randint(0, 736))
#     enemyY.append(random.randint(50, 150))
#     enemyX_change.append(1)
#     enemyY_change.append(10)

# # Bullet

# # Ready - You can't see the bullet on the screen
# # Fire - The bullet is currently moving

# bulletImg = pygame.image.load('image/bullet.png')
# bulletX = 0
# bulletY = 480
# bulletX_change = 0
# bulletY_change = 5
# bullet_state = "ready"

# # Score

# score_value = 0
# font = pygame.font.Font('freesansbold.ttf', 32)

# textX = 10
# testY = 10

# # Game Over
# over_font = pygame.font.Font('freesansbold.ttf', 64)


# def show_score(x, y):
#     score = font.render("Score : " + str(score_value), True, (255, 255, 255))
#     screen.blit(score, (x, y))


# def game_over_text():
#     over_text = over_font.render("GAME OVER", True, (255, 255, 255))
#     screen.blit(over_text, (200, 250))


# def player(x, y):
#     screen.blit(playerImg, (x, y))


# def enemy(x, y, i):
#     screen.blit(enemyImg[i], (x, y))


# def fire_bullet(x, y):
#     global bullet_state
#     bullet_state = "fire"
#     screen.blit(bulletImg, (x + 16, y + 10))


# def isCollision(enemyX, enemyY, bulletX, bulletY):
#     distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
#     if distance < 27:
#         return True
#     else:
#         return False


# # Game Loop
# running = True
# while running:

#     # RGB = Red, Green, Blue
#     screen.fill((0, 0, 0))
#     # Background Image
#     # screen.blit(background)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         # if keystroke is pressed check whether its right or left
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 playerX_change = -5
#             if event.key == pygame.K_RIGHT:
#                 playerX_change = 5
#             if event.key == pygame.K_SPACE:
#                 if bullet_state is "ready":
#                     # bulletSound = mixer.Sound("laser.wav")
#                     # bulletSound.play()
#                     # Get the current x cordinate of the spaceship
#                     bulletX = playerX
#                     fire_bullet(bulletX, bulletY)

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 playerX_change = 0

#     # 5 = 5 + -0.1 -> 5 = 5 - 0.1
#     # 5 = 5 + 0.1

#     playerX += playerX_change
#     if playerX <= 0:
#         playerX = 0
#     elif playerX >= 736:
#         playerX = 736

#     # Enemy Movement
#     for i in range(num_of_enemies):

#         # Game Over
#         if enemyY[i] > 440:
#             for j in range(num_of_enemies):
#                 enemyY[j] = 2000
#             game_over_text()
#             break

#         enemyX[i] += enemyX_change[i]
#         if enemyX[i] <= 0:
#             enemyX_change[i] = 4
#             enemyY[i] += enemyY_change[i]
#         elif enemyX[i] >= 736:
#             enemyX_change[i] = -4
#             enemyY[i] += enemyY_change[i]

#         # Collision
#         collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
#         if collision:
#             # explosionSound = mixer.Sound("explosion.wav")
#             # explosionSound.play()
#             bulletY = 480
#             bullet_state = "ready"
#             score_value += 1
#             enemyX[i] = random.randint(0, 736)
#             enemyY[i] = random.randint(50, 150)

#         enemy(enemyX[i], enemyY[i], i)

#     # Bullet Movement
#     if bulletY <= 0:
#         bulletY = 480
#         bullet_state = "ready"

#     if bullet_state is "fire":
#         fire_bullet(bulletX, bulletY)
#         bulletY -= bulletY_change

#     player(playerX, playerY)
#     show_score(textX, testY)
#     pygame.display.update()
