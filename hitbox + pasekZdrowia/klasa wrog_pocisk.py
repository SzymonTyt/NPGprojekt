import pygame

class Wrog:
    def __init__(self, nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga):
        self.nazwa = nazwa_wroga
        self.kolor = kolor_wroga
        self.rect = pygame.Rect(wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga)
        self.wspolrzedna_x = wspolrzedna_x
        self.wspolrzedna_y = wspolrzedna_y

class Pocisk(Wrog):
    def __init__(self, nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga):
        super().__init__(nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga)
        self.predkosc_x = 5

    def update(self, dt):
        self.rect.x += self.predkosc_x * dt

# Przykładowe użycie:
pygame.init()

# Tworzenie obiektu Wrog
wrog = Wrog("Zły Obcy", (255, 0, 0), 100, 100, 50, 50)
print(f"Wrog: nazwa={wrog.nazwa}, kolor={wrog.kolor}, wspolrzedna_x={wrog.wspolrzedna_x}, wspolrzedna_y={wrog.wspolrzedna_y}")

# Tworzenie obiektu Pocisk, który dziedziczy po Wrog
pocisk = Pocisk("Pocisk Obcego", (0, 255, 0), wrog.wspolrzedna_x, wrog.wspolrzedna_y, 10, 5)
print(f"Pocisk: nazwa={pocisk.nazwa}, kolor={pocisk.kolor}, wspolrzedna_x={pocisk.wspolrzedna_x}, wspolrzedna_y={pocisk.wspolrzedna_y}")

# Aktualizacja pozycji pocisku
dt = 1  # Przykładowy delta time
pocisk.update(dt)
print(f"Nowa pozycja pocisku: rect.x={pocisk.rect.x}, rect.y={pocisk.rect.y}")

pygame.quit()
