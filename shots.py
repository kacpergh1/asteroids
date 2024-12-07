import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    containers = None

    def __init__(self, x, y, groups):
        super().__init__(x, y, SHOT_RADIUS)
        self.add(self.containers)


    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
   
    def update(self, dt):
        # Update the shot's position based on its velocity
        self.position += self.velocity * dt
        # Update the rect to match this new position
        self.update_rect()