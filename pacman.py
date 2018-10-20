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
    image_lib = [pygame.image.load('Images/Pacman.png'), pygame.image.load('Images/Pac1.png'), pygame.image.load('Images/Pac3.png')]

    while True:
        pass


run_game()
