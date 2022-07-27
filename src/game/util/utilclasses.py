import json

class Vector2():
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def get_items(self) -> list[float]:
        return [self.x, self.y]

def get_palette() -> dict:
    with open('./palette.json', 'r') as palette: return json.loads(palette.read)