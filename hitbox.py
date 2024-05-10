import pygame
import sys
from pygame.locals import *

pygame.init()

def hitbox_ustalony_przez_gracza(x, y, szerokosc, wysokosc):
    hitbox = pygame.Rect(x, y, szerokosc, wysokosc)
    return hitbox

def main():
    window = pygame.display.set_mode((800, 500))  # Ustawienie rozmiaru okna
    pygame.display.set_caption('Magiczne przygody kamienia Artura')  # Etykieta okna

    szerokoscHb, wysokoscHb = map(int, input("Jaka wielkosc ma miec hitbox postaci (szerokosc wysokosc): ").split())

    hitbox = hitbox_ustalony_przez_gracza(0, 0, szerokoscHb, wysokoscHb)
    hitbox_speed = 5  # Szybkosc poruszania hitboxa

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Sprawdzenie nacisnieetych przyciskow
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            hitbox.x -= hitbox_speed
        if keys[K_d]:
            hitbox.x += hitbox_speed
        if keys[K_w]:
            hitbox.y -= hitbox_speed
        if keys[K_s]:
            hitbox.y += hitbox_speed

        # Sprawdzenie, czy hitbox dotyka krawedzi okna
        if hitbox.left <= 0:
            hitbox.left = 0
        if hitbox.right >= 800:
            hitbox.right = 800
        if hitbox.top <= 0:
            hitbox.top = 0
        if hitbox.bottom >= 500:
            hitbox.bottom = 500

        window.fill((255, 255, 255))  # Wypelnienie okna na bialo
        pygame.draw.rect(window, (0, 0, 0), hitbox)  # Rysowanie hitboxa na ekranie

        pygame.display.update()

if __name__ == "__main__":
    main()