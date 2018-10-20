import pygame


class PacMan:
    def __init__(self, image_library, screen, settings):
        self.screen = screen
        self.settings = settings
        self.images = []
        for index in self.settings.pacIndexes:
            self.images.append(image_library[index])

        self.blitCounter = 0
        self.blitIndex = 1
        self.indexInc = 1
        self.rect = self.images[0].get_rect()

        self.speed = self.settings.pacSpeed
        self.direction = "right"
        self.moving = True

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

    def update(self):
        if self.moving:
            if self.direction == "right" or self.direction == "left":
                self.rect.x += self.speed
            else:
                self.rect.y += self.speed

    def go_left(self):
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

    def go_right(self):
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

    def go_up(self):
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

    def go_down(self):
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
