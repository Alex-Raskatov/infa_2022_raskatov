import pygame
from pygame.draw import *
from random import randint
pygame.init()

balls_counts_1 = int(input("Количество движущихся шаров: "))
balls_counts_2 = int(input("Количество исчезающих шаров: "))
FPS = 30
Points = 0
frame_1 = 0
frame_2 = 0
screen = pygame.display.set_mode((1200, 900))
balls_1 = [[600, 450, randint(-5, 5), randint(-5, 5), 50, (randint(0, 255), randint(0, 255), randint(0, 255))] for i in range(balls_counts_1)]
balls_2 = [[600, 450, randint(-5, 5), randint(-5, 5), 50, (randint(0, 255), randint(0, 255), randint(0, 255))] for i in range(balls_counts_2)]

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball_1(number):
    '''рисует новый шарик, который движется '''
    global balls_1
    balls_1[number][0] += balls_1[number][2]
    balls_1[number][1] += balls_1[number][3]
    balls_1[number][4] += randint(-2, 2)
    if balls_1[number][4] < 10: balls_1[number][4] = 10
    if balls_1[number][4] > 100: balls_1[number][4] = 100
    if (balls_1[number][0] < balls_1[number][4] and balls_1[number][2] < 0) or (balls_1[number][0] > 1200-balls_1[number][4] and balls_1[number][2] > 0):
        balls_1[number][2] = - balls_1[number][2]
        balls_1[number][3] = randint(-6, 6)
    if (balls_1[number][1] > 900-balls_1[number][4] and balls_1[number][3] > 0) or (balls_1[number][1] < balls_1[number][4] and balls_1[number][3] < 0):
        balls_1[number][3] = - balls_1[number][3]
        balls_1[number][2] = randint(-6, 6)
    circle(screen, balls_1[number][5], (balls_1[number][0], balls_1[number][1]), balls_1[number][4])

def new_ball_2(number):
    '''рисует новый шарик, который исчезает '''
    global balls_2, frame_2
    if frame_2 == 30:
        balls_2[number][0] = randint(100, 1100)
        balls_2[number][1] = randint(100, 900)
        balls_2[number][4] = randint(10, 100)
        circle(screen, balls_2[number][5], (balls_2[number][0], balls_2[number][1]), balls_2[number][4])
        frame_2 = 0
    else:
        frame_2 += 1
        circle(screen, balls_2[number][5], (balls_2[number][0], balls_2[number][1]), balls_2[number][4])

def click_1(event, number):
    '''обработа попаданий и промахиваний по мячу'''
    global balls_1
    if (event.pos[0] - balls_1[number][0])**2 + (event.pos[1] - balls_1[number][1])**2 < balls_1[number][4]**2:
        print("Ура!!!")
        points_1(True)

def click_2(event, number):
    '''обработа попаданий и промахиваний по мячу'''
    global balls_2
    if (event.pos[0] - balls_2[number][0])**2 + (event.pos[1] - balls_2[number][1])**2 < balls_2[number][4]**2:
        print("Ура!!!")
        points_1(True)


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
            for i in range(balls_counts_1):
                click_1(event, i)
            for i in range(balls_counts_2):
                click_2(event, i)
    for i in range(balls_counts_1):
        new_ball_1(i)
    for i in range(balls_counts_2):
        new_ball_2(i)
    img = font.render('Points: ' + str(Points), True, (255, 255, 255))
    screen.blit(img, (20, 20))
    pygame.display.update()
    screen.fill(BLACK)
    finish()

pygame.quit()