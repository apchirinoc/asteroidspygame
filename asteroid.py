import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        new_velocity = random.uniform(20, 50)
        for velocity in [new_velocity, -new_velocity]:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(*self.position, new_radius)
            new_asteroid.velocity = self.velocity.rotate(velocity) * 1.2
