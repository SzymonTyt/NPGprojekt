
import pygame
import sys
from pygame.locals import *
sys.path.append('C:\\Users\\adasf\\OneDrive\\Pulpit\\github\\NPGprojekt\\hitbox + pasekZdrowia')
import pasek_zdrowia_HPP
pygame.init()


screen = pygame.display.set_mode((800, 600))

wrog = Wrog("Nazwa", (255, 0, 0), 100, 100, 50, 50)
pocisk = Pocisk("Pocisk", (0, 255, 0), 0, 0, 10, 10)

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pocisk.update(dt)

    screen.fill((255, 255, 255))  # Czyszczenie ekranu i rysowanie na nowo wroga i pocisku dla płynności
    pygame.draw.rect(screen, wrog.kolor_wroga, wrog.rect)
    pygame.draw.rect(screen, pocisk.kolor_wroga, pocisk.rect)
    pygame.display.flip()





def zasieg_obrazenia(x, y, hitbox): # współrzędne hitboxa
    wartosc_paska_obrazen = 100
    if abs(hitbox.x - x) >= 50 or abs(hitbox.x + hitbox.width - x) >= 50:
        wartosc_paska_obrazen -= 10
    return wartosc_paska_obrazen

def main():
    wartosc_paska_obrazen = 200 # przykładowa wartość
    if wartosc_paska_obrazen == 0:
        print("DEAD")
        # tutaj można dodać kod do wyświetlenia napisu z użyciem Pygame
        pygame.time.wait(1000)
        pygame.quit()

if __name__ == "__main__":
    main()



