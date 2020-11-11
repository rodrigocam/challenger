import pyxel
import pymunk

import constants
from sprites import Sprite

class SpaceShuttle:

    def __init__(self, position, sprites):
        self.sprites = sprites
        self.current_sprite = 0

        #pymunk
        self.body = pymunk.Body(1, 1666)
        self.shape = pymunk.Poly.create_box(self.body)
        self.body.position = position


    def update(self):
        self.current_sprite = 0


    def draw(self):
        self.sprite.draw(self.body.position)

    @property
    def sprite(self):
        return self.sprites[self.current_sprite]



SPRITES = [
    Sprite(0, start=(24, 0), size=(15, 39), bg_color=pyxel.COLOR_PINK),
]

CENTER = ((constants.WINDOW_WIDTH / 2) - 15, constants.WINDOW_HEIGHT - 40)

SPACE_SHUTTLE = SpaceShuttle(CENTER, SPRITES)
