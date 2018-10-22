import pygame
import time


class Ghost:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.index = None
        self.image_lib = None
        self.image = None
        self.rect = None

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def change_image(self):
        if self.index % 2 == 0:
            self.index += 1
            self.image = self.image_lib[self.index]
        else:
            self.index -= 1
            self.image = self.image_lib[self.index]


class Blinky(Ghost):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(screen, settings)
        self.image_lib = image_library[settings.BlinkyIndices[0]: settings.BlinkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Clyde(Ghost):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(screen, settings)
        self.image_lib = image_library[settings.ClydeIndices[0]: settings.ClydeIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Inky(Ghost):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(screen, settings)
        self.image_lib = image_library[settings.InkyIndices[0]: settings.InkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pinky(Ghost):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(screen, settings)
        self.image_lib = image_library[settings.PinkyIndices[0]: settings.PinkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y