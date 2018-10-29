import pygame
import time
import pac
import ghost
import powerpill


class TitleScreen:
    def __init__(self, clock, pacImages, image_library, screen, settings):
        self.clock = clock
        self.screen = screen
        self.settings = settings
        self.pacImages = pacImages
        self.regularPacImages = pacImages.copy()
        for index, image in enumerate(self.pacImages):
            self.pacImages[index] = pygame.transform.rotozoom(image, 0, 3)

        # Text Settings
        self.font = pygame.font.Font('Fonts/PFont.ttf', 150)
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

        self.titleMessageOne = self.font.render("PA", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.titleMessageTwo = self.font.render("MAN", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.oneRect = self.titleMessageOne.get_rect()
        self.oneRect.top = 100
        self.oneRect.centerx = self.settings.get_screen_width() / 2 - 150
        self.twoRect = self.titleMessageTwo.get_rect()
        self.twoRect.top = self.oneRect.top
        self.twoRect.x = self.oneRect.right + 100

        self.pRect = self.pacImages[0].get_rect()
        self.pRect.top = self.oneRect.top
        self.index = 1
        self.indexInc = 1
        self.speed = 5
        self.timer = 1
        self.timer2 = 0.5
        self.timer3 = 1.5
        self.delta_t = 0

        self.pacSpeed = 3
        self.ghostSpeed = 3
        self.collisioncounter = 0
        self.pill = powerpill.LargePowerPill(image_library, screen, settings, 1000,
                                             self.settings.get_screen_height() / 2 + 20)
        self.pacman = pac.PacMan([300, self.settings.get_screen_height() / 2], image_library, screen, settings)
        self.blinky = ghost.Blinky(image_library, screen, settings, 200, self.settings.get_screen_height() / 2)
        self.inky = ghost.Inky(image_library, screen, settings, 155, self.settings.get_screen_height() / 2)
        self.clyde = ghost.Clyde(image_library, screen, settings, 110, self.settings.get_screen_height() / 2)
        self.pinky = ghost.Pinky(image_library, screen, settings, 65, self.settings.get_screen_height() / 2)
        self.ghosts = [self.blinky, self.inky, self.clyde, self.pinky]
        self.fakeGhosts = []
        self.title_loop()

    def title_loop(self):
        self.fakeGhosts = self.ghosts.copy()
        self.ghostSpeed = 3
        self.pacSpeed = 3
        self.collisioncounter = 0
        print(len(self.pacImages))
        self.screen.fill(self.settings.get_bg_color())
        pygame.display.flip()
        while self.pRect.left < 516:
            self.pRect.x += self.speed
            self.screen.blit(self.pacImages[self.index], self.pRect)
            self.check_time()
            pygame.display.flip()
        self.index = 2
        self.screen.blit(self.pacImages[self.index], self.pRect)
        pygame.display.flip()

        self.screen.blit(self.titleMessageOne, self.oneRect)
        self.screen.blit(self.titleMessageTwo, self.twoRect)

        while self.pacman.rect.x < self.pill.rect.x - 10:
            self.pill.blit()
            self.blit_all()
            pygame.display.flip()
            self.update_all()

        for ghosts in self.fakeGhosts:
            ghosts.set_vulnerable()

        self.ghostSpeed = -1
        self.pacSpeed = -3
        for index, image in enumerate(self.pacman.images):
            self.pacman.images[index] = pygame.transform.flip(image, True, False)
        while len(self.fakeGhosts) > 0:
            self.blit_all()
            pygame.display.flip()
            self.update_all()
            self.check_collisions()
        time.sleep(5)

    def check_time(self):
        self.timer -= self.delta_t
        self.timer2 -= self.delta_t
        self.timer3 -= self.delta_t
        if self.timer <= 0:
            self.change_index()
            self.pacman.change_image()
            self.timer = 1
        self.delta_t = self.clock.tick(60) / 60
        if self.timer2 <= 0:
            self.pill.change_image()
            self.timer2 = 0.5
        if self.timer3 <= 0:
            for ghosts in self.fakeGhosts:
                ghosts.change_image()
            self.timer3 = 1.5

    def change_index(self):
        if self.index == 2 or self.index == 0:
            self.indexInc *= -1
        self.index += self.indexInc

    def update_all(self):
        self.pacman.rect.x += self.pacSpeed
        for ghosts in self.fakeGhosts:
            ghosts.rect.x += self.ghostSpeed
        self.check_time()

    def blit_all(self):
        for ghosts in self.fakeGhosts:
            ghosts.blit()
        self.pacman.blit()

    def check_collisions(self):
        for index, ghosts in enumerate(self.fakeGhosts):
            if pygame.Rect.colliderect(ghosts.rect, self.pacman.rect):
                pygame.draw.rect(self.screen, self.settings.get_bg_color(), ghosts.rect)
                self.rectList[self.collisioncounter].x = ghosts.rect.x
                self.rectList[self.collisioncounter].y = ghosts.rect.y
                self.fakeGhosts.pop(index)
                self.screen.blit(self.scoreList[self.collisioncounter], self.rectList[self.collisioncounter])
                pygame.display.flip()
                time.sleep(0.5)
                self.collisioncounter += 1
