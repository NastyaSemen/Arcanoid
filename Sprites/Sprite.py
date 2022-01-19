import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('Data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Sprite:

    x, y = 0, 0
    image = None

    def __init__(self, x, y, image_path):
        self.set_coords(x, y)
        self.image = load_image(image_path)

    def get_cords(self):
        return self.x, self.y

    def get_image(self):
        return self.image

    def on_event(self, event):
        pass

    def set_coords(self, x, y):
        self.x = x
        self.y = y