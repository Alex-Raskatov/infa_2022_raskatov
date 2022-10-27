import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# rect(screen, (255, 0, 255), (100, 100, 200, 200))
# rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
# polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                                (300,100), (100,100)])
# polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                                (300,100), (100,100)], 5)
# circle(screen, (0, 255, 0), (200, 175), 50)
# circle(screen, (255, 255, 255), (200, 175), 50, 5)


screen.fill((200, 200, 200))
circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (255, 0, 0), (150, 150), 30)
circle(screen, (255, 0, 0), (250, 150), 20)
circle(screen, (0, 0, 0), (150, 150), 20)
circle(screen, (0, 0, 0), (250, 150), 10)
rect(screen, (0, 0, 0), (150, 200, 100, 20))
# polygon(screen, (0, 0, 0), [(100, 100), (200, 50), (300, 100), (100, 100)])
# polygon(screen, (0, 0, 0), [(150, 150), (150 + 50, 150 + 50),(150 + 50 - 5, 150 + 50 + 5),(150 + 45 - 50, 150 + 55 - 50), (150, 150)])
line(screen , (0,0,0) , [100, 100], [200, 130], 10)
line(screen , (0,0,0) , [220, 130], [280, 110], 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()