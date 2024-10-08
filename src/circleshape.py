import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: object):
        # sub-classes must override
        pass

    def update(self, dt: int):
        # sub-classes must override
        pass

    def collision_detection(self, game_object: object):
        """Determines if two in-game objects collide"""
        distance = self.position.distance_to(game_object.position)
        if self.radius + game_object.radius <= distance:
            return False
        return True
