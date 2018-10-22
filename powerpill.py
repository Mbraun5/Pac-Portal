import pygame


class PowerPill:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.image = None
        self.rect = None

    def blit(self):
        self.screen.blit(self.image, self.rect)


class SmallPowerPill(PowerPill):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(screen, settings)
        self.image = image_library[self.settings.smallPillIndex]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.value = self.settings.smallPillValue


class LargePowerPill(PowerPill):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(screen, settings)
        self.image_lib = image_library[settings.largePillIndices[0]: settings.largePillIndices[1]]
        self.image = self.image_lib[10]
        self.__rect = pygame.Rect(0, 0, self.settings.get_square_rect(), self.settings.get_square_rect())
        self.__rect.centerx = x
        self.__rect.centery = y
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.blitCounter = 0
        self.blitIndex = 1
        self.indexInc = 1

        self.value = self.settings.largePillValue

    def change_image(self):
        pygame.draw.rect(self.screen, self.settings.blackFont, self.rect)
        if self.blitIndex == 10 or self.blitIndex == 0:
            self.indexInc *= -1
        self.blitIndex += self.indexInc
        self.image = self.image_lib[self.blitIndex]
        self.rect.x = self.__rect.x - self.blitIndex / 2
