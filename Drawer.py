import pygame


def draw(sprites, screen):

    all_sprites = pygame.sprite.Group()

    for spr in sprites:
        sprite = pygame.sprite.Sprite()
        sprite.image = spr.get_image()
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = spr.get_cords()[0]
        sprite.rect.y = spr.get_cords()[1]
        all_sprites.add(sprite)

    all_sprites.draw(screen)
