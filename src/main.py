import pyxel
import pymunk

from constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS_CAP, TITLE
import space_shuttle

SPACE = pymunk.Space()
SPACE.gravity = 0, 10
SPACE.add(space_shuttle.SPACE_SHUTTLE.body, space_shuttle.SPACE_SHUTTLE.shape)

def update():
    SPACE.step(0.02)

def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    space_shuttle.SPACE_SHUTTLE.draw()
    # map_x, map_y = (0, 0)
    # map_page = 0
    # tile_x, tile_y = (0, 8)
    # tile_size = 8

    # map
    # pyxel.bltm(map_x, map_y, map_page, tile_x, tile_y, tile_size*4, tile_size*3, pyxel.COLOR_CYAN)

    # x, y = (20, 20)
    # page = 0
    # x_page, y_page = (24, 0)
    # w,h = (15, 39)
    # sprite
    # pyxel.blt(x, y, page, x_page, y_page, w, h, pyxel.COLOR_PINK)


pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, fps=FPS_CAP, caption=TITLE)
pyxel.load("../res/resources.pyxres")
pyxel.run(update, draw)
