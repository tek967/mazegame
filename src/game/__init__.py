import mandaw
from util.utilclasses import *

class Window():
    def __init__(self, width: int, height: int):
        self.palette = get_palette()
        self.window = mandaw.Mandaw(title = "The Maze Game", width = width, height = height, bg_color = self.palette["verylightgray"])
    def draw():
        pass

    def update(dt):
        pass
