import pygame
import time


class PacMan:
    def __init__(self, image_library, screen, settings):
        self.screen = screen
        self.settings = settings
        self.images = []
        for index in self.settings.pacIndexes:
            self.images.append(image_library[index])
        self.map = None
        self.row_index = None
        self.column_index = None

        self.blitCounter = 0
        self.blitIndex = 1
        self.indexInc = 1
        self.rect = self.images[0].get_rect()

        self.speed = self.settings.pacSpeed
        self.direction = "right"
        self.moving = True
        #   Tracks whether or not Pacman needs to change direction and at what x or y coordinate it needs to change.
        self.updateFlag = [False, "Direction", 0, 0]
        self.mapCounter = 0

        self.travelDistance = 60

    def blit(self):
        self.screen.blit(self.images[self.blitIndex], self.rect)

    def set_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def change_image(self):
        if self.moving:
            if self.blitIndex == 2 or self.blitIndex == 0:
                self.indexInc *= -1
            self.blitIndex += self.indexInc

    def set_map(self, new_map, row_index, column_index):
        self.map = new_map
        self.row_index = row_index
        self.column_index = column_index
        self.go_left()

    def update(self):
        if self.moving:
            self.mapCounter += 1
            if self.direction == "right" or self.direction == "left":
                self.rect.x += self.speed
                if self.mapCounter == 5:
                    self.map[self.row_index][self.column_index] = '.'
                    self.column_index += int(self.speed/abs(self.speed))
                    self.map[self.row_index][self.column_index] = 'P'
                    self.mapCounter = 0
                self.travelDistance -= abs(self.speed)
            else:
                self.rect.y += self.speed
                if self.mapCounter == 5:
                    self.map[self.row_index][self.column_index] = '.'
                    self.row_index += int(self.speed/abs(self.speed))
                    self.map[self.row_index][self.column_index] = 'P'
                    self.mapCounter = 0
                self.travelDistance -= abs(self.speed)
        if self.travelDistance <= 0:
            self.moving = False
        self.print_map()



    ''' LEFT OFF HERE'''
    def check_move(self, direction):
        if direction == "left":
            if isinstance(self.map[self.row_index][self.column_index - 1], pygame.Rect) or \
                    isinstance(self.map[self.row_index + 1][self.column_index - 1], pygame.Rect) or \
                    isinstance(self.map[self.row_index + 2][self.column_index - 1], pygame.Rect):
                if self.direction == "up":
                    count = 2
                    while isinstance(self.map[self.row_index + count][self.column_index - 1], pygame.Rect):
                        count += 1
                    self.updateFlag = [True, "left", ]
        elif direction == "right":
            pass
        elif direction == "up":
            pass
        elif direction == "down":
            pass

    def go_left(self):
        self.moving = True
        if self.direction == "right":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.flip(image, True, False)
            self.speed *= -1
        elif self.direction == "up":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.rotate(image, 90)
        elif self.direction == "down":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.rotate(image, 270)
            self.speed *= -1
        self.direction = "left"

        count = 0
        while not isinstance(self.map[self.row_index][self.column_index - count], pygame.Rect):
            count += 1
        self.travelDistance = self.rect.left - self.map[self.row_index][self.column_index - count].right

    def go_right(self):
        self.moving = True
        if self.direction == "left":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.flip(image, True, False)
            self.speed *= -1
        elif self.direction == "up":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.rotate(image, 270)
            self.speed *= -1
        elif self.direction == "down":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.rotate(image, 90)
        self.direction = "right"

        count = 0
        while not isinstance(self.map[self.row_index][self.column_index + count], pygame.Rect):
            count += 1
        self.travelDistance = self.map[self.row_index][self.column_index + count].left - self.rect.right

    def go_up(self):
        self.moving = True
        if self.direction == "down":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.flip(image, False, True)
            self.speed *= -1
        elif self.direction == "left":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.rotate(image, 270)
        elif self.direction == "right":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.rotate(image, 90)
            self.speed *= -1
        self.direction = "up"

        count = 0
        while not isinstance(self.map[self.row_index - count][self.column_index], pygame.Rect):
            count += 1
        self.travelDistance = self.rect.top - self.map[self.row_index - count][self.column_index].bottom

    def go_down(self):
        self.moving = True
        if self.direction == "up":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.flip(image, False, True)
            self.speed *= -1
        elif self.direction == "left":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.rotate(image, 90)
            self.speed *= -1
        elif self.direction == "right":
            for index, image in enumerate(self.images):
                self.images[index] = pygame.transform.rotate(image, 270)
        self.direction = "down"

        count = 0
        while not isinstance(self.map[self.row_index + count][self.column_index], pygame.Rect):
            count += 1
        self.travelDistance = self.map[self.row_index + count][self.column_index].top - self.rect.bottom

    def print_map(self):
        for obj in self.map:
            for item in obj:
                if isinstance(item, pygame.Rect):
                    print('x', end="")
                elif isinstance(item, str):
                    print(item, end="")
            print()
