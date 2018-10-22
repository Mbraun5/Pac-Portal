import pygame
import os
import settings as s
import maze as m
import gameFunctions as gF
import pac as p
import scoreboard as sb


def run_game():
    #   Provides consistent window positioning. These settings center Pygame window for my computer.
    os.environ['SDL_VIDEO_WINDOW_POS'] = '60, 35'
    pygame.init()

    #   Initial Set-up
    settings = s.Settings()
    pygame.display.set_caption(settings.get_game_title())
    screen = pygame.display.set_mode((settings.get_screen_width(), settings.get_screen_height()))
    screen.fill(settings.get_bg_color())

    # Generate Game Objects
    image_lib = gF.import_image_library()
    pacman = p.PacMan(image_lib, screen, settings)
    maze = m.Maze(image_lib, screen, settings, pacman)
    pills = maze.pills.copy()
    large_pills = maze.largePills.copy()
    scoreboard = sb.ScoreBoard(maze, screen, settings)
    pacman.set_map(maze.get_map(), maze.rowIndex, maze.columnIndex)

    clock = pygame.time.Clock()
    timer = 1                       # Marks 1 second
    timer2 = 0.5                      # Marks 3 seconds
    delta_t = 0                     # Delta to subtract from time
    while True:
        gF.check_events(pacman)
        pacman.update()
        gF.check_collisions(large_pills, pacman, pills, scoreboard)
        delta_t, timer, timer2 = gF.check_time(clock, delta_t, large_pills, timer, timer2, pacman)
        for pill in large_pills:
            pill.blit()
        pacman.blit()
        pygame.display.flip()


run_game()
