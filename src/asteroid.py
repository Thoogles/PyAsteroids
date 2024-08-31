import pygame


from circleshape import CircleShape
from constants import (
    ASTEROID_COLOR,
    ASTEROID_LINE_WIDTH,
)


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen: object):
        pygame.draw.circle(
            screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
