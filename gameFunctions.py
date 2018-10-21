import pygame
import sys


def import_image_library():
    image_lib = [pygame.image.load('Images/Pac1.png'), pygame.image.load('Images/Pac4.png'),
                 pygame.image.load('Images/Pac5.png'), pygame.image.load('Images/Tile.png'),
                 pygame.image.load('Images/SmallPill.png'), pygame.image.load('Images/BlinkyUp1.png')]
    return image_lib


def check_key_down_events(event, pacman):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        pacman.check_move("left")
    elif event.key == pygame.K_RIGHT:
        pacman.check_move("right")
    elif event.key == pygame.K_DOWN:
        pacman.check_move("down")
    elif event.key == pygame.K_UP:
        pacman.check_move("up")


def check_events(pacman):
    #   Responds to key presses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, pacman)
        else:
            return


def check_time(clock, delta_t, timer, pacman):
    timer -= delta_t
    if timer <= 0:
        pacman.change_image()
        timer = 1
    delta_t = clock.tick(60) / 60
    return delta_t, timer
