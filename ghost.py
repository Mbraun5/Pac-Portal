class Ghost:
    def __init__(self, image_library, screen, settings, x, y):
        self.screen = screen
        self.settings = settings
        self.vulnerable_image_lib = image_library[self.settings.VulnerableIndices[0]:
                                                  self.settings.VulnerableIndices[1]]
        self.vulnerableImage = self.vulnerable_image_lib[0]
        self.vulnerableIndex = 0
        self.coordinates = [x, y]
        self.index = None
        self.image_lib = None
        self.image = None
        self.rect = None
        self.vulnerable = False

    def blit(self):
        if not self.vulnerable:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.vulnerable_image_lib[self.vulnerableIndex], self.rect)

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
            if self.vulnerableIndex == 0:
                self.vulnerableIndex = 1
            else:
                self.vulnerableIndex = 0

    def set_vulnerable(self):
        self.vulnerable = True


class Blinky(Ghost):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(image_library, screen, settings, x, y)
        self.image_lib = image_library[settings.BlinkyIndices[0]: settings.BlinkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Clyde(Ghost):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(image_library, screen, settings, x, y)
        self.image_lib = image_library[settings.ClydeIndices[0]: settings.ClydeIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Inky(Ghost):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(image_library, screen, settings, x, y)
        self.image_lib = image_library[settings.InkyIndices[0]: settings.InkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pinky(Ghost):
    def __init__(self, image_library, screen, settings, x, y):
        super().__init__(image_library, screen, settings, x, y)
        self.image_lib = image_library[settings.PinkyIndices[0]: settings.PinkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
