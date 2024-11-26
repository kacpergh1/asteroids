import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    containers = None
    
    def __init__(self, x, y, radius):
        # Use just one parent class initialization
        super().__init__(x, y, radius)
        # Add to containers after initialization
        self.add(self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
   
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50) 
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_velocity1 *= 1.2
        new_velocity2 *= 1.2
    
        # Create first asteroid using x, y coordinates
        new_asteroid1 = Asteroid(
            x=self.position.x,  # Extract x coordinate
            y=self.position.y,  # Extract y coordinate
            radius=new_radius
        )
        new_asteroid1.velocity = new_velocity1  # Set velocity after creation

        # Now create second asteroid...

        new_asteroid2 = Asteroid(
            x=self.position.x,  # Extract x coordinate
            y=self.position.y,  # Extract y coordinate
            radius=new_radius
        )
        new_asteroid2.velocity = new_velocity2  # Set velocity after creation

        

        