import pasek_zdrowia_HPP.py
import pygame
import sys
from pygame.locals import *

pygame.init()


#przyklad uzycia klasy wrog
wrog = Wrog("Nazwa Wroga", (255, 0, 0), 100, 100, 50, 30)

# Wywołanie metody wyświetlającej informacje o wrogu
wrog.wyswietlanie_informacji_o_wrogu()






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



