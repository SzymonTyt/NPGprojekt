import pygame
from Constans import *

class Projectile:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 5
        self.projectile_width = 10  # Dostosuj wymiary pocisku według potrzeb
        self.projectile_height = 10
        self.rect = pygame.Rect(x, y, self.projectile_width, self.projectile_height)

    def move(self):
        if self.direction == "1":
            self.x += self.speed
        elif self.direction == "2":
            self.x -= self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def colliderect(self, other_rect):
        return self.rect.colliderect(other_rect)