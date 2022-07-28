import pygame
from game.utilclasses import *
 
class Player:
    def __init__(self, mp: dict, window: pygame.Surface): #mp is map
        self.palette = get_palette()        
        self.velocity = pygame.Vector2(0,0)

        self.current_level = 1
        
        self.deathPosition = pygame.Vector2(mp["spawn_location"]["x"],mp["spawn_location"]["y"])
        self.position = pygame.Vector2(20,20)

        self.colors = (self.palette["lightblue"], self.palette["blue"]) 
        self.inner_rect = Rectangle(window, self.position.x+5, self.position.y+5, 30, 30, self.colors[0])
        self.outer_rect = Rectangle(window, self.position.x, self.position.y, 40, 40, self.colors[0])

    def reset_to_deathpos(self):
        self.position = self.deathPosition

    def draw(self):
        self.outer_rect.draw()
        self.inner_rect.draw()

    def controls(self, event):
        if event.key == pygame.K_UP:
            self.velocity.y = -7
        elif event.key == pygame.K_DOWN:
            self.velocity.y = 7
        elif event.key == pygame.K_LEFT:
            self.velocity.x = -7
        elif event.key == pygame.K_RIGHT:
            self.velocity.x = 7

    def controls_key_up(self, event):
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            self.velocity.y = 0
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            self.velocity.x = 0

    def update(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.outer_rect.x, self.outer_rect.y = self.position.x, self.position.y
        self.inner_rect.x, self.inner_rect.y = self.position.x+5, self.position.y+5