import pygame
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
    hitbox_speed = 1  # Minimalna wartość przesunięcia

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Sprawdzenie, czy hitbox dotyka krawedzi okna
        if hitbox.left <= 0 or hitbox.right >= 800 or hitbox.top <= 0 or hitbox.bottom >= 500:
            # Odbicie hitboxa w strone srodka 
            if hitbox.left <= 0:
                hitbox.x += hitbox_speed
            if hitbox.right >= 800:
                hitbox.x -= hitbox_speed
            if hitbox.top <= 0:
                hitbox.y += hitbox_speed
            if hitbox.bottom >= 500:
                hitbox.y -= hitbox_speed

        window.fill((255, 255, 255))  # Wypelnienie okna na bialo
        pygame.draw.rect(window, (0, 0, 0), hitbox)  # Rysowanie hitboxa na ekranie

        pygame.display.update()



