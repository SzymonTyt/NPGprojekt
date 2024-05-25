import pygame
import sys
import random
import time
from pygame.locals import *

sys.path.append('C:\\Users\\adasf\\OneDrive\\Pulpit\\github\\NPGprojekt\\hitbox + pasekZdrowia')
import pasek_zdrowia_HPP

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

class Pocisk(Wrog):
    def __init__(self, wrog):
        super().__init__(wrog.nazwa, wrog.kolor, wrog.rect.x, wrog.rect.y, 10, 5)
        self.predkosc_x = 5

    def update(self, dt):
        self.rect.x += self.predkosc_x * dt

    def draw(self, surface):
        pygame.draw.rect(surface, self.kolor, self.rect)

def losowe_generowanie_zdarzen(wrogowie, ilosc_czasu):
    poczatek = time.time()
    pociski = []

    while (time.time() - poczatek) < ilosc_czasu:
        losowy_wrog = random.choice(wrogowie)
        instancja_pocisku = Pocisk(losowy_wrog)
        pociski.append(instancja_pocisku)
        time.sleep(random.uniform(0.1, 1.0))

    return pociski

pygame.init()

def hitbox_ustalony_przez_gracza(x, y, szerokosc, wysokosc):
    return pygame.Rect(x, y, szerokosc, wysokosc)

def main():
    szerokoscHb, wysokoscHb = map(int, input("Jaka wielkosc ma miec hitbox postaci (szerokosc wysokosc): ").split())
    window = pygame.display.set_mode((800, 500))
    pygame.display.set_caption('Magiczne przygody kamienia Artura')

    wrogowie = [
        Wrog("Wrog1", (255, 0, 0), 0, 0, 50, 50),
        Wrog("Wrog2", (255, 0, 0), 750, 0, 50, 50),
        Wrog("Wrog3", (255, 0, 0), 0, 450, 50, 50),
        Wrog("Wrog4", (255, 0, 0), 750, 450, 50, 50)
    ]

    hitbox = hitbox_ustalony_przez_gracza(0, 0, szerokoscHb, wysokoscHb)
    hitbox_speed = 5

    clock = pygame.time.Clock()

    pociski = losowe_generowanie_zdarzen(wrogowie, 10)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_a]:
            hitbox.x -= hitbox_speed
        if keys[K_d]:
            hitbox.x += hitbox_speed
        if keys[K_w]:
            hitbox.y -= hitbox_speed
        if keys[K_s]:
            hitbox.y += hitbox_speed

        if hitbox.left <= 0:
            hitbox.left = 0
        if hitbox.right >= 800:
            hitbox.right = 800
        if hitbox.top <= 0:
            hitbox.top = 0
        if hitbox.bottom >= 500:
            hitbox.bottom = 500

        window.fill("purple")
        pygame.draw.rect(window, "red", hitbox)

        for wrog in wrogowie:
            wrog.move_towards(hitbox)
            wrog.draw(window)

        dt = clock.tick(60) / 1000.0
        for pocisk in pociski:
            pocisk.update(dt)
            pocisk.draw(window)

        pygame.display.update()

if __name__ == "__main__":
    main()
