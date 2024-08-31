import pygame
import random


from circleshape import CircleShape
from constants import (
    ASTEROID_COLOR,
    ASTEROID_LINE_WIDTH,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPLIT_VELOCITY_MULTIPLIER,
)


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen: object):
        """Draws the asteroid object on the screen"""
        pygame.draw.circle(
            screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_LINE_WIDTH
        )

    def update(self, dt: int):
        """Updates asteroid position during game loop"""
        self.position += self.velocity * dt

    def split(self):
        """Handles asteroid object destruction and spawning of smaller asteroids when player shoots one down."""
        # Asteroid getting should should always disappear
        self.kill()
        # If we have the smallest asteroid, it is simply destroyed
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # However if it was bigger, we will spawn new ones!
        random_angle = random.uniform(20, 50)
        asteroid_vector_1 = self.velocity.rotate(random_angle)
        asteroid_vector_2 = self.velocity.rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, radius)
        asteroid_one.velocity = asteroid_vector_1 * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        asteroid_two = Asteroid(self.position.x, self.position.y, radius)
        asteroid_two.velocity = asteroid_vector_2 * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
