import pygame
from circleshape import CircleShape
from constants import *
from shots import Shot

class Player(CircleShape):
    def __init__(self, x, y, groups):
        # Call parent class initializer first
        super().__init__(x, y, PLAYER_RADIUS)  # Using super() is cleaner
    
        # Then add to groups
        for group in groups:
            group.add(self)
    
        # Rest of your initialization code...
        self.shooting_timer = 0
        self.rotation = 0
        self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self._update_image()

    def triangle(self):
        # Use local coordinates relative to the surface center
        center = pygame.Vector2(self.image.get_width() / 2, self.image.get_height() / 2)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    
        # Calculate points relative to surface center
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]
    
    def _update_image(self):
        """Update the image surface based on current attributes."""
        # Clear and then draw new shape
        self.image.fill((0, 0, 0, 0))  # Clear with transparency
    
        # For debugging, let's draw a very visible triangle
        points = self.triangle()
        pygame.draw.polygon(self.image, WHITE, points)
    
        # Let's also draw a rectangle outline so we can see the surface bounds
        pygame.draw.rect(self.image, (255, 0, 0), self.image.get_rect(), 1)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)


    

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.shooting_timer > 0:
            self.shooting_timer -= dt


        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self._update_image()
        self.rect.center = self.position


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):

        if self.shooting_timer > 0:
            return
        
        # Extract x and y coordinates from your player's position
        shot_x = self.position.x
        shot_y = self.position.y

        # Create the Shot object using x, y, and group arguments
        new_shot = Shot(shot_x, shot_y, Shot.containers)

        # Set the velocity of the shot similarly to the previous method logic
        direction = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot.velocity = direction

       
        self.shooting_timer = PLAYER_SHOOT_COOLDOWN
        
        def upgrade(self,):
        


        


        
       