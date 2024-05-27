# Example file showing a circle moving on screen
import pygame
import random
import math

# pygame setup
pygame.init()

height = 720
width = 1280
screen = pygame.display.set_mode((width, height))

licznik_mrowek = 0
bug_resp = False
bug_resp_2 = False
bug_resp_3 = False

class Wrog:
    def __init__(self, kolor_hitboxu, nazwa_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga, grafika):
        self.nazwa = nazwa_wroga
        self.kolor = kolor_hitboxu
        self.rect = pygame.Rect(wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga)
        self.rect_hitbox = pygame.Rect(30, 30, szerokosc_wroga/1.3, wysokosc_wroga/1.2)
        self.grafika = grafika

    def create_surface(self):
        return pygame.image.load(self.grafika)

    def draw(self, surface):
        pygame.draw.rect(surface, self.kolor, self.rect)

    def hitbox(self, surface):
        pygame.draw.rect(surface, self.kolor, self.rect_hitbox)

    def move_towards(self, target_rect):
        if abs(self.rect.x - target_rect.x) < 5 or abs(self.rect.x - target_rect.y) < 5:
            if self.rect.x < target_rect.x:
                self.rect.x += 200
            elif self.rect.x > target_rect.x:
                self.rect.x -= 200
            if self.rect.y < target_rect.y:
                self.rect.y += 200
            elif self.rect.y > target_rect.y:
                self.rect.y -= 200

"""
class Pocisk(Wrog):
    def __init__(self, nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga):
        super().__init__(nazwa_wroga, kolor_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga)
        self.predkosc_x = 5

    def update(self, dt):
        self.rect.x += self.predkosc_x * dt
"""

# informacje o mieczu
sword_x_size = 70
sword_y_size = 70

sword = pygame.image.load("miecz.jpg")
sword = pygame.transform.scale(sword, (sword_x_size, sword_y_size))

sword_left = pygame.transform.flip(sword, True, False)

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

stone = pygame.image.load('animations/player_spawn/1.png')
stone = pygame.transform.scale(stone, (stone_x_size, stone_y_size))

# informacje o chrząszczu
bug_x_size = 75
bug_y_size = 50

bug_x_size_2 = 75
bug_y_size_2 = 50

bug_x_size_3 = 75
bug_y_size_3 = 50

# losowa początkowa pozycja chrząszcza
bug_x_rng = random.randint(60, 900)
bug_y_rng = random.randint(40, 540)

bug_x_rng_2 = random.randint(60, 900)
bug_y_rng_2 = random.randint(40, 540)

bug_x_rng_3 = random.randint(60, 900)
bug_y_rng_3 = random.randint(40, 540)

# sprawienie aby chrząszcz nie pojawił się w miejscu początkowego umiejscowienia gracza
if bug_x_rng <= 480:
    bug_x_rand = bug_x_rng
else:
    bug_x_rand = bug_x_rng + 320

if bug_y_rng <= 290:
    bug_y_rand = bug_y_rng
else:
    bug_y_rand = bug_y_rng + 180


if bug_x_rng_2 <= 480:
    bug_x_rand_2 = bug_x_rng_2
else:
    bug_x_rand_2 = bug_x_rng_2 + 320

if bug_y_rng_2 <= 290:
    bug_y_rand_2 = bug_y_rng_2
else:
    bug_y_rand_2 = bug_y_rng_2 + 180


if bug_x_rng_3 <= 480:
    bug_x_rand_3 = bug_x_rng_3
else:
    bug_x_rand_3 = bug_x_rng_3 + 320

if bug_y_rng_3 <= 290:
    bug_y_rand_3 = bug_y_rng_3
else:
    bug_y_rand_3 = bug_y_rng_3 + 180

bug_wrog = Wrog((255, 0, 0), "bug", bug_x_rand, bug_y_rand, bug_x_size, bug_y_size, "animations/ant_move/1.png")
bug_wrog_2 = Wrog((255, 0, 0), "bug_2", bug_x_rand_2, bug_y_rand_2, bug_x_size_2, bug_y_size_2, "animations/ant_move/1.png")
bug_wrog_3 = Wrog((255, 0, 0), "bug_3", bug_x_rand_3, bug_y_rand_3, bug_x_size_3, bug_y_size_3, "animations/ant_move/1.png")

bug = bug_wrog.create_surface()
bug_2 = bug_wrog_2.create_surface()
bug_3 = bug_wrog_3.create_surface()

