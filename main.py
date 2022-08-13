import pygame
import math
import time

# starting the game
pygame.init()

# creating the window
screen = pygame.display.set_mode((800,545))


# changing the title and logo
pygame.display.set_caption("Free Kick")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# changing the background
back_ground = pygame.image.load('new_800x545.jpg')

# creating the player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_Change = 0

# creating the goalpost
goalpostImg = pygame.image.load('post.png')

# loading the ball
ballImg = pygame.image.load('ball.png')
ball_State = "ready"

def player(x,y):
    screen.blit(playerImg, (x, y))

def ball_movement(a, b):
    screen.blit(ballImg, (a, b))

game_time = True

# game loop
while game_time:

    screen.fill((0, 0, 0))
    screen.blit(back_ground, (0, 0))
    screen.blit(goalpostImg,(370,0))


    # ball_vel = 5
    # ballX = 350
    # ballY = 400

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            game_time = False


            # designing the movement of player
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                    playerX_Change = -0.3

            if events.key == pygame.K_RIGHT:
                    playerX_Change = 0.3

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                playerX_Change = 0

        # adding the boundary for player
    playerX += playerX_Change
    if playerX <= 25:
        playerX = 25
    elif playerX >= 715:
        playerX = 715

    m = pygame.mouse.get_pressed()

    if m[0]:
        # is_mouse_clicked(playerX, playerY)
        print("mouse pressed")
        ball_State = "shoot"
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        radians = math.atan2(mouse_Y - playerY, mouse_X - playerX)
        distance = math.hypot(mouse_X - playerX, mouse_Y - playerY)/0.9
        distance1 = int(distance)
        dx = math.cos(radians)*0.9
        dy = math.sin(radians)*0.9
        ballX = playerX
        ballY = playerY

    if ball_State == "shoot" and distance1 > 0:
            distance1 -= 1
            ballX += dx
            ballY += dy
            ball_movement(ballX, ballY)
    else:
        ball_State = "ready"


    player(playerX, playerY)
    pygame.display.update()

pygame.quit()

