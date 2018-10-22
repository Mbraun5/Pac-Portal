import pygame
import os
import settings as s
import maze as m
import gameFunctions as gF
import pac as p
import scoreboard as sb
import ghost as g


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
    blinky = g.Blinky(image_lib, screen, settings, maze.blinkyCoordinates[0], maze.blinkyCoordinates[1])
    clyde = g.Clyde(image_lib, screen, settings, maze.clydeCoordinates[0], maze.clydeCoordinates[1])
    inky = g.Inky(image_lib, screen, settings, maze.inkyCoordinates[0], maze.inkyCoordinates[1])
    pinky = g.Pinky(image_lib, screen, settings, maze.pinkyCoordinates[0], maze.pinkyCoordinates[1])
    ghosts = [blinky, clyde, inky, pinky]

    clock = pygame.time.Clock()
    timer = 1                       # pacTimer
    timer2 = 0.5                    # pillTimer
    timer3 = 1.5                    # ghostTimer
    delta_t = 0                     # Delta to subtract from time
    while True:
        gF.check_events(pacman)
        pacman.update()
        gF.check_collisions(large_pills, pacman, pills, scoreboard)
        delta_t, timer, timer2, timer3 = gF.check_time(clock, delta_t, ghosts, large_pills, timer, timer2, timer3,
                                                       pacman)
        for pill in large_pills:
            pill.blit()
        for ghost in ghosts:
            ghost.blit()
        pacman.blit()
        pygame.display.flip()


run_game()
