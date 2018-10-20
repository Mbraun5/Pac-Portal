import pygame
import os
import settings as s
import maze as m
import gameFunctions as gF
import pac as p


def run_game():
    #   Provides consistent window positioning. These settings center Pygame window for my computer.
    os.environ['SDL_VIDEO_WINDOW_POS'] = '60, 35'
    pygame.init()

    #   Initial Set-up
    settings = s.Settings()
    screen = pygame.display.set_mode((settings.get_screen_width(), settings.get_screen_height()))
    pygame.display.set_caption(settings.get_game_title())
    screen.fill(settings.get_bg_color())

    image_lib = gF.import_image_library()
    pacman = p.PacMan(image_lib, screen, settings)
    maze = m.Maze(image_lib, screen, settings, pacman)
    pacman.set_map(maze.get_map(), maze.rowIndex, maze.columnIndex)


    rect = image_lib[5].get_rect()
    rect.x = 500
    rect.y = 500


    clock = pygame.time.Clock()
    timer = 1                       # Marks 1 second
    delta_t = 0                     # Delta to subtract from time
    while True:
        screen.blit(image_lib[5], rect)
        gF.check_events(pacman)
        pacman.update()
        delta_t, timer = gF.check_time(clock, delta_t, timer, pacman)
        pacman.blit()
        pygame.display.flip()

run_game()
