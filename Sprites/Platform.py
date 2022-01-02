from Sprites import Sprite


class Platform(Sprite.Sprite):

    def __init__(self, x, y):
        super().__init__(x, y, 'Platform.png')

    def on_event(self, event):
        name = event.get_name()
        if name == 'MOVE_LEFT':
            self.x -= 10
        elif name == 'MOVE_RIGHT':
            self.x += 10
