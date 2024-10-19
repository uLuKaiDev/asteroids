import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()


    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0


    # Main game loop starts here"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")        # Fills the screen with black       
        
        for obj in updatable:
            obj.update(dt)          # Updates the rotation and speed
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print('Game Over!')
                sys.exit()


        for obj in drawable:        # Draws the items on the screen
            obj.draw(screen)
        
        pygame.display.flip()       # Updates the screen THIS HAS TO BE AT THE BOTTOM

        # Limit framerate to 60 (dt = delta time)
        dt = clock.tick(60) / 1000
        
        # Main game loop ends here


if __name__ == "__main__":
    main()