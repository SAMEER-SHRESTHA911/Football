import pygame


# starting the game
pygame.init()

# creating the window
screen = pygame.display.set_mode((800,605))

# changing the title and logo
pygame.display.set_caption("Free Kick")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# changing the background
back_ground = pygame.image.load('ground_800x605.jpg')

# creating the player
playerImg = pygame.image.load('ball.png')
playerX = 370
playerY = 480
playerX_Change = 0
def player(x,y):
    screen.blit(playerImg, (x,y))

game_time = True


# game loop
while game_time:

    screen.fill((0, 0, 0))
    screen.blit(back_ground, (0, 0))


ball_vel = 5
ballX = 350
ballY = 400 

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
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    player(playerX, playerY)
    pygame.display.update()

pygame.quit()

