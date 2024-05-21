# Sprawdzenie kolizji gracza z błędami
        collided_bugs = pygame.sprite.spritecollide(player, bugs, True)
        for bug in collided_bugs:
            # Tworzenie nowego kamienia w miejscu błędu
            stone = Stone(bug.rect.x, bug.rect.y)
            stones.add(stone)
            all_sprites.add(stone)
# Aktualizacja wszystkich sprite'ów
        all_sprites.update()
# Rysowanie wszystkiego na ekranie
        screen.fill(WHITE)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)