import pygame
import random
from pygame.locals import *

pygame.init()
# TODO  zrobić snake'a z gierki
screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen): # rect in the third argument requiers 4 things
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 25, 25))

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen): # rect in the third argument requiers 4 things
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 25, 25))

player = Player(100, 400)
point = Point(random.randint(0, 500), random.randint(0, 500))
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.y -= 5
        print(player.y)
    if keys[pygame.K_DOWN]:
        player.y += 5
        print(player.y)
    if keys[pygame.K_LEFT]:
        player.x -= 5
        print(player.x)
    if keys[pygame.K_RIGHT]:
        player.x += 5
        print(player.x)
# crossing screen border on the left and right
#     right
    if player.x >= 500:
        player.x = 0
    #     left
    if player.x <= -10:
        player.x = 450
# crossing screen border on the top and bottom
#     bottom
    if player.y >= 500:
        player.y = 0
    # top
    if player.y <= -10:
        player.y = 500

    screen.fill((255, 255, 255))

    player.draw(screen)
    point.draw(screen)

    pygame.display.update()

pygame.quit()