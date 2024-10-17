import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0


    # Main game loop starts here"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")        # Fills the screen black
        player.draw(screen)         # Draws the player on top of it
        
        pygame.display.flip()       # Updates the screen THIS HAS TO BE AT THE BOTTOM

        # Limit framerate to 60 (dt = delta time)
        dt = clock.tick(60) / 1000
        
        # Main game loop ends here


if __name__ == "__main__":
    main()