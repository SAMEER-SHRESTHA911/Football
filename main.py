import pygame


# starting the game
pygame.init()

# creating the window
screen = pygame.display.set_mode((800,600))

# changing the title and logo
pygame.display.set_caption("Free Kick")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# changing the background
back_ground = pygame.image.load('ground_800x605.jpg')


game_time = True


# game loop
while game_time:

    screen.fill((0,0,0))
    screen.blit(back_ground,(0,0))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            game_time = False




    pygame.display.update()