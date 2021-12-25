from Sprites import Sprite


class Platform(Sprite.Sprite):

    def __init__(self, x, y):
        super().__init__(x, y, 'Платформа.png')
