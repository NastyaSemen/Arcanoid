import os
import sys
from Drawer import *
from Sprites.Platform import Platform
from Sprites.Ball import Ball
from Event.EventBus import EventBus
from Event.Event import Event
from GameData import GameData


gameData = GameData()
size = width, height = 800, 600
gameData.set("WIDTH", width)
gameData.set("HEIGHT", height)
gameData.set("MOVE_EVENT_BUS", EventBus())
gameData.set("GAME_EVENT_BUS", EventBus())


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
    sprites.append(Platform(gameData))
    sprites.append(Ball(gameData))
    return sprites


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode(size)
    back = pygame.transform.scale(load_image('level_one_back.jpg'), (width, height))
    screen.blit(back, (0, 0))
    clock = pygame.time.Clock()

    sprites = get_sprites()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gameData.get("MOVE_EVENT_BUS").publish_event(Event("MOVE_LEFT", None))
                if event.key == pygame.K_RIGHT:
                    gameData.get("MOVE_EVENT_BUS").publish_event(Event("MOVE_RIGHT", None))
                if event.key == pygame.K_SPACE:
                    gameData.get("MOVE_EVENT_BUS").publish_event(Event("UNDOCK", None))

            if event.type == pygame.KEYUP:
                pass
        gameData.get("GAME_EVENT_BUS").publish_event(Event("UPDATE_SCREEN", None))
        draw(sprites, screen)
        pygame.display.flip()
        screen.blit(back, (0, 0))
        clock.tick(50)
    pygame.quit()
