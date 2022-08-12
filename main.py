import pygame


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

def player(x,y):
    screen.blit(playerImg, (x,y))

game_time = True

# game loop
while game_time:

    screen.fill((0, 0, 0))
    screen.blit(back_ground, (0, 0))
    screen.blit(goalpostImg,(370,0))

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

    player(playerX, playerY)
    pygame.display.update()