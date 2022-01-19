class StartEnd():

    def __init__(self, pygame, gameData):
        self.text = ""
        self.gameData = gameData
        self.scoreFont = pygame.font.SysFont(None, 102)
        self.set_coords(200 , gameData.get("HEIGHT")//2)
        gameData.get("GAME_EVENT_BUS").add_subscriber(self)

    def get_image(self):
        scoreImg = self.scoreFont.render(self.text, True, (255, 255, 0))
        return scoreImg

    def on_event(self, event):
        name = event.get_name()
        if name == 'UPDATE_SCREEN':
            if self.gameData.get("IN_GAME"):
                self.text = ""
            elif self.gameData.get("GAME_OVER"):
                self.text = "GAME OVER"
            elif not self.gameData.get("GAME_OVER"):
                self.text = "START GAME"


    def get_cords(self):
        return self.x, self.y

    def set_coords(self, x, y):
        self.x = x
        self.y = y