bug = pygame.transform.scale(bug, (bug_x_size, bug_y_size))
bug_v_start = 200

bug_2 = pygame.transform.scale(bug_2, (bug_x_size_2, bug_y_size_2))
bug_v_start_2 = 200

bug_3 = pygame.transform.scale(bug_3, (bug_x_size_3, bug_y_size_3))
bug_v_start_3 = 200

rect_bug = pygame.Rect(0, 0, 0, 0)
rect_bug_hp = pygame.Rect(0, 0, 0, 0)

rect_bug_2 = pygame.Rect(0, 0, 0, 0)
rect_bug_hp_2 = pygame.Rect(0, 0, 0, 0)

rect_bug_3 = pygame.Rect(0, 0, 0, 0)
rect_bug_hp_3 = pygame.Rect(0, 0, 0, 0)

# pozycja gracza
player_pos = pygame.Vector2((screen.get_width() / 2) - stone_x_size / 2, (screen.get_height() / 2) - stone_y_size / 2)

# pozycja chrząszcza
bug_pos = pygame.Vector2(bug_x_rand, bug_y_rand)
bug_pos_2 = pygame.Vector2(bug_x_rand_2, bug_y_rand_2)
bug_pos_3 = pygame.Vector2(bug_x_rand_3, bug_y_rand_3)

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

left = False
right = False
up = False
down = False

last_left = False
last_right = False

bug_left = False
bug_right = False
bug_up = False
bug_down = False

bug_left_2 = False
bug_right_2 = False
bug_up_2 = False
bug_down_2 = False

bug_left_3 = False
bug_right_3 = False
bug_up_3 = False
bug_down_3 = False

mouse = False

# ruch robaka
bug_movement = True
bug_movement_x = True
bug_movement_y = True

bug_movement_2 = True
bug_movement_x_2 = True
bug_movement_y_2 = True

bug_movement_3 = True
bug_movement_x_3 = True
bug_movement_y_3 = True

# start gry
game_starting = True

# funkcja logiczna - sprawdzenie czy następuje atak mieczem
one_hit_stone = False
one_hit_bug = False
one_hit_bug_2 = False
one_hit_bug_3 = False

# punkty zdrowia
stone_hp = 100
bug_hp = 100
bug_hp_2 = 100
bug_hp_3 = 100

# animacja player_move
player_move = []
for i in range(1, 10):
    player_move.append(pygame.transform.scale(pygame.image.load("animations/player_move/" + str(i) + ".png"), (1.5 * stone_x_size, 1.5 * stone_y_size)))

#animacja ant_move
ant_move = []
for i in range(1, 7):
    ant_move.append(pygame.transform.scale(pygame.image.load("animations/ant_move/" + str(i) + ".png"), (1.5 * bug_x_size, 1.5 * bug_y_size)))


#animacja player_spawn
player_spawn = []
for i in range(1, 32):
    player_spawn.append(pygame.transform.scale(pygame.image.load("animations/player_spawn/" + str(i) + ".png"), (1.5 * stone_x_size, 1.5 * stone_y_size)))

#iteratory
iter_pm = 1
iter_am = 1
iter_am_2 = 1
iter_am_3 = 1
iter_ps = 1

