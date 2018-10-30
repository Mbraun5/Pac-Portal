import pygame
import time
import pac
import ghost
import powerpill
import sys
import gameFunctions as gF


class TitleScreen:
    def __init__(self, clock, pac_images, image_library, screen, settings):
        self.clock = clock
        self.image_library = image_library
        self.screen = screen
        self.settings = settings
        self.pac_images = pac_images
        self.regularPacImages = pac_images.copy()
        for index, image in enumerate(self.pac_images):
            self.pac_images[index] = pygame.transform.rotozoom(image, 0, 3)

        # Text Settings
        self.font = pygame.font.Font('Fonts/PFont.ttf', 150)
        self.ghostFont = pygame.font.Font('Fonts/PFont.ttf', 30)
        self.playFontOne = pygame.font.Font('Fonts/PFont.ttf', 50)
        self.playFontTwo = pygame.font.Font('Fonts/PFont.ttf', 75)

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

        self.clydeImg = self.ghostFont.render("\"CLYDE\"", True, (255, 136, 0), self.settings.get_bg_color())
        self.inkyImg = self.ghostFont.render("\"INKY\"", True, (0, 255, 255), self.settings.get_bg_color())
        self.pinkyImg = self.ghostFont.render("\"PINKY\"", True, (222, 129, 145), self.settings.get_bg_color())
        self.blinkyImg = self.ghostFont.render("\"BLINKY\"", True, (255, 0, 0), self.settings.get_bg_color())
        self.clydeRect = self.clydeImg.get_rect()
        self.inkyRect = self.inkyImg.get_rect()
        self.pinkyRect = self.pinkyImg.get_rect()
        self.blinkyRect = self.blinkyImg.get_rect()

        self.titleMessageOne = self.font.render("PA", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.titleMessageTwo = self.font.render("MAN", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.oneRect = self.titleMessageOne.get_rect()
        self.oneRect.top = 100
        self.oneRect.centerx = self.settings.get_screen_width() / 2 - 150
        self.twoRect = self.titleMessageTwo.get_rect()
        self.twoRect.top = self.oneRect.top
        self.twoRect.x = self.oneRect.right + 100

        self.playImgOne = self.playFontOne.render("PLAY GAME", True, self.settings.whiteFont,
                                                  self.settings.get_bg_color())
        self.playImgTwo = self.playFontTwo.render("PLAY GAME", True, self.settings.whiteFont,
                                                  self.settings.get_bg_color())
        self.playRectOne = self.playImgTwo.get_rect()
        self.playRectOne.centerx = self.settings.get_screen_width() / 2 + 100
        self.playRectOne.y = 1000
        self.playRectTwo = self.playImgTwo.get_rect()
        self.playRectTwo.centerx = self.settings.get_screen_width() / 2 + 50
        self.playRectTwo.y = 1000

        self.hsImgOne = self.playFontOne.render("HIGH SCORES", True, self.settings.whiteFont,
                                                self.settings.get_bg_color())
        self.hsImgTwo = self.playFontTwo.render("HIGH SCORES", True, self.settings.whiteFont,
                                                self.settings.get_bg_color())
        self.hsRectOne = self.hsImgTwo.get_rect()
        self.hsRectOne.centerx = self.settings.get_screen_width() / 2 + 100
        self.hsRectOne.y = 1100
        self.hsRectTwo = self.hsImgTwo.get_rect()
        self.hsRectTwo.centerx = self.settings.get_screen_width() / 2 + 50
        self.hsRectTwo.y = 1100

        self.pRect = self.pac_images[0].get_rect()
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
        self.pacman = pac.PacMan([300, self.settings.get_screen_height() / 2], image_library, screen, settings,
                                 sound_lib=None)
        self.blinky = ghost.Blinky(self.clock, image_library, screen, settings, 200,
                                   self.settings.get_screen_height() / 2)
        self.inky = ghost.Inky(self.clock, image_library, screen, settings, 155, self.settings.get_screen_height() / 2)
        self.clyde = ghost.Clyde(self.clock, image_library, screen, settings, 110,
                                 self.settings.get_screen_height() / 2)
        self.pinky = ghost.Pinky(self.clock, image_library, screen, settings, 65, self.settings.get_screen_height() / 2)
        self.ghosts = [self.blinky, self.pinky, self.inky, self.clyde]
        self.fakeGhosts = self.ghosts.copy()
        self.loop = True
        self.title_loop()

    def title_loop(self):
        self.init_start_settings()
        while self.loop:
            self.screen.fill(self.settings.get_bg_color())
            pygame.display.flip()
            while self.pRect.left < 516:
                self.check_events()
                if not self.loop:
                    break
                self.pRect.x += self.speed
                self.screen.blit(self.pac_images[self.index], self.pRect)
                self.check_time()
                pygame.display.flip()
            self.index = 2
            self.screen.blit(self.pac_images[self.index], self.pRect)
            pygame.display.flip()

            self.screen.blit(self.titleMessageOne, self.oneRect)
            self.screen.blit(self.titleMessageTwo, self.twoRect)
            self.screen.blit(self.playImgOne, self.playRectOne)
            self.screen.blit(self.hsImgOne, self.hsRectOne)
            while self.loop:
                self.init_settings()
                while self.pacman.rect.x < self.pill.rect.x - 10:
                    self.check_events()
                    if not self.loop:
                        break
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
                    self.check_events()
                    if not self.loop:
                        break
                    self.blit_all()
                    pygame.display.flip()
                    self.update_all()
                    self.check_collisions()

                self.screen.fill(self.settings.get_bg_color())
                self.screen.blit(self.pac_images[2], self.pRect)
                self.screen.blit(self.titleMessageOne, self.oneRect)
                self.screen.blit(self.titleMessageTwo, self.twoRect)
                self.screen.blit(self.playImgOne, self.playRectOne)
                self.screen.blit(self.hsImgOne, self.hsRectOne)
                pygame.display.flip()

                while self.pacman.rect.right > 0:
                    self.check_events()
                    if not self.loop:
                        break
                    self.update_all()
                    self.blit_all()
                    pygame.display.flip()

                self.ghostSpeed = 3
                self.blinky_loop()
                self.pinky_loop()
                self.inky_loop()
                self.clyde_loop()

    @staticmethod
    def check_keydown_events(event):
        if event == pygame.K_q:
            sys.exit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playRectTwo.collidepoint(pygame.mouse.get_pos()):
                    self.loop = False
                elif self.hsRectTwo.collidepoint(pygame.mouse.get_pos()):
                    self.high_score_screen()
                    self.title_loop()
                    self.loop = False
        if self.playRectOne.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.playRectOne)
            self.screen.blit(self.playImgTwo, self.playRectTwo)
        else:
            pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.playRectTwo)
            self.screen.blit(self.playImgOne, self.playRectOne)
        if self.hsRectOne.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.hsRectOne)
            self.screen.blit(self.hsImgTwo, self.hsRectTwo)
        else:
            pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.hsRectTwo)
            self.screen.blit(self.hsImgOne, self.hsRectOne)

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

    def blinky_loop(self):
        self.fakeGhosts = [self.blinky]
        self.fakeGhosts[0].rect.x = -45
        self.fakeGhosts[0].vulnerable = False
        while self.fakeGhosts[0].rect.x < self.settings.get_screen_width() / 2 + 100:
            self.check_events()
            if not self.loop:
                break
            self.update_all()
            self.blit_all()
            pygame.display.flip()
        self.blinkyRect.x = self.fakeGhosts[0].rect.x - 200
        self.blinkyRect.top = self.fakeGhosts[0].rect.top
        self.screen.blit(self.blinkyImg, self.blinkyRect)
        for i in range(0, 50):
            self.check_events()
            if not self.loop:
                break
            self.check_time()
            self.blit_all()
            pygame.display.flip()
        pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.blinkyRect)
        while self.fakeGhosts[0].rect.x < self.settings.get_screen_width() + 45:
            self.check_events()
            if not self.loop:
                break
            self.update_all()
            self.blit_all()
            pygame.display.flip()

    def pinky_loop(self):
        self.fakeGhosts = [self.pinky]
        self.fakeGhosts[0].rect.x = -45
        self.fakeGhosts[0].vulnerable = False
        while self.fakeGhosts[0].rect.x < self.settings.get_screen_width() / 2 + 100:
            self.check_events()
            if not self.loop:
                break
            self.update_all()
            self.blit_all()
            pygame.display.flip()
        self.pinkyRect.x = self.fakeGhosts[0].rect.x - 200
        self.pinkyRect.top = self.fakeGhosts[0].rect.top
        self.screen.blit(self.pinkyImg, self.pinkyRect)
        for i in range(0, 50):
            self.check_events()
            if not self.loop:
                break
            self.check_time()
            self.blit_all()
            pygame.display.flip()
        pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.blinkyRect)
        while self.fakeGhosts[0].rect.x < self.settings.get_screen_width() + 45:
            self.check_events()
            if not self.loop:
                break
            self.update_all()
            self.blit_all()
            pygame.display.flip()

    def inky_loop(self):
        self.fakeGhosts = [self.inky]
        self.fakeGhosts[0].rect.x = -45
        self.fakeGhosts[0].vulnerable = False
        while self.fakeGhosts[0].rect.x < self.settings.get_screen_width() / 2 + 100:
            self.check_events()
            if not self.loop:
                break
            self.update_all()
            self.blit_all()
            pygame.display.flip()
        self.inkyRect.x = self.fakeGhosts[0].rect.x - 200
        self.inkyRect.top = self.fakeGhosts[0].rect.top
        self.screen.blit(self.inkyImg, self.inkyRect)
        for i in range(0, 50):
            self.check_events()
            if not self.loop:
                break
            self.check_time()
            self.blit_all()
            pygame.display.flip()
        pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.blinkyRect)
        while self.fakeGhosts[0].rect.x < self.settings.get_screen_width() + 45:
            self.check_events()
            if not self.loop:
                break
            self.update_all()
            self.blit_all()
            pygame.display.flip()

    def clyde_loop(self):
        self.fakeGhosts = [self.clyde]
        self.fakeGhosts[0].rect.x = -45
        self.fakeGhosts[0].vulnerable = False
        while self.fakeGhosts[0].rect.x < self.settings.get_screen_width() / 2 + 100:
            self.check_events()
            if not self.loop:
                break
            self.update_all()
            self.blit_all()
            pygame.display.flip()
        self.clydeRect.x = self.fakeGhosts[0].rect.x - 200
        self.clydeRect.top = self.fakeGhosts[0].rect.top
        self.screen.blit(self.clydeImg, self.clydeRect)
        for i in range(0, 50):
            self.check_events()
            if not self.loop:
                break
            self.check_time()
            self.blit_all()
            pygame.display.flip()
        pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.blinkyRect)
        while self.fakeGhosts[0].rect.x < self.settings.get_screen_width() + 45:
            self.check_events()
            if not self.loop:
                break
            self.update_all()
            self.blit_all()
            pygame.display.flip()

    def init_settings(self):
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
        self.pill = powerpill.LargePowerPill(self.image_library, self.screen, self.settings, 1000,
                                             self.settings.get_screen_height() / 2 + 20)
        self.pacman = pac.PacMan([300, self.settings.get_screen_height() / 2], self.image_library, self.screen,
                                 self.settings, sound_lib=None)
        self.blinky = ghost.Blinky(self.clock, self.image_library, self.screen, self.settings, 200,
                                   self.settings.get_screen_height() / 2)
        self.inky = ghost.Inky(self.clock, self.image_library, self.screen, self.settings, 155,
                               self.settings.get_screen_height() / 2)
        self.clyde = ghost.Clyde(self.clock, self.image_library, self.screen, self.settings, 110,
                                 self.settings.get_screen_height() / 2)
        self.pinky = ghost.Pinky(self.clock, self.image_library, self.screen, self.settings, 65,
                                 self.settings.get_screen_height() / 2)
        self.ghosts = [self.blinky, self.pinky, self.inky, self.clyde]
        self.fakeGhosts = self.ghosts.copy()
        self.loop = True

    def init_start_settings(self):
        self.pRect = self.pac_images[0].get_rect()
        self.pRect.top = self.oneRect.top

    def refresh_screen(self):
        self.screen.fill(self.settings.get_bg_color())
        pygame.display.flip()

    def high_score_screen(self):
        self.screen.fill(self.settings.get_bg_color())
        font = pygame.font.Font('Fonts/PFont.ttf', 40)
        text_color = self.settings.whiteFont
        image_rect = None
        image_one_rect = None
        high_score_image = font.render("HIGH SCORES!", True, text_color, self.settings.get_bg_color())
        high_score_rect = high_score_image.get_rect()
        high_score_rect.centerx = self.settings.get_screen_width() / 2
        high_score_rect.y = 100
        self.screen.blit(high_score_image, high_score_rect)
        pygame.display.flip()
        try:
            with open("high score.txt") as f:
                score = f.readline()
                if score == "":
                    return
                score = score.strip('\n')
                image_one = font.render("Score: {}".format(score), True, text_color, self.settings.get_bg_color())
                image_one_rect = image_one.get_rect()
                image_one_rect.centerx = self.settings.get_screen_width() / 2
                image_one_rect.y = 200
                self.screen.blit(image_one, image_one_rect)
                pygame.display.flip()
                time.sleep(0.2)
                for count in range(0, 10):
                    score = f.readline()
                    if score == "":
                        break
                    score = score.strip('\n')
                    image = font.render("Score: {}".format(score), True, text_color, self.settings.get_bg_color())
                    image_rect = image.get_rect()
                    image_rect.left = image_one_rect.left
                    image_rect.top = image_one_rect.bottom
                    image_one_rect = image_rect
                    self.screen.blit(image, image_rect)
                    pygame.display.flip()
                    time.sleep(0.2)
        except FileNotFoundError:
            pass
        continue_image = font.render("PRESS SPACE TO CONTINUE, Q TO EXIT", True, text_color)
        continue_rect = continue_image.get_rect()
        try:
            continue_rect.centerx = image_rect.centerx
            continue_rect.top = image_rect.bottom + 50
        except AttributeError:
            continue_rect.centerx = image_one_rect.centerx
            continue_rect.top = image_one_rect.bottom + 50
        self.screen.blit(continue_image, continue_rect)
        pygame.display.flip()
        while gF.wait_for_space(0):
            continue
        self.screen.fill(self.settings.get_bg_color())

    @staticmethod
    #   Ensures a high score file is inside directory. If one is not there, makes one. If it is there, it does nothing.
    def create_high_score_file():
        try:
            with open('high score.txt', 'r') as f:
                f.close()
        except FileNotFoundError:
            with open('high score.txt', 'w') as f:
                f.write("0000")
