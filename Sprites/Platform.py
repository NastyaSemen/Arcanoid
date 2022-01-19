from Sprites import Sprite


class Platform(Sprite.Sprite):

    def __init__(self, gameData):
        self.gameData = gameData
        gameData.get("MOVE_EVENT_BUS").add_subscriber(self)
        gameData.get("GAME_EVENT_BUS").add_subscriber(self)
        self.x = gameData.get("WIDTH") // 2
        self.y = gameData.get("HEIGHT") - gameData.get("HEIGHT") // 4
        gameData.set("START_PLATFORM_X", self.x)
        gameData.set("START_PLATFORM_Y", self.y)
        super().__init__(self.x, self.y, 'Platform.png')
        gameData.set("PLATFORM_X", self.x)
        gameData.set("PLATFORM_Y", self.y)
        gameData.set("PLATFORM_WIDTH", 200)
        gameData.set("PLATFORM_HEIGHT", 30)
        gameData.set("PLATFORM_SPEED", 10)


    def on_event(self, event):
        name = event.get_name()
        if name == 'MOVE_LEFT':
            self.x -= self.gameData.get("PLATFORM_SPEED")
            self.gameData.set("PLATFORM_X", self.x)
        elif name == 'MOVE_RIGHT':
            self.x += self.gameData.get("PLATFORM_SPEED")
            self.gameData.set("PLATFORM_X", self.x)
        elif name == 'START_GAME' or name == 'LOSE_BALL':
            self.restart()

    def restart(self):
        if (self.gameData.get("START_PLATFORM_X") != None):
            self.x = self.gameData.get("START_PLATFORM_X")
        else:
            self.x = self.gameData.get("WIDTH") // 2
        if (self.gameData.get("START_PLATFORM_Y") != None):
            self.y = self.gameData.get("START_PLATFORM_Y")
        else:
            self.y = self.gameData.get("HEIGHT") - self.gameData.get("HEIGHT") // 4
        self.gameData.set("PLATFORM_X", self.x)
        self.gameData.set("PLATFORM_Y", self.y)
        self.set_coords(self.x, self.y)