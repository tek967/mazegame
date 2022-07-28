import json, pygame, os
from .game_elements.black_patch import BlackPatch

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

class Map():
    def __init__(self, window: pygame.Surface) -> None:
        self.mapFiles = []

        for m in range(1):
            with open(relative_path(f"resources/maps/{m+1}.json")) as t:
                self.mapFiles.append(json.loads(t.read()))
        
        self.mapData = [{"spawn_location": {"x": 0,"y": 0},"elements" : {"black_patch" : []}} for _, _ in self.mapFiles]

        for i, _ in enumerate(self.mapFiles):
            self.mapData[i]["elements"]["black_patch"].append([BlackPatch(window, 
            map_data["elements"]["black_patch"]["x"], 
            map_data["elements"]["black_patch"]["y"],
            map_data["elements"]["black_patch"]["width"],
            map_data["elements"]["black_Patch"]["height"]
            ) for map_data in self.mapFiles[i] ])
            self.mapData[i]["spawn_location"] = self.mapData[i]["spawn_location"]

    def return_map_data_at_index(self, index: int) -> dict:
        return self.mapFiles[index]
    
    def return_map_classes_at_inde(self, index: int) -> dict:
        return self.mapData[index]