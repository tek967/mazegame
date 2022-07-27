import pygame
import json, os

"UTILITY CLASSES"

def relative_path(relpath: str) -> str:
    return os.path.join(os.path.dirname(__file__), '../../', relpath)

class Vector2Int():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_items(self) -> list[int]:
        return [self.x, self.y]

class Vector2():
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def get_items(self) -> list[float]:
        return [self.x, self.y]

def get_palette() -> dict:
    with open(relative_path("resources/palette.json"), 'r') as palette: return json.loads(palette.read())

"END UTILITY CLASSES"

class Window():
    def __init__(self, width: int, height: int):
        pygame.init()

        self.window = pygame.display.set_mode([width, height])
        pygame.display.set_caption("The Maze Game")

        self.palette = get_palette()

        self.is_window_alive = True
        while self.is_window_alive: self.update(); pygame.display.update()

    def draw(self):
        self.window.fill(self.palette["verylightgray"])

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_window_alive = False
                break
        self.draw()
        
