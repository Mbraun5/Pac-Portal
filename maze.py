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

        self.image_lib = [pygame.image.load('Images/Pacmang.png'), pygame.image.load('Images/Pac1.png'), pygame.image.load('Images/Pac3.png'), pygame.image.load('Images/Tile.png')]
        self.map = []
        self.parse_file()
        self.draw_maze()

        self.rowIndex = 0
        self.columnIndex = 0

    def parse_file(self):
        try:
            with open('pellet.txt', 'r') as f:
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
                    elif flag == "." or flag == 'o':
                        copy.left = copy.right
                        map_row.append(flag)
                    elif flag == "P":
                        self.newRect = self.image_lib[0].get_rect()
                        self.newRect.left = copy.right
                        self.newRect.y = copy.y
                        self.rowIndex = len(self.map)
                        self.columnIndex = len(map_row)
                        map_row.append(self.newRect)
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
                    #pygame.draw.rect(self.__screen, self.__rectColor, item)
        self.__screen.blit(self.image_lib[0], self.newRect)
        pygame.display.flip()
