class Ghost:
    def __init__(self, clock, image_library, screen, settings, x, y):
        self.screen = screen
        self.clock = clock
        self.settings = settings
        self.vulnerable_image_lib = image_library[self.settings.VulnerableIndices[0]:
                                                  self.settings.VulnerableIndices[1]]
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
            if self.vulnerableIndex == 0:
                self.vulnerableIndex = 1
            else:
                self.vulnerableIndex = 0

    def set_vulnerable(self):
        self.vulnerable = True
        self.vulnerableTimer = 10
        self.delta_t = 0


class Blinky(Ghost):
    def __init__(self, clock, image_library, screen, settings, x, y):
        super().__init__(clock, image_library, screen, settings, x, y)
        self.image_lib = image_library[settings.BlinkyIndices[0]: settings.BlinkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Clyde(Ghost):
    def __init__(self, clock, image_library, screen, settings, x, y):
        super().__init__(clock, image_library, screen, settings, x, y)
        self.image_lib = image_library[settings.ClydeIndices[0]: settings.ClydeIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Inky(Ghost):
    def __init__(self, clock, image_library, screen, settings, x, y):
        super().__init__(clock, image_library, screen, settings, x, y)
        self.image_lib = image_library[settings.InkyIndices[0]: settings.InkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pinky(Ghost):
    def __init__(self, clock, image_library, screen, settings, x, y):
        super().__init__(clock, image_library, screen, settings, x, y)
        self.image_lib = image_library[settings.PinkyIndices[0]: settings.PinkyIndices[1]]
        self.index = 4                                  # Ghosts start game looking up.
        self.image = self.image_lib[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
