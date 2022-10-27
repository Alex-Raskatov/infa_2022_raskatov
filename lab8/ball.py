import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
Points = 0
frame_1 = 0
frame_2 = 0
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x_1, x_2, y_1, y_2, r_1, r_2 = 600, 600, 450, 450, 50, 50
v_x_1 = randint(-50, 50)/10
v_y_1 = randint(-50, 50)/10

def new_ball_1():
    '''рисует новый шарик, который движется '''
    global x_1, y_1, r_1, v_x_1, v_y_1
    x_1 += v_x_1
    y_1 += v_y_1
    r_1 += randint(-2, 2)
    if x_1 < 0+r_1 or x_1 > 1200-r_1:
        v_x_1 = - v_x_1 + randint(-2, 2)
        v_y_1 += randint(-2, 2)
    if y_1 > 900-r_1 or y_1 < 0+r_1:
        v_y_1 = - v_y_1 + randint(-2, 2)
        v_x_1 += randint(-2, 2)
    color = COLORS[randint(0, 5)]
    circle(screen, (200,50, 170), (x_1, y_1), r_1)

def new_ball_2():
    '''рисует новый шарик, который исчезает '''
    global x_2, y_2, r_2, frame_2
    color = COLORS[randint(0, 5)]
    if frame_2 == 60:
        x_2 = randint(100, 1100)
        y_2 = randint(100, 900)
        r_2 = randint(10, 100)
        circle(screen, (200, 50, 170), (x_2, y_2), r_2)
        frame_2 = 0
    else:
        frame_2 += 1
        circle(screen, (200, 170, 50), (x_2, y_2), r_2)

def click(event):
    '''обработа попаданий и промахиваний по мячу'''
    global  frame_2
    if (event.pos[0]-x_1)**2 + (event.pos[1]-y_1)**2 < r_1**2:
        print("Ура!!!")
        points_1(True)
    if (event.pos[0]-x_2)**2 + (event.pos[1]-y_2)**2 < r_2**2:
        print("Ура!!!")
        points_2(True)
        frame_2 = 60
    if (event.pos[0]-x_1)**2 + (event.pos[1]-y_1)**2 > r_1**2 and (event.pos[0]-x_2)**2 + (event.pos[1]-y_2)**2 > r_2**2:
        print("Не ура")
        points_1(False)

def points_1(flag):
    '''счетчик очков за движущийся шарик'''
    global Points
    if flag == True:
        Points += 1
        print("Points: ", Points)
    else:
        Points -= 1
        print("Не ура")

def points_2(flag):
    '''счетчик очков за исчезающий шарик'''
    global Points
    if flag == True:
        Points += 2
        print("Points: ", Points)
    else:
        Points -= 1
        print("Не ура")

def finish():
    global finished, Points
    if Points < 0:
        finished = True


font = pygame.font.SysFont(None, 24)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    new_ball_2()
    new_ball_1()
    img = font.render('Points: ' + str(Points), True, (255, 255, 255))
    screen.blit(img, (20, 20))
    pygame.display.update()
    screen.fill(BLACK)
    finish()

pygame.quit()