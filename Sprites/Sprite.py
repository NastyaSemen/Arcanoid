class Sprite:

    x, y = 0, 0
    image_path = ''

    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image_path = image_path

    def get_cords(self):
        return self.x, self.y

    def get_image(self):
        return self.image_path
