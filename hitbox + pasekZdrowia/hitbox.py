import pygame
import sys
import os
sys.path.append('C:\\Users\\adasf\\OneDrive\\Pulpit\\github\\NPGprojekt\\hitbox + pasekZdrowia')
import pasek_zdrowia_HPP
from pygame.locals import *

class Wrog:
    def __init__(self, nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga):
        self.nazwa = nazwa_wroga
        self.kolor = kolor_wroga
        self.rect = pygame.Rect(wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga)

    def draw(self, surface):
        pygame.draw.rect(surface, self.kolor, self.rect)

    def move_towards(self, target_rect):
        if self.rect.x < target_rect.x:
            self.rect.x += 1
        elif self.rect.x > target_rect.x:
            self.rect.x -= 1
        if self.rect.y < target_rect.y:
            self.rect.y += 1
        elif self.rect.y > target_rect.y:
            self.rect.y -= 1


pygame.init()

def hitbox_ustalony_przez_gracza(x, y, szerokosc, wysokosc):
    hitbox = pygame.Rect(x, y, szerokosc, wysokosc)
    return hitbox

def main():

    szerokoscHb, wysokoscHb = map(int, input("Jaka wielkosc ma miec hitbox postaci (szerokosc wysokosc): ").split())
    window = pygame.display.set_mode((800, 500))  # Ustawienie rozmiaru okna
    pygame.display.set_caption('Magiczne przygody kamienia Artura')  # Etykieta okna

    wrogowie = [
    Wrog("Wrog1", (255, 0, 0), 0, 0, 50, 50),  # Lewy górny róg
    Wrog("Wrog2", (255, 0, 0), 750, 0, 50, 50),  # Prawy górny róg
    Wrog("Wrog3", (255, 0, 0), 0, 450, 50, 50),  # Lewy dolny róg
    Wrog("Wrog4", (255, 0, 0), 750, 450, 50, 50)  # Prawy dolny róg
]


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
       
        for wrog in wrogowie:
            
            wrog.draw(window)


        pygame.display.update()

if __name__ == "__main__":
    main()
