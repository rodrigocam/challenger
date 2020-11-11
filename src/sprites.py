import pyxel

class Sprite:

    x, y = (20, 20)

    def __init__(self, page, start=(0,0), size=(0,0), bg_color=pyxel.COLOR_BLACK):
        self.page = page
        self.start = start
        self.size = size
        self.bg_color = bg_color


    def draw(self):
        pyxel.blt(20, 20, self.page, self.start[0], self.start[1], self.size[0], self.size[1], self.bg_color)
