import pygame
class Coin:
    def __init__(self, x, y):
        self.image = pygame.image.load('coin.png')  # Ścieżka do obrazu monety
        self.rect = self.image.get_rect(center=(x, y))
        self.collected = False
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)
