import pygame
pygame.init()

height = 720
width = 1280

screen = pygame.display.set_mode((width, height))

stone_x_size = 60
stone_y_size = 40

stone = pygame.image.load('kamien.png')
stone = pygame.transform.scale(stone, (stone_x_size, stone_y_size))

def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
if self.rect.left <= 0 or self.rect.right >= 800:
            self.velocity[0] = -self.velocity[0]
if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.velocity[1] = -self.velocity[1]