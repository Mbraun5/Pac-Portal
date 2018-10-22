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
        self.highScoreTextImage = self.font.render("HIGH SCORE", True, self.settings.whiteFont,
                                                   self.settings.get_bg_color())
        self.highScoreTextRect = self.highScoreTextImage.get_rect()
        self.highScoreTextRect.bottom = self.map[0][int(len(self.map[0]) / 2)].top - 50
        self.highScoreTextRect.centerx = self.map[0][int(len(self.map[0]) / 2)].left

        self.highScoreValueImage = self.font.render("{}".format(self.highScore), True, self.settings.yellowFont,
                                                    self.settings.get_bg_color())
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
        self.livesRectList = [self.livesRect]

        self.blit()
        self.blit_lives()

    def blit(self):
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.currentScoreImage, self.currentScoreRect)
        self.screen.blit(self.highScoreTextImage, self.highScoreTextRect)
        self.screen.blit(self.highScoreValueImage, self.highScoreValueRect)
        self.screen.blit(self.livesTextImage, self.livesTextRect)

    def update_lives(self, value):
        if self.numberOfLives < 7:
            self.numberOfLives += value
            self.prep_lives()
        if self.numberOfLives <= 0:
            self.game_over()

    def update_score(self, value):
        self.currentScore = self.game_str(int(self.currentScore) + value)
        self.prep_score()

    def prep_score(self):
        if int(self.highScore) < int(self.currentScore):
            self.highScore = self.currentScore
            pygame.draw.rect(self.screen, self.settings.blackFont, self.highScoreValueRect)
            self.highScoreValueImage = self.font.render("{}".format(self.highScore), True, self.settings.yellowFont,
                                                        self.settings.get_bg_color())
            self.highScoreValueRect = self.highScoreValueImage.get_rect()
            self.highScoreValueRect.centerx = self.highScoreTextRect.centerx
            self.highScoreValueRect.top = self.highScoreTextRect.bottom
        pygame.draw.rect(self.screen, self.settings.blackFont, self.currentScoreRect)
        self.currentScoreImage = self.font.render("{}".format(self.currentScore), True, self.settings.yellowFont,
                                                  self.settings.get_bg_color())
        self.currentScoreRect = self.currentScoreImage.get_rect()
        self.currentScoreRect.top = self.scoreRect.top
        self.currentScoreRect.left = self.scoreRect.right
        self.blit()

    def prep_lives(self):
        self.livesRectList = [self.livesRect]                   # Original rect to recognize placement
        for i in range(1, self.numberOfLives):
            newRect = self.livesRectList[i - 1].copy()          # Creates new rects for every life
            newRect.top = self.livesRectList[i - 1].top
            newRect.left = self.livesRectList[i - 1].right      # Places new life image next to previous one.
            self.livesRectList.append(newRect)

    def blit_lives(self):
        self.prep_lives()
        for life in self.livesRectList:
            self.screen.blit(self.livesImage, life)

    def game_over(self):
        pass    # todo

    def get_high_score(self):
        try:                                                    # Generates high score string of form "0000"
            with open('high score.txt', 'r') as f:
                high_score_value = int(f.readline())
                high_score_str = self.game_str(high_score_value)
        except FileNotFoundError:                               # Creates a blank file if file not found.
            with open('high score.txt', 'w') as f:
                f.write('0000')
                high_score_str = '0000'
        return high_score_str

    @staticmethod
    def game_str(score):
        if score < 1000:
            if score < 100:
                if score < 10:
                    score_str = "000" + str(score)
                    return score_str
                score_str = "00" + str(score)
                return score_str
            score_str = "0" + str(score)
            return score_str
        return str(score)
