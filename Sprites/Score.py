class Score():

    def __init__(self, pygame, gameData):
        self.gameData = gameData
        self.scoreFont = pygame.font.SysFont(None, 48)
        self.set_coords(gameData.get("WIDTH") - gameData.get("WIDTH")//11 , 10)
        gameData.get("GAME_EVENT_BUS").add_subscriber(self)

    def get_image(self):
        scoreImg = self.scoreFont.render(str(self.gameData.get("GAME_SCORE")), True, (255, 255, 0))
        return scoreImg

    def on_event(self, event):
        name = event.get_name()

    def get_cords(self):
        return self.x, self.y

    def set_coords(self, x, y):
        self.x = x
        self.y = y