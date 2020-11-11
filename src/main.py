import pyxel

from space_shuttle import SPACE_SHUTTLE


FPS_CAP = 60
TITLE = "Challenger"
WINDOW_WIDTH = 64 * 4
WINDOW_HEIGHT = 64 * 3


def update():
    pass

def draw():
    SPACE_SHUTTLE.draw()
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
