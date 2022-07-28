import pygame

from game.mapio import Map
from .game_elements.player import Player
from .utilclasses import *

class Window():
    def __init__(self, width: int, height: int):
        pygame.init()
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode([width, height])
        pygame.display.set_caption("The Maze Game")

        self.palette = get_palette() 

        # class objects
        self.map = Map(self.window)
        self.player = Player(self.map,self.window)
        # --
        self.is_window_alive = True
        while self.is_window_alive: 
            self.update()
            pygame.display.update()

    def draw(self):
        self.window.fill(self.palette["verylightgray"])
        self.player.draw()

    def update(self):
        self.clock.tick(self.fps) 
        self.player.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.is_window_alive = False
                break
            if event.type == pygame.KEYDOWN:
                self.player.controls(event)
            if event.type == pygame.KEYUP:
                self.player.controls_key_up(event)
        self.draw()
        
