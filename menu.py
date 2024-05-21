import pygame
import sys
def wypisz(tekst, font, kolor, surf, x, y):
    tekstobj = font.render(tekst, True, kolor)
    tekstrect = tekstobj.get_rect()
    tekstrect.topleft = (x, y)
    surf.blit(tekstobj, tekstrect)

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

def main_menu():
    while True:
        screen.fill(WHITE)
        wypisz('Menu glowne', font, BLACK, screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, BLACK, button_1)
        pygame.draw.rect(screen, BLACK, button_2)

        draw_text('Graj', small_font, WHITE, screen, 100, 110)
        draw_text('Wyjdz', small_font, WHITE, screen, 100, 210)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(144)
