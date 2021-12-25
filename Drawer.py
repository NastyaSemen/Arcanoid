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


def draw(sprites, screen):

    all_sprites = pygame.sprite.Group()

    for spr in sprites:
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image(spr.get_image())
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = spr.get_cords()[0]
        sprite.rect.y = spr.get_cords()[1]
        all_sprites.add(sprite)

    all_sprites.draw(screen)
