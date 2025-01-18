from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(velocity)



    def draw(self, screen):
        pygame.draw.circle(screen, "cyan", self.position, self.radius, 2)

    def update(self, dt):
       self.position += self.velocity * dt

       if (
           self.position.x < 0 or self.position.x > SCREEN_WIDTH or
           self.position.y < 0 or self.position.y >SCREEN_HEIGHT
       ):
           self.kill()
