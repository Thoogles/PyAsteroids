import pygame
import random
from asteroid import Asteroid
from constants import *  # noqa: F403


class AsteroidField(pygame.sprite.Sprite):
    # determines the edges of the game window
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),  # noqa: F405
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS,
                y * SCREEN_HEIGHT,  # noqa: F405
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),  # noqa: F405
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH,
                SCREEN_HEIGHT + ASTEROID_MAX_RADIUS,  # noqa: F405
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius: int, position: tuple, velocity: int):
        """Spawns asteroid objects and sets their velocity"""
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt: int):
        """Determines if asteroid can spawn, and then sets random
        spawn point on the edge of the screen for it"""
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:  # noqa: F405
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)  # noqa: F405
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)  # noqa: F405
