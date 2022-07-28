from .player import Player
import pygame
from game.utilclasses import Rectangle, collision_rects

class BlackPatch():
    def __init__(self, window: pygame.Surface, x: int, y: int, width: int, height: int):
        self.x, self.y, self.width, self.height= x, y, width, height
        self.rect = Rectangle(window, self.x, self.y, self.width, self.height, [250,250,250])

    def draw(self):
        self.rect.draw()
    
    def playerCollision(self, player: Player):
        if collision_rects(self.rect, player):
            player.reset_to_deathpos()
    
    def update(self):
        pass