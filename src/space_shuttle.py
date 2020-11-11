import pyxel
from sprites import Sprite

class SpaceShuttle:

    def __init__(self, sprites):
        self.sprites = sprites
        self.current_sprite = 0


    def update(self):
        self.current_sprite = 0


    def draw(self):
        self.sprite.draw()

    @property
    def sprite(self):
        return self.sprites[self.current_sprite]



SPRITES = [
    Sprite(0, start=(24, 0), size=(15, 39), bg_color=pyxel.COLOR_PINK),
]


SPACE_SHUTTLE = SpaceShuttle(SPRITES)
