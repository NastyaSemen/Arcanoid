import os
import sys
import pygame
from Drawer import *
from Sprites.Platform import Platform
from Event.EventBus import EventBus
from Event.Event import Event


size = width, height = 800, 600
eventBus = EventBus()


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
    eventBus.add_subscriber(platform)
    sprites.append(platform)
    return sprites


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode(size)
    back = pygame.transform.scale(load_image('level_one_back.jpg'), (width, height))
    screen.blit(back, (0, 0))

    sprites = get_sprites()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    eventBus.publish_event(Event('MOVE_LEFT', None))
                if event.key == pygame.K_RIGHT:
                    eventBus.publish_event(Event('MOVE_RIGHT', None))

            if event.type == pygame.KEYUP:
                pass

        draw(sprites, screen)

        pygame.display.flip()

        screen.blit(back, (0, 0))

    pygame.quit()