while program_running:
    if game_starting:
        if iter_ps < len(player_spawn):
            stone = player_spawn[iter_ps]
            iter_ps += 1
        else:
            game_starting = False

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            hitting = True
            one_hit_stone = True
            mouse = True

    # wciśnięcie klawisza
    key_pressed = pygame.key.get_pressed()

    # prostokąty ustalające hitboxy danego obiektu (pisane ręcznie zamiast wykorzystania metody get_rect())
    if not last_left:
        rect_sword = pygame.Rect(player_pos.x + stone_x_size, player_pos.y - sword_y_size + (4 * stone_y_size / 5), 1.1 * sword_x_size, 1.1 * sword_y_size)
    else:
        rect_sword = pygame.Rect(player_pos.x - stone_x_size + 30, player_pos.y - sword_y_size + (4 * stone_y_size / 5), 1.1 * sword_x_size, 1.1 * sword_y_size)

    rect_stone = pygame.Rect(player_pos.x + 0.3 * stone_x_size, player_pos.y + 0.5 * stone_y_size, 0.8 * stone_x_size, 0.9 * stone_y_size)
    if bug_resp:
        rect_bug = pygame.Rect(bug_pos.x + 0.45 * bug_x_size, bug_pos.y + 0.6 * bug_y_size, 0.7 * bug_x_size, 0.8 * bug_y_size)
    bug_hitbox = bug_wrog.rect

    if bug_resp_2:
        rect_bug_2 = pygame.Rect(bug_pos_2.x + 0.45 * bug_x_size_2, bug_pos_2.y + 0.6 * bug_y_size_2, 0.7 * bug_x_size_2, 0.8 * bug_y_size_2)
    bug_hitbox_2 = bug_wrog_2.rect

    if bug_resp_3:
        rect_bug_3 = pygame.Rect(bug_pos_3.x + 0.45 * bug_x_size_3, bug_pos_3.y + 0.6 * bug_y_size_3, 0.7 * bug_x_size_3, 0.8 * bug_y_size_3)
    bug_hitbox_3 = bug_wrog_3.rect

    # paski zdrowia
    rect_stone_hp = pygame.Rect(player_pos.x, player_pos.y - 20, stone_hp, 10)
    if bug_resp:
        rect_bug_hp = pygame.Rect(bug_pos.x, bug_pos.y - 10, bug_hp, 10)

    rect_stone_hp_2 = pygame.Rect(player_pos.x, player_pos.y - 20, stone_hp, 10)
    if bug_resp_2:
        rect_bug_hp_2 = pygame.Rect(bug_pos_2.x, bug_pos_2.y - 10, bug_hp_2, 10)

    rect_stone_hp_3 = pygame.Rect(player_pos.x, player_pos.y - 20, stone_hp, 10)
    if bug_resp_3:
        rect_bug_hp_3 = pygame.Rect(bug_pos_3.x, bug_pos_3.y - 10, bug_hp_3, 10)

    # zablokowanie ruchu, gdy bohater znajdzie się na brzegu ekranu
    if player_pos.x <= 0:
        movement_left = False
    if player_pos.x >= width - stone_x_size:
        movement_right = False
    if player_pos.y <= 0:
        movement_up = False
    if player_pos.y >= height - stone_y_size:
        movement_down = False
    if 0 < player_pos.x < width - stone_x_size:
        movement_right = True
        movement_left = True
    if 0 < player_pos.y < height - stone_y_size:
        movement_up = True
        movement_down = True

    # ruch postaci (strzałkami lub WASD)
    if not game_starting:
        if (key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]) and movement_up:
            player_pos.y -= 400 * dt
            up = True
            down = False
            stone = player_move[iter_pm]
        elif (key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]) and movement_down:
            player_pos.y += 400 * dt
            down = True
            up = False
            stone = player_move[iter_pm]
        elif (key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]) and movement_left:
            player_pos.x -= 400 * dt
            left = True
            last_left = True
            right = False
            last_right = False
            stone = player_move[iter_pm]
        elif (key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]) and movement_right:
            player_pos.x += 400 * dt
            right = True
            last_right = True
            left = False
            last_left = False
            stone = player_move[iter_pm]
        else:
            right = False
            left = False
            up = False
            down = False

    if mouse:
        x, y = pygame.mouse.get_pos()

        if x < player_pos.x + stone_x_size/2:
            left = True
            last_left = True
            right = False
            last_right = False
        elif x > player_pos.x + stone_x_size/2:
            left = False
            last_left = False
            right = True
            last_right = True
        else:
            left = False
            last_left = False
            right = False
            last_right = False

    #ruch wroga
    if bug_resp:
        if game_starting:
            bug_v = 1/2 * bug_v_start
        else:
            bug_v = bug_v_start

        bug_v_dx = abs(player_pos.x - bug_pos.x)
        bug_v_dy = abs(player_pos.y - bug_pos.y)

        bug_v_y = bug_v * bug_v_dy * math.sqrt(1/((bug_v_dx * bug_v_dx) + (bug_v_dy * bug_v_dy)))
        bug_v_x = bug_v_y * (bug_v_dx/bug_v_dy)

        mistake_range = 30

        if abs(bug_pos.x - player_pos.x - 10) > mistake_range:
            bug_movement_x = True
        else:
            bug_movement_x = False
            bug_left = False
            bug_right = False

        if abs(bug_pos.y - player_pos.y) > mistake_range:
            bug_movement_y = True
        else:
            bug_movement_y = False
            bug_up = False
            bug_down = False

        if bug_movement_x or bug_movement_y:
            bug_movement = True
        else:
            bug_movement = False
            bug_left = False
            bug_right = False
            bug_up = False
            bug_down = False

        if bug_movement_x:
            if bug_pos.x - player_pos.x - 10 > mistake_range:
                bug_v_x = -bug_v_x
                bug_left = True
                bug_right = False
            else:
                bug_left = False
                bug_right = True
            bug_pos.x += bug_v_x * dt

        if bug_movement_y:
            if bug_pos.y - player_pos.y > mistake_range:
                bug_v_y = -bug_v_y
                bug_up = True
                bug_down = False
            else:
                bug_up = False
                bug_down = True
            bug_pos.y += bug_v_y * dt

    if bug_movement:
        bug = ant_move[iter_am]
        iter_am += 1

    # ruch wroga 2
    if bug_resp_2:
        if game_starting:
            bug_v_2 = 1 / 2 * bug_v_start_2
        else:
            bug_v_2 = bug_v_start_2

        bug_v_dx_2 = abs(player_pos.x - bug_pos_2.x)
        bug_v_dy_2 = abs(player_pos.y - bug_pos_2.y)

        bug_v_y_2 = bug_v_2 * bug_v_dy_2 * math.sqrt(1 / ((bug_v_dx_2 * bug_v_dx_2) + (bug_v_dy_2 * bug_v_dy_2)))
        bug_v_x_2 = bug_v_y_2 * (bug_v_dx_2 / bug_v_dy_2)

        mistake_range_2 = 30

        if abs(bug_pos_2.x - player_pos.x - 10) > mistake_range_2:
            bug_movement_x_2 = True
        else:
            bug_movement_x_2 = False
            bug_left_2 = False
            bug_right_2 = False

        if abs(bug_pos_2.y - player_pos.y) > mistake_range_2:
            bug_movement_y_2 = True
        else:
            bug_movement_y_2 = False
            bug_up_2 = False
            bug_down_2 = False

        if bug_movement_x_2 or bug_movement_y_2:
            bug_movement_2 = True
        else:
            bug_movement_2 = False
            bug_left_2 = False
            bug_right_2 = False
            bug_up_2 = False
            bug_down_2 = False

        if bug_movement_x_2:
            if bug_pos_2.x - player_pos.x - 10 > mistake_range_2:
                bug_v_x_2 = -bug_v_x_2
                bug_left_2 = True
                bug_right_2 = False
            else:
                bug_left_2 = False
                bug_right_2 = True
            bug_pos_2.x += bug_v_x_2 * dt

        if bug_movement_y_2:
            if bug_pos_2.y - player_pos.y > mistake_range_2:
                bug_v_y_2 = -bug_v_y_2
                bug_up_2 = True
                bug_down_2 = False
            else:
                bug_up_2 = False
                bug_down_2 = True
            bug_pos_2.y += bug_v_y_2 * dt

    if bug_movement_2:
        bug_2 = ant_move[iter_am_2]
        iter_am_2 += 1

    # ruch wroga 3
    if bug_resp_3:
        if game_starting:
            bug_v_3 = 1 / 2 * bug_v_start_3
        else:
            bug_v_3 = bug_v_start_3

        bug_v_dx_3 = abs(player_pos.x - bug_pos_3.x)
        bug_v_dy_3 = abs(player_pos.y - bug_pos_3.y)

        bug_v_y_3 = bug_v_3 * bug_v_dy_3 * math.sqrt(1 / ((bug_v_dx_3 * bug_v_dx_3) + (bug_v_dy_3 * bug_v_dy_3)))
        bug_v_x_3 = bug_v_y_3 * (bug_v_dx_3 / bug_v_dy_3)

        mistake_range_3 = 30

        if abs(bug_pos_3.x - player_pos.x - 10) > mistake_range_3:
            bug_movement_x_3 = True
        else:
            bug_movement_x_3 = False
            bug_left_3 = False
            bug_right_3 = False

        if abs(bug_pos_3.y - player_pos.y) > mistake_range_3:
            bug_movement_y_3 = True
        else:
            bug_movement_y_3 = False
            bug_up_3 = False
            bug_down_3 = False

        if bug_movement_x_3 or bug_movement_y_3:
            bug_movement_3 = True
        else:
            bug_movement_3 = False
            bug_left_3 = False
            bug_right_3 = False
            bug_up_3 = False
            bug_down_3 = False

        if bug_movement_x_3:
            if bug_pos_3.x - player_pos.x - 10 > mistake_range_3:
                bug_v_x_3 = -bug_v_x_3
                bug_left_3 = True
                bug_right_3 = False
            else:
                bug_left_3 = False
                bug_right_3 = True
            bug_pos_3.x += bug_v_x_3 * dt

        if bug_movement_y_3:
            if bug_pos_3.y - player_pos.y > mistake_range_3:
                bug_v_y_3 = -bug_v_y_3
                bug_up_3 = True
                bug_down_3 = False
            else:
                bug_up_3 = False
                bug_down_3 = True
            bug_pos_3.y += bug_v_y_3 * dt

    if bug_movement_3:
        bug_3 = ant_move[iter_am_3]
        iter_am_3 += 1

    if iter_am >= len(ant_move):
        iter_am = 1

    if iter_am_2 >= len(ant_move):
        iter_am_2 = 1

    if iter_am_3 >= len(ant_move):
        iter_am_3 = 1

    # zwiększenie wartości iteratora za każdym razem, gdy trwa atak mieczem (pozwalające kontynuować animację)
    if hitting:
        iter += 1

    # zakończenie ruchu mieczem - funkcja odpowiedzialna za atak przyjmuje wartość fałsz, a iterator wraca do wartości początkowej
    if iter >= len(sword_sprite):
        iter = 0
        hitting = False

    if movement_up or movement_left or movement_down or movement_right:
        iter_pm += 1

    if iter_pm >= len(player_move):
        iter_pm = 1

    # animacja
    sword = sword_sprite[iter]

    # zmiana rozmiaru miecza w trakcie animacji
    sword = pygame.transform.scale(sword, (sword_x_size, sword_y_size))

    # wyświetlenie miecza, kamienia i robaka
    if left and last_left:
        sword = pygame.transform.flip(sword, True, False)
        screen.blit(sword, (player_pos.x - sword_x_size + 30, player_pos.y + stone_y_size / 4))
    elif right and last_right:
        screen.blit(sword, (player_pos.x + stone_x_size, player_pos.y + stone_y_size / 4))
    elif last_right:
        screen.blit(sword, (player_pos.x + stone_x_size, player_pos.y + stone_y_size / 4))
    elif last_left:
        sword = pygame.transform.flip(sword, True, False)
        screen.blit(sword, (player_pos.x - sword_x_size + 30, player_pos.y + stone_y_size / 4))
    else:
        screen.blit(sword, (player_pos.x + stone_x_size, player_pos.y + stone_y_size / 4))

    if left:
        stone = pygame.transform.flip(stone, True, False)
        screen.blit(stone, (player_pos.x, player_pos.y))
    else:
        screen.blit(stone, (player_pos.x, player_pos.y))

    if not bug_resp_2:
        bug_resp_2 = (random.randint(0, 3000) <= 2)

    if bug_resp_2:
        if bug_right_2:
            bug_2 = pygame.transform.flip(bug_2, True, False)
            screen.blit(bug_2, (bug_pos_2.x, bug_pos_2.y))
        else:
            screen.blit(bug_2, (bug_pos_2.x, bug_pos_2.y))

    if not bug_resp_3:
        bug_resp_3 = (random.randint(0, 15000) <= 2)

    if bug_resp_3:
        if bug_right_3:
            bug_3 = pygame.transform.flip(bug_3, True, False)
            screen.blit(bug_3, (bug_pos_3.x, bug_pos_3.y))
        else:
            screen.blit(bug_3, (bug_pos_3.x, bug_pos_3.y))

    if not bug_resp:
        bug_resp = (random.randint(0, 500) <= 2)

    if bug_resp:
        if bug_right:
            bug = pygame.transform.flip(bug, True, False)
            screen.blit(bug, (bug_pos.x, bug_pos.y))
        else:
            screen.blit(bug, (bug_pos.x, bug_pos.y))

    pygame.draw.rect(screen, (0, 128, 0), rect_stone_hp)

    if bug_resp:
        pygame.draw.rect(screen, (255, 0, 0, 0), rect_bug_hp)

    if bug_resp_2:
        pygame.draw.rect(screen, (255, 0, 0, 0), rect_bug_hp_2)

    if bug_resp_3:
        pygame.draw.rect(screen, (255, 0, 0, 0), rect_bug_hp_3)

    if pygame.Rect.colliderect(rect_sword, rect_bug) and one_hit_stone:
        bug_hp -= 10
        one_hit_stone = False
    if pygame.Rect.colliderect(rect_sword, rect_bug_2) and one_hit_stone:
        bug_hp_2 -= 10
        one_hit_stone = False
    if pygame.Rect.colliderect(rect_sword, rect_bug_3) and one_hit_stone:
        bug_hp_3 -= 10
        one_hit_stone = False

    if pygame.Rect.colliderect(rect_bug, rect_stone) and bug_resp:
        stone_hp -= 1
    if pygame.Rect.colliderect(rect_bug_2, rect_stone) and bug_resp_2:
        stone_hp -= 1
    if pygame.Rect.colliderect(rect_bug_3, rect_stone) and bug_resp_3:
        stone_hp -= 1

    # zatrzymanie gry, gdy zdrowie kamienia lub przeciwnika spadnie do zera
    # - gdy kamień zginie, wyświetla się informacja o zwycięstwie (w konsoli)
    # - gdy zginie przeciwnik, wyświetla się informacja o porażce (również w konsoli)

    if bug_hp <= 0:
        licznik_mrowek += 1
        pygame.time.wait(80)
        bug_x_rng = random.randint(0, width - 320)
        bug_y_rng = random.randint(0, height - 180)
        bug_resp = False
        if bug_x_rng <= player_pos.x - 160:
            bug_pos.x = bug_x_rng
        else:
            bug_pos.x = bug_x_rng + 320

        if bug_y_rng <= player_pos.y - 90:
            bug_pos.y = bug_y_rng
        else:
            bug_pos.y = bug_y_rng + 180
        bug = bug_wrog.create_surface()
        bug = pygame.transform.scale(bug, (bug_x_size, bug_y_size))
        bug_hp = 100

    if bug_hp_2 <= 0:
        licznik_mrowek += 1
        pygame.time.wait(80)
        bug_x_rng_2 = random.randint(0, width - 320)
        bug_y_rng_2 = random.randint(0, height - 180)
        bug_resp_2 = False
        if bug_x_rng_2 <= player_pos.x - 160:
            bug_pos_2.x = bug_x_rng_2
        else:
            bug_pos_2.x = bug_x_rng_2 + 320

        if bug_y_rng_2 <= player_pos.y - 90:
            bug_pos_2.y = bug_y_rng_2
        else:
            bug_pos_2.y = bug_y_rng_2 + 180
        bug_2 = bug_wrog_2.create_surface()
        bug_2 = pygame.transform.scale(bug_2, (bug_x_size_2, bug_y_size_2))
        bug_hp_2 = 100

    if bug_hp_3 <= 0:
        licznik_mrowek += 1
        pygame.time.wait(80)
        bug_x_rng_3 = random.randint(0, width - 320)
        bug_y_rng_3 = random.randint(0, height - 180)
        bug_resp_3 = False
        if bug_x_rng_3 <= player_pos.x - 160:
            bug_pos_3.x = bug_x_rng_3
        else:
            bug_pos_3.x = bug_x_rng_3 + 320

        if bug_y_rng_3 <= player_pos.y - 90:
            bug_pos_3.y = bug_y_rng_3
        else:
            bug_pos_3.y = bug_y_rng_3 + 180
        bug_3 = bug_wrog_3.create_surface()
        bug_3 = pygame.transform.scale(bug_3, (bug_x_size_3, bug_y_size_3))
        bug_hp_3 = 100

    if licznik_mrowek >= 10:
        print("Congratulations. You won")
        program_running = False
        pygame.quit()
        quit()
    elif stone_hp <= 0:
        print("Game over")
        program_running = False


    #poniżej zakomentowane metody pozwalające pokolorować hitboxy poszczególnych obiektów, w celu sprawdzenia sposobu ich zachowania się

    """
    pygame.draw.rect(screen, (0, 0, 0), rect_stone)
    pygame.draw.rect(screen, (0, 0, 255), rect_sword)
    pygame.draw.rect(screen, (0, 255, 0), rect_bug)"""

    # update wyświetlanych na ekranie obiektów przy każdej iteracji pętli
    pygame.display.update()

    # białe tło ekranu
    screen.fill("white")

    # zmienna pomocnicza niezbędna przy mechanice sterowania klawiszami
    dt = clock.tick(60) / 1000
