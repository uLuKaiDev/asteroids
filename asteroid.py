import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        # The smaller the asteroid, the higher the points
        if self.radius <= 20.0:
            self.value = 3
        elif 20.0 < self.radius <= 40.0:
            self.value = 2
        else:
            self.value = 1
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20.0, 50.0)
        asteroid_1_velocity = self.velocity.rotate(random_angle)
        asteroid_2_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = asteroid_1_velocity * 1.2
        asteroid_2.velocity = asteroid_2_velocity * 1.2

        

