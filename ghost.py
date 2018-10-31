import pygame
import time


class Ghost:
    def __init__(self, clock, image_library, screen, settings, sounds, x, y):
        self.screen = screen
        self.clock = clock
        self.settings = settings
        self.vulnerable_image_lib = image_library[self.settings.VulnerableIndices[0]:
                                                  self.settings.VulnerableIndices[1]]
        self.sound_lib = sounds
        self.vulnerableImage = self.vulnerable_image_lib[0]
        self.vulnerableIndex = 0
        self.vulnerable_white_lib = [image_library[49], image_library[51]]
        self.coordinates = [x, y]
        self.index = None
        self.image_lib = None
        self.image = None
        self.rect = None
        self.vulnerable = False
        self.vulnerableTimer = 8
        self.delta_t = 0

        self.ghostFont = pygame.font.Font('Fonts/PFont.ttf', 30)
        self.twoHunImg = self.ghostFont.render("200", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.fourHunImg = self.ghostFont.render("400", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.eightHunImg = self.ghostFont.render("800", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.sixteenHunImg = self.ghostFont.render("1600", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.twoRect = self.twoHunImg.get_rect()
        self.fourRect = self.fourHunImg.get_rect()
        self.eightRect = self.eightHunImg.get_rect()
        self.sixteenRect = self.sixteenHunImg.get_rect()
        self.scoreList = [self.twoHunImg, self.fourHunImg, self.eightHunImg, self.sixteenHunImg]
        self.rectList = [self.twoRect, self.fourRect, self.eightRect, self.sixteenRect]

    def blit(self):
        if not self.vulnerable:
            self.screen.blit(self.image, self.rect)
        elif self.vulnerableTimer > 3:
            self.screen.blit(self.vulnerable_image_lib[self.vulnerableIndex], self.rect)
        else:
            self.screen.blit(self.vulnerable_white_lib[self.vulnerableIndex], self.rect)

    def reset(self):
        self.rect.x = self.coordinates[0]
        self.rect.y = self.coordinates[1]
        self.index = 4

    def change_image(self):
        if not self.vulnerable:
            if self.index % 2 == 0:
                self.index += 1
                self.image = self.image_lib[self.index]
            else:
                self.index -= 1
                self.image = self.image_lib[self.index]
        else:
            self.vulnerableTimer -= self.delta_t
            self.delta_t = 0.1
            if self.vulnerableTimer <= 0:
                self.vulnerable = False
                self.settings.resetPacEaten = True
            if self.vulnerableIndex == 0:
                self.vulnerableIndex = 1
            else:
                self.vulnerableIndex = 0

    def set_vulnerable(self):
        self.vulnerable = True
        self.vulnerableTimer = 10
        self.delta_t = 0

    def die(self, value):
        pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.rect)
        if value == 1:
            self.twoRect.x = self.rect.x - 5
            self.twoRect.y = self.rect.y + 10
            self.screen.blit(self.twoHunImg, self.twoRect)
        elif value == 2:
            self.fourRect.x = self.rect.x - 5
            self.fourRect.y = self.rect.y + 10
            self.screen.blit(self.fourHunImg, self.fourRect)
        elif value == 3:
            self.eightRect.x = self.rect.x - 5
            self.eightRect.y = self.rect.y + 10
            self.screen.blit(self.eightHunImg, self.eightRect)
        elif value == 4:
            self.sixteenRect.x = self.rect.x - 5
            self.sixteenRect.y = self.rect.y + 10
            self.screen.blit(self.sixteenHunImg, self.sixteenRect)
        pygame.display.flip()
        time.sleep(2)
        pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.sixteenRect)
        self.vulnerable = False


class Blinky(Ghost):
    def __init__(self, clock, image_library, screen, settings, sounds, x, y):
        super().__init__(clock, image_library, screen, settings, sounds, x, y)
        self.image_lib = image_library[settings.BlinkyIndices[0]: settings.BlinkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Clyde(Ghost):
    def __init__(self, clock, image_library, screen, settings, sounds, x, y):
        super().__init__(clock, image_library, screen, settings, sounds, x, y)
        self.image_lib = image_library[settings.ClydeIndices[0]: settings.ClydeIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Inky(Ghost):
    def __init__(self, clock, image_library, screen, settings, sounds, x, y):
        super().__init__(clock, image_library, screen, settings, sounds, x, y)
        self.image_lib = image_library[settings.InkyIndices[0]: settings.InkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pinky(Ghost):
    def __init__(self, clock, image_library, screen, settings, sounds, x, y):
        super().__init__(clock, image_library, screen, settings, sounds, x, y)
        self.image_lib = image_library[settings.PinkyIndices[0]: settings.PinkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
