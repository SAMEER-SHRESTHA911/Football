from turtle import position
import pygame
import random
import math
from pygame import mixer
import time

# starting the game
pygame.init()

# creating the window
screen = pygame.display.set_mode((800, 545))

# changing the title and logo
pygame.display.set_caption("Free Kick")
icon = pygame.image.load("./images/icon.png")
pygame.display.set_icon(icon)

# changing the background
back_ground = pygame.image.load("./images/new_800x545.jpg")

# background music
mixer.music.load('./sounds/MATAFAKA.mp3')
mixer.music.play(-1)

# creating the player
playerImg = pygame.image.load("./images/player.png")
playerX = 370
playerY = 480
playerX_Change = 0

# score
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 30
texty = 30

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 32)

# creating opponents
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10
opp_spacing = 150
# changing position of opponents
for i in range(num_of_enemies):
    for row in range(3):
        enemyImg = pygame.image.load("./images/standing.png")
        if row == 1:
            enemyX.append(200 + opp_spacing * 1.25)
        elif row == 2:
            enemyX.append(250 + opp_spacing * i)
        elif row == 3:
            enemyX.append(500 + opp_spacing * i)
        enemyY.append(350 - row * 100)
        enemyX_change.append(0.4)
        enemyY_change.append(0)

# creating the goalpost
goalpostImg = pygame.image.load("./images/post.png")
post_rect = goalpostImg.get_rect()

# loading the ball
ballImg = pygame.image.load('./images/ball.png')
ballX = playerX
ballY = playerY
ball_State = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))


def ball_movement(a, b):
    screen.blit(ballImg, (a, b))


def opponent(x, y, i):
    screen.blit(enemyImg, (x, y))


def goal_detection(ballA, ballB):
    global no_ofgoals
    if ballB < 50:
        if (ballA > 310) and (ballA < 485):
            score_chances.append(1)
        else:
            score_chances.append(0)

    goal_true = score_chances.count(1)
    goal_false = score_chances.count(0)
    if goal_true > goal_false:
        no_ofgoals += 1
        score_chances.clear()
        # rakhna maan thiyo tara adkinxa program
        # goal_sound = mixer.Sound('./sounds/goal.mp3')
        # goal_sound.play()

def iscollision(enemyx, enemyy, ballx, bally):
            distance_ball = math.sqrt((math.pow(enemyx - ballx, 2)) + (math.pow(enemyy - bally, 2)))
            if distance_ball < 50:
                return True
            else:
                return False


def show_score(x, y):
    score = font.render("SCORE:" + str(round(no_ofgoals/25)), True, (0, 0, 0))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (30, 25, 10))
    screen.blit(over_text, (200, 250))
    
    
game_time = True
score_chances = []
count = 0
no_ofgoals = 0
no_of_turns = 0

# game loop
while game_time:

    screen.fill((0, 0, 0))
    screen.blit(back_ground, (0, 0))
    screen.blit(goalpostImg, (370, 0))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            game_time = False

            # designing the movement of player
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                playerX_Change = -1

            if events.key == pygame.K_RIGHT:
                playerX_Change = 1

            if events.key == pygame.K_ESCAPE:
                game_over_text()
                game_time = False


        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                playerX_Change = 0

    # designing the movement of opponent
    for i in range(num_of_enemies):
        for row in range(3):
            if enemyX[i] <= 0:
                enemyX_change[i] = 0.4
                enemyY[i] += row * enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -0.4
                enemyY[i] += row * enemyY_change[i]

            enemyX[i] += enemyX_change[i]
            opponent(enemyX[i], enemyY[i], i)

            collision = iscollision(enemyX[i], enemyY[i], ballX, ballY)
            if collision:
                print("collision")
                count += 1
                ballX = playerX
                ballY = playerY
                print(count)


    # checking boundary of opponent and making them bounce back
    for i in range(num_of_enemies):
        for row in range(3):
            if i == 1:
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = i / 2 * 0.4
                elif enemyX[i] >= 736:
                    enemyX_change[i] = i / 2 * -0.4
            if i == 2:
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = i / 3 * 0.4
                elif enemyX[i] >= 736:
                    enemyX_change[i] = i / 3 * -0.4
            if i == 3:
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 100:
                    enemyX_change[i] = i / 4 * 0.4
                elif enemyX[i] >= 700:
                    enemyX_change[i] = i / 4 * -0.4

        # adding the boundary for player
    playerX += playerX_Change
    if playerX <= 25:
        playerX = 25
    elif playerX >= 715:
        playerX = 715

    m = pygame.mouse.get_pressed()

    if m[0]:
        ball_State = "shoot"
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        radians = math.atan2(mouse_Y - playerY, mouse_X - playerX)
        distance = math.hypot(mouse_X - playerX, mouse_Y - playerY) / 1.5
        distance1 = int(distance)
        dx = math.cos(radians) * 1.5
        dy = math.sin(radians) * 1.5
        ballX = playerX
        ballY = playerY

    if ball_State == "shoot" and distance1 > 0:
        shoot_sound = mixer.Sound('./sounds/ball_shoot.wav')
        shoot_sound.play(0)
        distance1 -= 1
        ballX += dx
        ballY += dy
        ball_movement(ballX, ballY)
        goal_detection(ballX, ballY)

    player(playerX, playerY)
    show_score(textx, texty)
    pygame.display.update()

pygame.quit()
