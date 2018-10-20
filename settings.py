class Settings:
    def __init__(self):
        #   Screen Settings
        self.__screenWidth = 1200
        self.__screenHeight = 1000
        self.__bgColor = (0, 0, 0)

        #   Game Settings
        self.__gameTitle = "Pacman Portal"

        #   Maze Settings
        self.__squareRect = 17
        self.__squareRectColor = (60, 30, 255)

    def get_bg_color(self):
        return self.__bgColor

    def get_game_title(self):
        return self.__gameTitle

    def get_screen_width(self):
        return self.__screenWidth

    def get_screen_height(self):
        return self.__screenHeight

    #   Maze Functions
    def get_square_rect(self):
        return self.__squareRect

    def get_square_rect_color(self):
        return self.__squareRectColor