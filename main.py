import os
import sys
import pygame
from Drawer import *
from Sprites.Platform import Platform


size = width, height = 800, 600


def load_image(name, colorkey=None):
    fullname = os.path.join('Data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def get_sprites():
    sprites = []
    platform = Platform(width // 2, 400)
    sprites.append(platform)
    return sprites


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode(size)
    back = pygame.transform.scale(load_image('level_one_back.jpg'), (width, height))
    screen.blit(back, (0, 0))

    sprites = get_sprites()

    sprites.image = load_image('Platform.png')
    sprites.rect = sprites.image.get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                sprites.rect.x -= 10

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                sprites.rect.x += 10
        draw(sprites, screen)

        pygame.display.flip()

    pygame.quit()

