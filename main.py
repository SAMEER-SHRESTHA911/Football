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


game_time = True

playerX = 370
playerY = 480


ball_vel = 5
radius = 10
ballX = 350
ballY = 400 

# game loop
while game_time:

    screen.fill((0,0,0))
    screen.blit(back_ground,(0,0))
    pygame.draw.circle(screen,(255,255,255),(ballX,ballY),radius)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            game_time = False

#changing position of shooter 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= 0.3
    if keys[pygame.K_RIGHT]:
        playerX += 0.3


    pygame.display.update()
pygame.quit()