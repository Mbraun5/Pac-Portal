import pygame
import os
import settings as s
import maze as m
import gameFunctions as gF
import pac as p
import scoreboard as sb
import ghost as g
import titleScreen as tS
import time


def run_game():
    #   Provides consistent window positioning. These settings center Pygame window for my computer.
    os.environ['SDL_VIDEO_WINDOW_POS'] = '60, 35'
    pygame.init()

    #   Initial Set-up
    settings = s.Settings()
    pygame.display.set_caption(settings.get_game_title())
    screen = pygame.display.set_mode((settings.get_screen_width(), settings.get_screen_height()))
    screen.fill(settings.get_bg_color())
    clock = pygame.time.Clock()

    # Generate Game Objects
    image_lib = gF.import_image_library()
    sound_lib = gF.import_sound_library()
    maze = m.Maze(image_lib, screen, settings)
    pacman = p.PacMan(maze.pacmanCoordinates, image_lib, screen, settings, sound_lib)
    pills = maze.pills.copy()
    large_pills = maze.largePills.copy()
    blinky = g.Blinky(image_lib, screen, settings, maze.blinkyCoordinates[0], maze.blinkyCoordinates[1])
    clyde = g.Clyde(image_lib, screen, settings, maze.clydeCoordinates[0], maze.clydeCoordinates[1])
    inky = g.Inky(image_lib, screen, settings, maze.inkyCoordinates[0], maze.inkyCoordinates[1])
    pinky = g.Pinky(image_lib, screen, settings, maze.pinkyCoordinates[0], maze.pinkyCoordinates[1])
    ghosts = [blinky, clyde, inky, pinky]
    title_sequence = tS.TitleScreen(clock, pacman.images.copy(), image_lib, screen, settings)
    title_sequence.refresh_screen()
    pacman.set_map(maze.get_map(), maze.rowIndex, maze.columnIndex)
    maze.draw_part_maze()
    scoreboard = sb.ScoreBoard(maze, screen, settings)

    timer = 1                       # pacTimer
    timer2 = 0.5                    # pillTimer
    timer3 = 1.5                    # ghostTimer
    delta_t = 0                     # Delta to subtract from time
    reset_flag = False
    print(reset_flag)
    gF.start_game(ghosts, large_pills, pacman, pills, sound_lib[0])
    pygame.mixer.Sound.play(sound_lib[1], -1)

    while True:
        gF.check_events(pacman)
        pacman.update()
        reset_flag = gF.check_collisions(ghosts, large_pills, maze, pacman, pills, scoreboard, sound_lib[3])
        delta_t, timer, timer2, timer3 = gF.check_time(clock, delta_t, ghosts, large_pills, timer, timer2, timer3,
                                                       pacman)
        for pill in large_pills:
            pill.blit()
        for ghost in ghosts:
            ghost.blit()
        pacman.blit()
        pygame.display.flip()
        if reset_flag:
            screen.fill(settings.get_bg_color())
            pills = maze.pills.copy()
            large_pills = maze.largePills.copy()
            maze.draw_part_maze()
            gF.start_game(ghosts, large_pills, pacman, pills, sound_lib[0])
            timer = 1
            timer2 = 0.5
            timer3 = 1.5
            delta_t = 0
            reset_flag = False
            print(reset_flag)


run_game()

'''
def hello(rect):
    return rect.x
myDict = {}
myDict['hey'] = hello(pacman.rect)
print(myDict)
print(pacman.rect.x)
myDict['hey'] = hello(pacman.rect)
'''