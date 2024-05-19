# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()

height = 720
width = 1280
screen = pygame.display.set_mode((width, height))

# informacje o mieczu
sword_x_size = 70
sword_y_size = 70

sword = pygame.image.load("miecz.jpg")
sword = pygame.transform.scale(sword, (sword_x_size, sword_y_size))

# animacja miecza
sword_sprite_1 = []
for i in range(5):
    sword_sprite_1.append(pygame.transform.rotate(sword, -10 * i))

sword_sprite_2 = []
for i in range(2):
    sword_sprite_2.append(pygame.transform.rotate(sword, -25 * (1 - i)))

sword_sprite = sword_sprite_1 + [pygame.transform.rotate(sword, -50)] + sword_sprite_2

# informacje o kamieniu
stone_x_size = 81
stone_y_size = 54

stone = pygame.image.load('kamien.png')
stone = pygame.transform.scale(stone, (stone_x_size, stone_y_size))

# informacje o chrząszczu
bug_x_size = 75
bug_y_size = 50

bug = pygame.image.load('chrzaszcz.png')
bug = pygame.transform.scale(bug, (bug_x_size, bug_y_size))

# losowa początkowa pozycja chrząszcza
bug_x_rng = random.randint(60, 900)
bug_y_rng = random.randint(40, 540)

# sprawienie aby chrząszcz nie pojawił się w miejscu początkowego umiejscowienia gracza
if bug_x_rng <= 480:
    bug_x_rand = bug_x_rng
else:
    bug_x_rand = bug_x_rng + 320

if bug_y_rng <= 290:
    bug_y_rand = bug_y_rng
else:
    bug_y_rand = bug_y_rng + 180

# pozycja gracza
player_pos = pygame.Vector2((screen.get_width() / 2) - stone_x_size / 2, (screen.get_height() / 2) - stone_y_size / 2)

# pozycja chrząszcza
bug_pos = pygame.Vector2(bug_x_rand, bug_y_rand)

# zegar
clock = pygame.time.Clock()
dt = 0

# iterator przechodzący po kontenerze przechowującym kolejne pozycje miecza - umożliwia zajście animacji
iter = 0

# funkcje logiczne
program_running = True
hitting = False

# funkcje logiczne - możliwość poruszania
movement_left = True
movement_up = True
movement_right = True
movement_down = True

# funkcja logiczna - sprawdzenie czy następuje atak mieczem
one_hit_stone = False
one_hit_bug = False

# punkty zdrowia
stone_hp = 100
bug_hp = 100

while program_running:
    clock.tick(60)

    # wyłączanie programu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False
            pygame.quit()
            quit()

        # ustawienie funkcji logicznych odpowiedzialnych za atak mieczem na True pod wpływem wciśniętej spacji
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hitting = True
                one_hit_stone = True

    # wciśnięcie klawisza
    key_pressed = pygame.key.get_pressed()

    # prostokąty ustalające hitboxy danego obiektu (pisane ręcznie zamiast wykorzystania metody get_rect())
    rect_sword = pygame.Rect(player_pos.x + stone_x_size, player_pos.y - sword_y_size + (4 * stone_y_size / 5),
                             1.1 * sword_x_size, 1.1 * sword_y_size)
    rect_stone = pygame.Rect(player_pos.x, player_pos.y + 0.1 * stone_y_size, 1.1 * stone_x_size, stone_y_size)
    rect_bug = pygame.Rect(bug_pos.x + 0.1 * bug_x_size, bug_pos.y + 0.2 * bug_y_size, 0.8*bug_x_size, 0.8*bug_y_size)

    # zablokowanie ruchu, gdy bohater znajdzie się na brzegu ekranu
    if player_pos.x <= 0:
        movement_left = False
    if player_pos.x >= width - stone_x_size:
        movement_right = False
    if player_pos.y <= 0:
        movement_up = False
    if player_pos.y >= height - stone_y_size:
        movement_down = False
    if player_pos.x > 0 and player_pos.x < width - stone_x_size:
        movement_right = True
        movement_left = True
    if player_pos.y > 0 and player_pos.y < height - stone_y_size:
        movement_up = True
        movement_down = True

    # ruch postaci (strzałkami lub WASD)
    if (key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]) and movement_up:
        player_pos.y -= 400 * dt
    if (key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]) and movement_down:
        player_pos.y += 400 * dt
    if (key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]) and movement_left:
        player_pos.x -= 400 * dt
    if (key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]) and movement_right:
        player_pos.x += 400 * dt

    #ruch przeciwnika
    if bug_pos.x != 0:
        if bug_pos.x > player_pos.x:
            bug_pos.x -= 200 * dt
        elif bug_pos.x < player_pos.x:
            bug_pos.x += 200 * dt
    if bug_pos.y != 0:
        if bug_pos.y > player_pos.y:
            bug_pos.y -= 200 * dt
        if bug_pos.y < player_pos.y:
            bug_pos.y += 200 * dt

    # zwiększenie wartości iteratora za każdym razem, gdy trwa atak mieczem (pozwalające kontynuować animację)
    if hitting:
        iter += 1

    # zakończenie ruchu mieczem - funkcja odpowiedzialna za atak przyjmuje wartość fałsz, a iterator wraca do wartości początkowej
    if iter >= len(sword_sprite):
        iter = 0
        hitting = False

    # animacja
    sword = sword_sprite[iter]

    # zmiana rozmiaru miecza w trakcie animacji
    sword = pygame.transform.scale(sword, (sword_x_size, sword_y_size))

    # wyświetlenie miecza, kamienia i robaka
    screen.blit(sword, (player_pos.x + stone_x_size, player_pos.y - stone_y_size / 2))
    screen.blit(stone, (player_pos.x, player_pos.y))
    screen.blit(bug, (bug_pos.x, bug_pos.y))

    # kolizja obiektów
    # - gdy zderzy się miecz i przeciwnik oraz następuje atak mieczem, zdrowie przeciwnika spada o 10
    # - gdy zetkną się kamień i przeciwnik, zdrowie kamienia spada o ustaloną wartość z każdą sekundą kolizji
    if pygame.Rect.colliderect(rect_sword, rect_bug) and one_hit_stone:
        bug_hp -= 10
        one_hit_stone = False
    if pygame.Rect.colliderect(rect_bug, rect_stone):
        stone_hp -= 1

    # zatrzymanie gry, gdy zdrowie kamienia lub przeciwnika spadnie do zera
    # - gdy kamień zginie, wyświetla się informacja o zwycięstwie (w konsoli)
    # - gdy zginie przeciwnik, wyświetla się informacja o porażce (również w konsoli)
    if bug_hp <= 0:
        print("Congratulations. You won")
        program_running = False
    elif stone_hp <= 0:
        print("Game over")
        program_running = False

    """poniżej zakomentowane metody pozwalające pokolorować hitboxy poszczególnych obiektów, w celu sprawdzenia sposobu ich zachowania się

    pygame.draw.rect(screen, (0, 0, 0), rect_stone)
    pygame.draw.rect(screen, (0, 0, 255), rect_sword)
    pygame.draw.rect(screen, (0, 255, 0), rect_bug)"""

    # update wyświetlanych na ekranie obiektów przy każdej iteracji pętli
    pygame.display.update()

    # białe tło ekranu
    screen.fill("white")

    # zmienna pomocnicza niezbędna przy mechanice sterowania klawiszami
    dt = clock.tick(60) / 1000
