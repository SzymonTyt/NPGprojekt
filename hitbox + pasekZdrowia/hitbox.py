import pygame
import sys
from pygame.locals import *

pygame.init()

def hitbox_ustalony_przez_gracza(x, y, szerokosc, wysokosc):
    hitbox = pygame.Rect(x, y, szerokosc, wysokosc)
    return hitbox

def main():

    szerokoscHb, wysokoscHb = map(int, input("Jaka wielkosc ma miec hitbox postaci (szerokosc wysokosc): ").split())
    window = pygame.display.set_mode((800, 500))  # Ustawienie rozmiaru okna
    pygame.display.set_caption('Magiczne przygody kamienia Artura')  # Etykieta okna

    hitbox = hitbox_ustalony_przez_gracza(0, 0, szerokoscHb, wysokoscHb)
    hitbox_speed = 1  # Szybkosc poruszania hitboxa

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Sprawdzenie nacisnieetych przyciskow
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            hitbox.x -= hitbox_speed
            pygame.time.wait(5)
        if keys[K_d]:
            hitbox.x += hitbox_speed
            pygame.time.wait(5)
        if keys[K_w]:
            hitbox.y -= hitbox_speed
            pygame.time.wait(5)
        if keys[K_s]:
            hitbox.y += hitbox_speed
            pygame.time.wait(5)

        # Sprawdzenie, czy hitbox dotyka krawedzi okna
        if hitbox.left <= 0:
            hitbox.left = 0
        if hitbox.right >= 800:
            hitbox.right = 800
        if hitbox.top <= 0:
            hitbox.top = 0
        if hitbox.bottom >= 500:
            hitbox.bottom = 500

        window.fill("purple")

        pygame.draw.rect(window, "red", hitbox)  # Rysowanie hitboxa na ekranie

        pygame.display.update()

if __name__ == "__main__":
    main()
