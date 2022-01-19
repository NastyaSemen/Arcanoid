import os
import sys
from Drawer import *
from Sprites.Platform import Platform
from Sprites.Ball import Ball
from Sprites.Score import Score
from Sprites.StartEnd import StartEnd
from Event.EventBus import EventBus
from Event.Event import Event
from SoundProcessor import SoundProcessor
from GameLogic import GameLogic
from GameData import GameData


pygame.init()
gameData = GameData()
size = width, height = 800, 600
gameData.set("WIDTH", width)
gameData.set("HEIGHT", height)
gameData.set("MOVE_EVENT_BUS", EventBus())
gameData.set("GAME_EVENT_BUS", EventBus())
gameData.set("SOUND_EVENT_BUS", EventBus())
gameData.set("GAME_OVER", False)
sprites = {}
sprites["PLARFORM"] = Platform(gameData)
sprites["BALL"] = Ball(gameData)
sprites["SCORE"] = Score(pygame, gameData)
sprites["START_END_GAME"] = StartEnd(pygame, gameData)
gameData.set("SPRITES", sprites)


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
    return gameData.get("SPRITES").values()

if __name__ == '__main__':
    SoundProcessor(pygame, gameData)
    GameLogic(gameData)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Arcanoid')
    back = pygame.transform.scale(load_image('level_one_back.jpg'), (width, height))
    screen.blit(back, (0, 0))
    clock = pygame.time.Clock()

    running = True
    key_pressed = set()
    gameData.get("SOUND_EVENT_BUS").publish_event(Event("START_GAME", None))
    gameData.get("GAME_EVENT_BUS").publish_event(Event("START_GAME", None))
    while running:
        game_over = gameData.get("GAME_OVER")
        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    gameData.set("IN_GAME", True)
                    if event.key == pygame.K_LEFT:
                        key_pressed.add("MOVE_LEFT")
                    if event.key == pygame.K_RIGHT:
                        key_pressed.add("MOVE_RIGHT")
                    if event.key == pygame.K_SPACE:
                        key_pressed.add("UNDOCK")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        key_pressed.remove("MOVE_LEFT")
                    if event.key == pygame.K_RIGHT:
                        key_pressed.remove("MOVE_RIGHT")
                    if event.key == pygame.K_SPACE:
                        key_pressed.remove("UNDOCK")
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        gameData.get("GAME_EVENT_BUS").publish_event(Event("START_GAME", None))
                        gameData.set("GAME_OVER", False)
                        gameData.set("IN_GAME", True)
        for key in key_pressed:
            gameData.get("MOVE_EVENT_BUS").publish_event(Event(key, None))
        gameData.get("GAME_EVENT_BUS").publish_event(Event("UPDATE_SCREEN", None))
        draw(get_sprites(), screen)
        pygame.display.flip()
        screen.blit(back, (0, 0))
        clock.tick(50)
    pygame.quit()
