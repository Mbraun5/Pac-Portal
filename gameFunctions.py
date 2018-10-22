import pygame
import sys


def import_image_library():
    image_lib = [pygame.image.load('Images/Pac1.png'), pygame.image.load('Images/Pac4.png'),
                 pygame.image.load('Images/Pac5.png'), pygame.image.load('Images/Tile.png'),
                 pygame.image.load('Images/SmallPill.png'), pygame.image.load('Images/LargePill1.png'),
                 pygame.image.load('Images/LargePill2.png'), pygame.image.load('Images/LargePill3.png'),
                 pygame.image.load('Images/LargePill4.png'), pygame.image.load('Images/LargePill5.png'),
                 pygame.image.load('Images/LargePill6.png'), pygame.image.load('Images/LargePill7.png'),
                 pygame.image.load('Images/LargePill8.png'), pygame.image.load('Images/LargePill9.png'),
                 pygame.image.load('Images/LargePill10.png'), pygame.image.load('Images/LargePill11.png')]
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


def check_time(clock, delta_t, large_pills, timer, timer2, pacman):
    timer -= delta_t
    timer2 -= delta_t
    if timer <= 0:
        pacman.change_image()
        timer = 1
    if timer2 <= 0:
        for pill in large_pills:
            pill.change_image()
        timer2 = 0.5
    delta_t = clock.tick(60) / 60
    return delta_t, timer, timer2


def check_collisions(large_pills, pacman, pills, scoreboard):
    for index, pill in enumerate(pills):
        if pacman.rect.colliderect(pill.rect):
            scoreboard.update_score(pill.value)
            del pills[index]
    for index, pill in enumerate(large_pills):
        if pacman.rect.colliderect(pill.rect):
            scoreboard.update_score(pill.value)
            del large_pills[index]
