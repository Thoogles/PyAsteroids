import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_COLOR,
    PLAYER_LINE_WIDTH,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    SHOT_RADIUS,
    SHOT_COLOR,
    SHOT_LINE_WIDTH,
)


class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_interval = 0

    def triangle(self):
        """Creates the triangle points for our ship model

        Output:
            - list containing the triangle points
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: object):
        """Draws the player ship on the screen"""
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), PLAYER_LINE_WIDTH)

    def rotate(self, dt: int):
        """Handles the vector rotation for the player ship"""
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self, dt: int):
        """Spawns bullet objects from player ship at set interval.
        The bullets will follow the ships at the moment trajectory"""
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shots_interval = PLAYER_SHOOT_COOLDOWN

    def update(self, dt: int):
        """Handles the player input, as well as shots interval"""
        keys = pygame.key.get_pressed()
        self.shots_interval -= dt

        # Ship controls
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shots_interval < 0:
                self.shoot(dt)

    def move(self, dt: int):
        """Sets the new position for the player model based on their speed"""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


class Shot(CircleShape):
    def __init__(self, x: int, y: int, radius: int = SHOT_RADIUS):
        super().__init__(x, y, radius)

    def draw(self, screen: object):
        """Handles bullet drawing on the screen"""
        pygame.draw.circle(
            screen, SHOT_COLOR, self.position, self.radius, SHOT_LINE_WIDTH
        )

    def update(self, dt: int):
        """Updates bullet position with each tick"""
        self.position += self.velocity * dt
