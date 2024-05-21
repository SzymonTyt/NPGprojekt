import pygame

class Animacja(pygame.sprite.Sprite):
    def __init__(self, klatki, czas_trwania_klatki_ms):
	super().__init__()
        self.klatki = klatki
	self.indeks_biezacej_klatki = 0
	self.czas_trwania_klatki_ms = czas_trwania_klatki_ms
	self.ostatniczas_zmiany_klatki_ms = 0
	self.aktualny_obraz = self.klatki[self.indeks_biezacje_klatki]