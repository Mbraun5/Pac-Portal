import pygame
import sys
import traceback


class Maze:
    def __init__(self, screen, settings):
        self.__screen = screen
        self.__screenRect = screen.get_rect()
        self.__settings = settings

        self.__rect = pygame.Rect(0, 0, self.__settings.get_square_rect(), self.__settings.get_square_rect())
        self.__rectColor = settings.get_square_rect_color()
        self.__rect.x = 215
        self.__rect.top = 60

        self.draw_map()

        print("last")

    def draw_maze(self, f):
        copy = self.__rect.copy()
        while True:
            flag = f.read(1)
            if flag == "":
                break
            if flag == "\n":
                copy.top = copy.bottom
                copy.left = self.__rect.left
            elif flag == ".":
                copy.left = copy.right
            elif flag == "x":
                pygame.draw.rect(self.__screen, self.__rectColor, copy)
                copy.left = copy.right
        pygame.display.flip()

    def draw_map(self):
        try:
            with open('maze.txt', 'r') as f:
                self.draw_maze(f)
        except FileNotFoundError:
            print("The file '{}' was not found.".format('maze.txt'))
            sys.exit(1)
        except Exception as ex:
            print("File error: '{}' when opening the file: '{}'".format(ex, 'maze.txt'))
            traceback.print_exc()
            sys.exit(1)

