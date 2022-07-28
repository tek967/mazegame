import pygame, json 
from .utilclasses import relative_path
from .game_elements.black_patch import BlackPatch
class Map():
    def __init__(self, window: pygame.Surface) -> None:
        self.mapFiles = []

        for m in range(1):
            with open(relative_path(f"resources/maps/{m+1}.json")) as t:
                self.mapFiles.append(json.loads(t.read()))
        
        self.mapData = [{"spawn_location": {"x": 0,"y": 0},"elements" : {"black_patch" : []}} for _, _ in self.mapFiles]
        
        for i, _ in enumerate(self.mapFiles): 
            self.mapData[i]["elements"]["black_patch"].append(
                BlackPatch(
                    window, 
                    self.mapFiles[i]['elements']['black_patch'][i]['x'], 
                    self.mapFiles[i]["elements"]["black_patch"][i]["y"],
                    self.mapFiles[i]["elements"]["black_patch"][i]["width"],
                    self.mapFiles[i]["elements"]["black_patch"][i]["height"]
                )
            )
            self.mapData[i]["spawn_location"] = self.mapData[i]["spawn_location"]

    def return_map_json_at_index(self, index: int) -> dict:
        return self.mapFiles[index]
    
    def return_map_classes_at_index(self, index: int) -> dict:
        return self.mapData[index]
        