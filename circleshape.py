import pygame
from constants import WHITE

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Just call the parent (Sprite) init without any arguments
        super().__init__()  
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        # Initialize the 'rect' attribute with an appropriate size and position
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2) 

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
        

    def update(self, dt):
        # sub-classes must override
        pass

    def update_rect(self):
        # Keep the rect position in sync with the sprite's position
        self.rect.center = (self.position.x, self.position.y)

    def collides_with(self, other_shape):
        distance = self.position.distance_to(other_shape.position) 
        if distance <= (self.radius + other_shape.radius):
            return True
        else:
            return False
        