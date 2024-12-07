import pygame
from player import Player
from constants import *
from circleshape import CircleShape
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys
from shots import Shot
from powerup import PowerUp


def main():
    pygame.init()  # Initialize pygame modules

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    PowerUp.containers = (powerups, updatable,drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, [updatable, drawable])
    asteroidfield = AsteroidField()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Properly close the loop
        
        screen.fill((0, 0, 0))  # Clear the screen with black
        
        
         drawable.draw(screen)
        
        dt = clock.tick(60) / 1000  # Ensure we get the delta time in seconds
        updatable.update(dt)  # Update all "updatable" objects
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
        for powerup in powerups:
            if player.collides_with(powerup):
                print("Upgrade!")
                upgrade(player)
        
        pygame.display.flip()  # Update the display
    
    pygame.quit()  # Shutdown all pygame modules 
        
if __name__ == "__main__":
    main()



