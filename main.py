import pygame 

pygame.init()
WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60


#game variable and images


#main game loop

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    
    #event handling 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.flip()


pygame.quit()