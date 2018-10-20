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
