import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop starts here"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill('black')
        pygame.display.flip()

        # Limit framerate to 60 (dt = delta time)
        dt = clock.tick(60) / 1000
        
        # Main game loop ends here


if __name__ == "__main__":
    main()