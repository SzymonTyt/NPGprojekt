
import pygame
import sys
from pygame.locals import *

pygame.init()

class Wrog:
    def __init__(self, nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga):
        self.nazwa = nazwa_wroga
        self.kolor_wroga = kolor_wroga
        self.rect = pygame.Rect(wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga)
        self.wspolrzedna_x = 0

    def wyswietlanie_informacji_o_wrogu(self):
        print(f"Nazwa wroga: {self.nazwa}")
        print(f"Kolor wroga: {self.kolor_wroga}")
        print(f"Współrzędna x: {self.rect.x}")
        print(f"Współrzędna y: {self.rect.y}")
        print(f"Szerokość wroga: {self.rect.width}")
        print(f"Wysokość wroga: {self.rect.height}")

import pygame

class Wrog:
    def __init__(self, nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga):
        self.nazwa = nazwa_wroga
        self.kolor_wroga = kolor_wroga
        self.rect = pygame.Rect(wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga)
        self.wspolrzedna_x = wspolrzedna_x  # Poprawka: ustawiamy współrzędną x na początkową wartość

class Pocisk(Wrog):
    def __init__(self, nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga):
        super().__init__(nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga)
        self.predkosc_x = 5

    def update(self, dt):
        self.rect.x += self.predkosc_x * dt



class Postac:
    def __init__(self, nazwa_postaci, kolor_postaci, wspolrzedna_x, wspolrzedna_y, szerokosc_postaci, wysokosc_postaci):
        self.nazwa = nazwa_postaci
        self.kolor_postaci = kolor_postaci
        self.rect = pygame.Rect(wspolrzedna_x, wspolrzedna_y, szerokosc_postaci, wysokosc_postaci)
        self.wspolrzedna_x = 0

    def wyswietlanie_informacji_o_wrogu(self):
        print(f"Nazwa postaci: {self.nazwa}")
        print(f"Kolor postaci: {self.kolor_wroga}")

