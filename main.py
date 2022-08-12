import pygame
pygame.init()

win = pygame.display.set_mode((800,800))

pygame.display.set_caption("FOOSBALL")

x=50
y=50
width=40
height=40
vel=5
radius=10

run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    keys = pygame.key.get_pressed()
   
    color = (0,0,255)
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    win.fill((0,0,0))
    pygame.draw.circle(win, color, (x,y),radius)
    pygame.display.update()
pygame.quit()
