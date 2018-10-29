import pygame
import sys
import traceback
import powerpill


class Maze:
    def __init__(self, image_lib, screen, settings):
        self.__screen = screen
        self.__screenRect = screen.get_rect()
        self.__settings = settings

        self.__rect = pygame.Rect(0, 0, self.__settings.get_square_rect(), self.__settings.get_square_rect())
        self.__rectColor = settings.get_square_rect_color()
        self.__rect.x = 200
        self.__rect.top = 110

        self.image_lib = image_lib
        self.map = []
        self.rowIndex = None
        self.columnIndex = None

        self.blinkyCoordinates = None
        self.clydeCoordinates = None
        self.inkyCoordinates = None
        self.pinkyCoordinates = None
        self.pacmanCoordinates = None

        self.pills = []
        self.largePills = []
        self.parse_file()

        self.print_map()

    def parse_file(self):
        try:
            with open('maze.txt', 'r') as f:
                map_row = []
                copy = self.__rect.copy()
                while True:
                    flag = f.read(1)
                    if flag == "":
                        self.map.append(map_row)
                        break
                    elif flag == "\n":
                        copy.top = copy.bottom
                        copy.left = self.__rect.left
                        self.map.append(map_row)
                        map_row = []
                    elif flag == ".":
                        copy.left = copy.right
                        map_row.append(flag)
                    elif flag == 'o':
                        x = copy.centerx
                        y = copy.centery
                        new_pill = powerpill.SmallPowerPill(self.image_lib, self.__screen, self.__settings, x, y)
                        self.pills.append(new_pill)
                        map_row.append(flag)
                        copy.left = copy.right
                    elif flag == 'O':
                        x = copy.centerx+5
                        y = copy.centery+5
                        new_pill = powerpill.LargePowerPill(self.image_lib, self.__screen, self.__settings, x, y)
                        self.largePills.append(new_pill)
                        map_row.append(flag)
                        copy.left = copy.right
                    elif flag == "b":
                        self.blinkyCoordinates = [copy.x, copy.y]
                        map_row.append(flag)
                        copy.left = copy.right
                    elif flag == "i":
                        self.inkyCoordinates = [copy.x, copy.y]
                        map_row.append(flag)
                        copy.left = copy.right
                    elif flag == "p":
                        self.pinkyCoordinates = [copy.x, copy.y]
                        map_row.append(flag)
                        copy.left = copy.right
                    elif flag == "c":
                        self.clydeCoordinates = [copy.x, copy.y]
                        map_row.append(flag)
                        copy.left = copy.right
                    elif flag == "P":
                        self.pacmanCoordinates = [copy.x, copy.y]
                        self.rowIndex = len(self.map)
                        self.columnIndex = len(map_row)
                        map_row.append(flag)
                        copy.left = copy.right
                    elif flag == "x":
                        map_row.append(copy.copy())
                        copy.left = copy.right
        except FileNotFoundError:
            print("The file '{}' was not found.".format('maze.txt'))
            sys.exit(1)
        except Exception as ex:
            print("File error: '{}' when opening the file: '{}'".format(ex, 'maze.txt'))
            traceback.print_exc()
            sys.exit(1)

    def draw_maze(self):
        for obj in self.map:
            for item in obj:
                if isinstance(item, pygame.Rect):
                    self.__screen.blit(self.image_lib[3], item)
        for pill in self.pills:
            pill.blit()
        pygame.display.flip()

    def draw_part_maze(self):
        for obj in self.map:
            for item in obj:
                if isinstance(item, pygame.Rect):
                    self.__screen.blit(self.image_lib[3], item)

    def get_map(self):
        return self.map

    def print_map(self):
        for obj in self.map:
            for item in obj:
                if isinstance(item, pygame.Rect):
                    print('x', end="")
                elif isinstance(item, str):
                    print(item, end="")
            print()
        print(self.rowIndex, self.columnIndex)
