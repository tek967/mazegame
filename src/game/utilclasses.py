import json, pygame, os

def relative_path(relpath: str) -> str:
    return os.path.join(os.path.dirname(__file__), '../../', relpath)

def get_palette() -> dict:
    with open(relative_path("resources/palette.json"), 'r') as palette: return json.loads(palette.read())

class Rectangle():
    def __init__(self, window: pygame.Surface, x: int, y: int, width: int, height: int, color: list[int]):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.window = window
        self.color = color

    def draw(self):
        pygame.draw.rect(self.window, self.color, [self.x, self.y, self.width, self.height], 0)

def collision_rects(rect1: Rectangle, rect2: Rectangle):
    if (rect1.x < (rect2.x + rect2.width) and (rect1.x + rect1.width) > rect2.x and rect1.y < (rect2.y + rect2.height) and (rect1.height + rect1.y) > rect2.y):
        return True
    else:
        return False   

