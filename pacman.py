import pygame
import os
import settings as s
import maze as m
import math
import time


def run_game():
    #   Provides consistent window positioning. These settings center Pygame window for my computer.
    os.environ['SDL_VIDEO_WINDOW_POS'] = '60, 35'
    pygame.init()

    settings = s.Settings()
    screen = pygame.display.set_mode((settings.get_screen_width(), settings.get_screen_height()))
    pygame.display.set_caption(settings.get_game_title())

    screen.fill(settings.get_bg_color())
    maze = m.Maze(screen, settings)

    '''
    image = pygame.image.load('Images/Pac0.png')
    image = pygame.transform.scale(image, (30, 30))
    image = pygame.transform.rotate(image, 270)
    rect = image.get_rect()
    rect.centerx = 300
    rect.centery = 300
    screen.blit(image, rect)
    pygame.display.flip()
    '''
    image_lib = [pygame.image.load('Images/Pac0.png'), pygame.image.load('Images/Pac1.png'), pygame.image.load('Images/Pac3.png')]

    '''
    for index, image in enumerate(image_lib):
        new_img = pygame.transform.rotate(image, 180)
        image_lib[index] = new_img
    '''

    rect = image_lib[0].get_rect()
    rect.centerx = 670
    rect.centery = 629
    screen.blit(image_lib[0], rect)
    pygame.display.flip()

    count = 1
    item = 0
    counter = 1
    while True:
        '''
        screen.fill((0, 0, 0))
        rect.x -= 1
        screen.blit(image_lib[item], rect)
        pygame.display.flip()
        if count > 28 or count < 1:
            counter *= -1
        count += counter
        item = math.floor(count / 10)
        '''
        pass


run_game()
