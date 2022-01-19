from Sprites.Heart import Heart

class GameLogic:

    lives = 3

    def __init__(self, gameData):
        self.gameData = gameData
        gameData.get("GAME_EVENT_BUS").add_subscriber(self)
        self.restart()

    def restart(self):
        self.lives = 3
        self.drawHearts()
        self.gameData.set("GAME_SCORE", 0)
        self.gameData.set("BALL_SPEED", self.gameData.get("START_BALL_SPEED"))


    def drawHearts(self):
        sprites = self.gameData.get("SPRITES")
        sprites["HEARTH1"] = Heart(20, 10)
        sprites["HEARTH2"] = Heart(55, 10)
        sprites["HEARTH3"] = Heart(90, 10)

    def on_event(self, event):
        name = event.get_name()
        if name == 'LOSE_BALL':
            hearthName = "HEARTH" + str(self.lives)
            sprites = self.gameData.get("SPRITES")
            if sprites.get(hearthName) != None:
                sprites.pop("HEARTH" + str(self.lives))
            self.lives -= 1
            if self.lives < 1:
                self.gameData.set("GAME_OVER", True)
                self.gameData.set("IN_GAME", False)
        if name == 'PLATFORM_CROSS':
            self.gameData.set("GAME_SCORE", self.gameData.get("GAME_SCORE") + 10)
            self.gameData.set("BALL_SPEED", self.gameData.get("BALL_SPEED") + 0.1)
        if name == 'WALL_CROSS':
            self.gameData.set("GAME_SCORE", self.gameData.get("GAME_SCORE") + 5)
            self.gameData.set("BALL_SPEED", self.gameData.get("BALL_SPEED") + 0.1)
        if name == 'START_GAME':

            self.restart()
