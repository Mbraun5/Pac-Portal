import pygame
import time


class PacMan:
    def __init__(self, coordinates, image_library, screen, settings, sound_lib):
        self.screen = screen
        self.settings = settings
        self.images = []
        try:
            self.death_sound = sound_lib[2]
        except TypeError:
            pass
        self.deathImages = image_library[self.settings.deathIndices[0]: self.settings.deathIndices[1]]
        for index in self.settings.pacIndexes:
            self.images.append(image_library[index])
        self.map = None
        self.mapOrig = None
        self.row_index = None
        self.column_index = None
        self.row_index_orig = None
        self.column_index_orig = None

        self.blueImage = image_library[58]
        self.orangeImage = image_library[59]
        self.blueActive = False
        self.orangeActive = False
        self.createBlue = False
        self.createOrange = False
        self.blueRect = self.blueImage.get_rect()
        self.orangeRect = self.orangeImage.get_rect()
        self.blue_portal_row_index = None
        self.blue_portal_column_index = None
        self.orange_portal_row_index = None
        self.orange_portal_column_index = None

        self.blitCounter = 0
        self.blitIndex = 1
        self.indexInc = 1
        self.rect = self.images[0].get_rect()
        self.coordinates = coordinates
        self.set_rect(self.coordinates[0], self.coordinates[1])

        self.speed = self.settings.pacSpeed
        self.direction = "right"
        self.moving = True
        #   Tracks whether or not Pacman needs to change direction and at what x or y coordinate it needs to change.
        self.updateFlag = [False, "Direction", 999]
        self.mapCounter = 0

        self.travelDistance = 60

    def set_blue_portal(self):
        if not self.blueActive or self.createBlue:
            self.createBlue = True

    def set_orange_portal(self):
        if not self.orangeActive or self.createOrange:
            self.createOrange = True

    def create_blue_portal(self):
        if not self.blueActive:
            self.blueRect.x = self.rect.x
            self.blueRect.y = self.rect.y
            self.blue_portal_row_index = self.row_index
            self.blue_portal_column_index = self.column_index
            self.blueActive = True

    def create_orange_portal(self):
        if not self.orangeActive:
            self.orangeRect.x = self.rect.x
            self.orangeRect.y = self.rect.y
            self.orange_portal_row_index = self.row_index
            self.orange_portal_column_index = self.column_index
            self.orangeActive = True

    def check_portal_collisions(self):
        if self.createBlue and self.createOrange:
            self.createBlue = False
            self.createOrange = False
        if not self.blueActive or not self.orangeActive:
            return
        if self.blueActive and self.orangeActive:
            if pygame.Rect.contains(self.rect, self.blueRect):
                self.rect.x = self.orangeRect.x
                self.rect.y = self.orangeRect.y
                self.map[self.row_index][self.column_index] = '.'
                self.map[self.orange_portal_row_index][self.orange_portal_column_index] = 'P'
                self.column_index = self.orange_portal_column_index
                self.row_index = self.orange_portal_row_index
                self.continue_direction()
                self.blueActive = False
                self.orangeActive = False
                pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.blueRect)
                pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.orangeRect)
            elif pygame.Rect.contains(self.rect, self.orangeRect):
                self.rect.x = self.blueRect.x
                self.rect.y = self.blueRect.y
                self.map[self.row_index][self.column_index] = '.'
                self.map[self.blue_portal_row_index][self.blue_portal_column_index] = 'P'
                self.column_index = self.blue_portal_column_index
                self.row_index = self.blue_portal_row_index
                self.continue_direction()
                self.blueActive = False
                self.orangeActive = False
                pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.blueRect)
                pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.orangeRect)

    def continue_direction(self):
        self.print_map()
        self.check_move(self.direction)

    def blit(self):
        if self.blueActive:
            self.screen.blit(self.blueImage, self.blueRect)
        if self.orangeActive:
            self.screen.blit(self.orangeImage, self.orangeRect)
        self.screen.blit(self.images[self.blitIndex], self.rect)

    def set_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        self.rect.x = self.coordinates[0]
        self.rect.y = self.coordinates[1]
        self.indexInc = 1
        self.blitIndex = 1
        self.blitCounter = 0
        self.map = self.mapOrig
        self.row_index = self.row_index_orig
        self.column_index = self.column_index_orig
        self.go_left()

    def die(self):
        pygame.mixer.stop()
        pygame.mixer.Sound.play(self.death_sound)
        time.sleep(0.5)
        self.screen.blit(self.deathImages[0], self.rect)
        pygame.display.flip()
        counter = 1
        for i in range(1, 3000000):
            if i % 500000 == 0:
                self.screen.blit(self.deathImages[counter], self.rect)
                pygame.display.flip()
                counter += 1
        pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.rect)
        pygame.display.flip()
        self.reset()
        time.sleep(1)
        pygame.display.flip()

    def change_image(self):
        if self.moving:
            if self.blitIndex == 2 or self.blitIndex == 0:
                self.indexInc *= -1
            self.blitIndex += self.indexInc

    def set_map(self, new_map, row_index, column_index):
        self.map = new_map
        self.mapOrig = new_map.copy()
        self.row_index = row_index
        self.column_index = column_index
        self.row_index_orig = self.row_index
        self.column_index_orig = self.column_index
        self.go_left()

    def update(self):
        if self.moving:
            self.mapCounter += 1
            if self.direction == "right" or self.direction == "left":
                self.rect.x += self.speed
                if self.mapCounter == 5:
                    if self.createBlue:
                        self.create_blue_portal()
                    if self.createOrange:
                        self.create_orange_portal()
                    self.map[self.row_index][self.column_index] = '.'
                    self.column_index += int(self.speed/abs(self.speed))
                    self.map[self.row_index][self.column_index] = 'P'
                    self.mapCounter = 0
                self.travelDistance -= abs(self.speed)
            else:
                self.rect.y += self.speed
                if self.mapCounter == 5:
                    if self.createBlue:
                        self.create_blue_portal()
                    if self.createOrange:
                        self.create_orange_portal()
                    self.map[self.row_index][self.column_index] = '.'
                    self.row_index += int(self.speed/abs(self.speed))
                    self.map[self.row_index][self.column_index] = 'P'
                    self.mapCounter = 0
                self.travelDistance -= abs(self.speed)
            if self.updateFlag[0]:
                self.updateFlag[2] -= abs(self.speed)
        if self.travelDistance <= 0:
            self.moving = False
        if self.updateFlag[0]:
            if self.updateFlag[2] <= 0:
                if self.updateFlag[1] == "left":
                    self.go_left()
                elif self.updateFlag[1] == "right":
                    self.go_right()
                elif self.updateFlag[1] == "up":
                    self.go_up()
                elif self.updateFlag[1] == "down":
                    self.go_down()
                self.updateFlag[0] = False
        self.check_portal_collisions()
        # self.print_map()

    def check_move(self, direction):
        while self.mapCounter != 0:
            self.update()
            self.blit()
            pygame.display.flip()
        if direction == "left":
            if isinstance(self.map[self.row_index][self.column_index - 1], pygame.Rect) or \
                    isinstance(self.map[self.row_index + 1][self.column_index - 1], pygame.Rect) or \
                    isinstance(self.map[self.row_index + 2][self.column_index - 1], pygame.Rect):
                if self.direction == "up":
                    count = 2
                    try:
                        while isinstance(self.map[self.row_index + count][self.column_index - 1], str):
                            count -= 1
                        while isinstance(self.map[self.row_index + count][self.column_index - 1], pygame.Rect):
                            count -= 1
                    except IndexError:
                        return
                    distance = abs(self.rect.bottom - self.map[self.row_index + count + 1][self.column_index - 1].top)
                    self.updateFlag = [True, "left", distance]
                elif self.direction == "down":
                    count = 0
                    try:
                        while isinstance(self.map[self.row_index + count][self.column_index - 1], str):
                            count += 1
                        while isinstance(self.map[self.row_index + count][self.column_index - 1], pygame.Rect):
                            count += 1
                    except IndexError:
                        return
                    distance = abs(self.map[self.row_index + count - 1][self.column_index - 1].bottom - self.rect.top)
                    self.updateFlag = [True, "left", distance]
            else:
                self.go_left()
        elif direction == "right":
            if isinstance(self.map[self.row_index][self.column_index + 3], pygame.Rect) or \
                    isinstance(self.map[self.row_index + 1][self.column_index + 3], pygame.Rect) or \
                    isinstance(self.map[self.row_index + 2][self.column_index + 3], pygame.Rect):
                if self.direction == "up":
                    count = 2
                    try:
                        while isinstance(self.map[self.row_index + count][self.column_index + 3], str):
                            count -= 1
                        while isinstance(self.map[self.row_index + count][self.column_index + 3], pygame.Rect):
                            count -= 1
                    except IndexError:
                        return
                    distance = abs(self.rect.bottom - self.map[self.row_index + count + 1][self.column_index + 3].top)
                    self.updateFlag = [True, "right", distance]
                elif self.direction == "down":
                    count = 0
                    try:
                        while isinstance(self.map[self.row_index + count][self.column_index + 3], str):
                            count += 1
                        while isinstance(self.map[self.row_index + count][self.column_index + 3], pygame.Rect):
                            count += 1
                    except IndexError:
                        return
                    distance = self.map[self.row_index + count - 1][self.column_index + 3].bottom - self.rect.top
                    self.updateFlag = [True, "right", distance]
                return
            else:
                self.go_right()
        elif direction == "up":
            if isinstance(self.map[self.row_index - 1][self.column_index], pygame.Rect) or \
                    isinstance(self.map[self.row_index - 1][self.column_index + 1], pygame.Rect) or \
                    isinstance(self.map[self.row_index - 1][self.column_index + 2], pygame.Rect):
                if self.direction == "left":
                    count = 2
                    try:
                        while isinstance(self.map[self.row_index - 1][self.column_index + count], str):
                            count -= 1
                        while isinstance(self.map[self.row_index - 1][self.column_index + count], pygame.Rect):
                            count -= 1
                    except IndexError:
                        return
                    distance = abs(self.rect.right - self.map[self.row_index - 1][self.column_index + count + 1].left)
                    self.updateFlag = [True, "up", distance]
                elif self.direction == "right":
                    count = 0
                    try:
                        while isinstance(self.map[self.row_index - 1][self.column_index + count], str):
                            count += 1
                            if self.column_index + count > len(self.map[self.row_index - 1]) - 1:
                                return
                        while isinstance(self.map[self.row_index - 1][self.column_index + count], pygame.Rect):
                            count += 1
                            if self.column_index + count > len(self.map[self.row_index - 1]) - 1:
                                return
                    except IndexError:
                        return
                    distance = self.map[self.row_index - 1][self.column_index + count - 1].right - self.rect.left
                    self.updateFlag = [True, "up", distance]
            else:
                self.go_up()
        elif direction == "down":
            if isinstance(self.map[self.row_index + 3][self.column_index], pygame.Rect) or \
                    isinstance(self.map[self.row_index + 3][self.column_index + 1], pygame.Rect) or \
                    isinstance(self.map[self.row_index + 3][self.column_index + 2], pygame.Rect):
                if self.direction == "left":
                    count = 2
                    try:
                        while isinstance(self.map[self.row_index + 3][self.column_index + count], str):
                            count -= 1
                        while isinstance(self.map[self.row_index + 3][self.column_index + count], pygame.Rect):
                            count -= 1
                    except IndexError:
                        return
                    distance = abs(self.rect.right - self.map[self.row_index + 3][self.column_index + count + 1].left)
                    self.updateFlag = [True, "down", distance]
                elif self.direction == "right":
                    count = 0
                    try:
                        while isinstance(self.map[self.row_index + 3][self.column_index + count], str):
                            count += 1
                            if self.column_index + count > len(self.map[self.row_index+3]) - 1:
                                return
                        while isinstance(self.map[self.row_index + 3][self.column_index + count], pygame.Rect):
                            count += 1
                            if self.column_index + count > len(self.map[self.row_index+3]) - 1:
                                return
                    except IndexError:
                        return
                    distance = abs(self.map[self.row_index + 3][self.column_index + count - 1].right - self.rect.left)
                    self.updateFlag = [True, "down", distance]
            else:
                self.go_down()

    def go_left(self):
        if isinstance(self.map[self.row_index][self.column_index - 1], pygame.Rect) or \
                isinstance(self.map[self.row_index + 1][self.column_index - 1], pygame.Rect) or \
                isinstance(self.map[self.row_index + 2][self.column_index - 1], pygame.Rect):
            return
        self.mapCounter = 0
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
        if isinstance(self.map[self.row_index][self.column_index + 3], pygame.Rect) or \
                isinstance(self.map[self.row_index + 1][self.column_index + 3], pygame.Rect) or \
                isinstance(self.map[self.row_index + 2][self.column_index + 3], pygame.Rect):
            return
        self.mapCounter = 0
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
        if isinstance(self.map[self.row_index - 1][self.column_index], pygame.Rect) or \
                isinstance(self.map[self.row_index - 1][self.column_index + 1], pygame.Rect) or \
                isinstance(self.map[self.row_index - 1][self.column_index + 2], pygame.Rect):
            return
        self.mapCounter = 0
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
        self.mapCounter = 0
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
