import pygame
from circleshape import CircleShape
from constants import *
import random


class PowerUp(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        # Use just one parent class initialization
        super().__init__(x, y, radius)
        # Add to containers after initialization
        self.add(self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, RANDOM_COLOR, self.position, self.radius, 1)
   
    def update(self, dt):
        self.position += (self.velocity * dt)