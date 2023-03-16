import pygame
import sys
from pytmx.util_pygame import load_pygame

pygame.init()
screen = pygame.display.set_mode((1280, 1280))
tmxdata = load_pygame('dia.tmx')
sprite_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

# for layer in tmxdata.visible_layers:
#     print(layer)


# Get tiles
layer = tmxdata.get_layer_by_name('walls')
for x, y, surf in layer.tiles():
    Tile(pos=(x *64, y*64), surf=surf, groups=sprite_group)
    print(x, y, surf)

print(layer.data)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    sprite_group.draw(screen)
    pygame.display.update()
