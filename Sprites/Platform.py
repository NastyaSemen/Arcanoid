from Sprites import Sprite


class Platform(Sprite.Sprite):

    def __init__(self, gameData):
        self.gameData = gameData
        self.x = gameData.get("WIDTH")//2
        self.y = gameData.get("HEIGHT") - gameData.get("HEIGHT")//4
        gameData.get("MOVE_EVENT_BUS").add_subscriber(self)
        gameData.set("PLATFORM_X", self.x)
        gameData.set("PLATFORM_Y", self.y)
        gameData.set("PLATFORM_WIDTH", 200)
        gameData.set("PLATFORM_HEIGHT", 30)
        gameData.set("PLATFORM_SPEED", 10)
        super().__init__(self.x, self.y, 'Platform.png')

    def on_event(self, event):
        name = event.get_name()
        if name == 'MOVE_LEFT':
            self.x -= self.gameData.get("PLATFORM_SPEED")
            self.gameData.set("PLATFORM_X", self.x)
        elif name == 'MOVE_RIGHT':
            self.x += self.gameData.get("PLATFORM_SPEED")
            self.gameData.set("PLATFORM_X", self.x)
