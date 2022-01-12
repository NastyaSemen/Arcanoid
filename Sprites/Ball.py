from Sprites import Sprite
from Event.Event import Event

class Ball(Sprite.Sprite):

    onPlatform = True
    lost = False
    direction = "NE"

    def __init__(self, gameData):
        self.gameData = gameData
        gameData.set("BALL_WIDTH", 30)
        gameData.set("BALL_HEIGHT", 30)
        gameData.set("BALL_SPEED", 3)
        self.initStartPosition()
        gameData.get("MOVE_EVENT_BUS").add_subscriber(self)
        gameData.get("GAME_EVENT_BUS").add_subscriber(self)
        super().__init__(self.x, self.y, 'Ball.png')

    def on_event(self, event):
        name = event.get_name()
        if self.onPlatform:
            if name == 'MOVE_LEFT':
                self.x -= self.gameData.get("PLATFORM_SPEED")
                self.gameData.set("BALL_X", self.x)
            elif name == 'MOVE_RIGHT':
                self.x += self.gameData.get("PLATFORM_SPEED")
                self.gameData.set("BALL_Y", self.x)
            if name == 'UNDOCK':
               self.updateDirection()
               self.onPlatform = False
        else:
            if name == 'UPDATE_SCREEN':
                self.move()
            if name == 'LOSE_BALL':
                self.initStartPosition()

    def updateDirection(self):
        if self.onPlatform:
            if 0 < self.gameData.get("BALL_X") < self.gameData.get("WIDTH") // 2 - self.gameData.get("BALL_WIDTH"):
                self.direction = "NW"
            else:
                self.direction = "NE"

    def move(self):
        self.checkBorder()
        if self.direction == "NE":
            self.x += self.gameData.get("BALL_SPEED")
            self.y -= self.gameData.get("BALL_SPEED")
        elif self.direction == "NW":
            self.x -= self.gameData.get("BALL_SPEED")
            self.y -= self.gameData.get("BALL_SPEED")
        elif self.direction == "SW":
            self.x -= self.gameData.get("BALL_SPEED")
            self.y += self.gameData.get("BALL_SPEED")
        elif self.direction == "SE":
            self.x += self.gameData.get("BALL_SPEED")
            self.y += self.gameData.get("BALL_SPEED")
        self.gameData.set("BALL_X", self.x)
        self.gameData.set("BALL_Y", self.y)


    def checkBorder(self):
        if self.x + self.gameData.get("BALL_WIDTH") > self.gameData.get("WIDTH"):
            if self.direction == "NE":
                self.direction = "NW"
            elif self.direction == "SE":
                self.direction = "SW"
        if self.y < 0:
            if self.direction == "NE":
                self.direction = "SE"
            elif self.direction == "NW":
                self.direction = "SW"
        if self.y > self.gameData.get("HEIGHT"):
            self.gameData.get("GAME_EVENT_BUS").publish_event(Event("LOSE_BALL", None))
        if self.x < 0:
            if self.direction == "NW":
                self.direction = "NE"
            elif self.direction == "SW":
                self.direction = "SE"
        if self.isCrossPlatform():
            if self.direction == "SE":
                self.direction = "NE"
            elif self.direction == "SW":
                self.direction = "NW"

    def isCrossPlatform(self):
        crossX = self.gameData.get("PLATFORM_X") < self.x < self.gameData.get("PLATFORM_X") + self.gameData.get("PLATFORM_WIDTH")
        crossY = self.gameData.get("PLATFORM_Y") < self.y + self.gameData.get("BALL_WIDTH") < self.gameData.get("PLATFORM_Y") + self.gameData.get("PLATFORM_HEIGHT")
        return crossX and crossY

    def initStartPosition(self):
        self.onPlatform = True
        self.x = self.gameData.get("PLATFORM_X") + self.gameData.get("PLATFORM_WIDTH") // 2 - self.gameData.get("BALL_WIDTH") // 2
        self.gameData.set("BALL_X", self.x)
        self.y = self.gameData.get("PLATFORM_Y") - self.gameData.get("PLATFORM_HEIGHT")
        self.gameData.set("BALL_Y", self.y)
