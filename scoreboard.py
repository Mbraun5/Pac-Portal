import pygame


class ScoreBoard:
    def __init__(self, maze, screen, settings):
        self.screen = screen
        self.settings = settings
        self.map = maze.map
        self.highScore = self.get_high_score()

        #   Text Settings
        self.font = pygame.font.Font('Fonts/PFont.ttf', 45)

        #   Current Score Image
        self.scoreImage = self.font.render("SCORE: ", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.top = self.map[len(self.map) - 1][0].bottom + 10
        self.scoreRect.left = self.map[len(self.map) - 1][0].left

        self.currentScore = '0000'
        self.currentScoreImage = self.font.render("{}".format(self.currentScore), True, self.settings.yellowFont,
                                                  self.settings.get_bg_color())
        self.currentScoreRect = self.currentScoreImage.get_rect()
        self.currentScoreRect.top = self.scoreRect.top
        self.currentScoreRect.left = self.scoreRect.right

        #   High Score Image
        self.highScoreTextImage = self.font.render("HIGH SCORE", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.highScoreTextRect = self.highScoreTextImage.get_rect()
        self.highScoreTextRect.bottom = self.map[0][int(len(self.map[0]) / 2)].top - 50
        self.highScoreTextRect.centerx = self.map[0][int(len(self.map[0]) / 2)].left

        self.highScoreValueImage = self.font.render("{}".format(self.highScore), True, self.settings.yellowFont, self.settings.get_bg_color())
        self.highScoreValueRect = self.highScoreValueImage.get_rect()
        self.highScoreValueRect.centerx = self.highScoreTextRect.centerx
        self.highScoreValueRect.top = self.highScoreTextRect.bottom

        #   Lives Image
        self.numberOfLives = 2
        self.livesTextImage = self.font.render("LIVES:", True, self.settings.whiteFont, self.settings.get_bg_color())
        self.livesTextRect = self.livesTextImage.get_rect()
        self.livesTextRect.left = self.currentScoreRect.right + 180
        self.livesTextRect.bottom = self.currentScoreRect.bottom

        #   Pac Image for lives
        self.livesImage = pygame.transform.flip(maze.image_lib[self.settings.pacIndexes[1]], True, False)
        self.livesRect = self.livesImage.get_rect()
        self.livesRect.top = self.livesTextRect.top
        self.livesRect.left = self.livesTextRect.right + 5

    def blit(self):
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.currentScoreImage, self.currentScoreRect)
        self.screen.blit(self.highScoreTextImage, self.highScoreTextRect)
        self.screen.blit(self.highScoreValueImage, self.highScoreValueRect)
        self.screen.blit(self.livesTextImage, self.livesTextRect)
        self.screen.blit(self.livesImage, self.livesRect)

    @staticmethod
    def get_high_score():
        try:
            with open('high score.txt', 'r') as f:
                high_score_value = int(f.readline())
                high_score_str = str(high_score_value)
                if high_score_value < 1000:
                    if high_score_value < 100:
                        if high_score_value < 10:
                            high_score_str = "000" + str(high_score_value)
                            return high_score_str
                        high_score_str = "00" + str(high_score_value)
                        return high_score_str
                    high_score_str = "0" + str(high_score_value)
        except FileNotFoundError:
            with open('high score.txt', 'w') as f:
                f.write('0000')
                high_score_str = '0000'
        return high_score_str
