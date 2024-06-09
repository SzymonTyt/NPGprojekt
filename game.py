import pygame
import sys
from pygame.locals import *
import random
import math

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Menu Gry")

# Wczytywanie obrazów
background_image = pygame.image.load("data/images/background_menu.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

button_play_image = pygame.image.load("data/images/button_play.png")
button_play_hovered_image = pygame.image.load("data/images/button_play_hovered.png")
button_settings_image = pygame.image.load("data/images/button_settings.png")
button_settings_hovered_image = pygame.image.load("data/images/button_settings_hovered.png")
button_stats_image = pygame.image.load("data/images/button_stats.png")
button_stats_hovered_image = pygame.image.load("data/images/button_stats_hovered.png")
button_quit_image = pygame.image.load("data/images/button_quit.png")
button_quit_hovered_image = pygame.image.load("data/images/button_quit_hovered.png")

volume_rect = None

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (65, 88, 208)
HOVER_COLOR = (200, 50, 192)

# Czcionka
font = pygame.font.Font(None, 36)

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # -1 oznacza odtwarzanie w pętli

play_music("data/soundtrack/main_menu.mp3")

def stop_music():
    pygame.mixer.music.stop()

# Funkcje przycisków
def start_game():
    # pygame setup
    pygame.init()

    stop_music()

    pygame.mixer.music.load('data/soundtrack/early_game.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.45)

    # nowe iteratory
    iter_ant_death = 1
    iter_fly_move = 1
    iter_fly_death = 1
    iter_spider_move = 1
    iter_spider_death = 1
    iter_spider_missile = 1
    iter_spider_attack = 1
    iter_player_slow = 1

    spider_attack_animation = False
    player_slow = False

    ant_dying = False
    spider_dying = False
    fly_dying = False

    distance = 60

    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    width, height = screen.get_size()
    background = pygame.transform.scale(pygame.image.load("data/images/map_base.png"), (3200, 3000))
    trees = pygame.transform.scale(pygame.image.load("data/images/map_objects.png"), (3200, 3000))

    money_counter = 0

    money_pos_x = None
    money_pos_y = None
    money_r = 5
    money = pygame.image.load("data/animations/coin/1.png")
    money = pygame.transform.scale(money, (2 * money_r, 2 * money_r))
    money_existence = False
    money_rect = pygame.Rect(0, 0, 2 * money_r, 2 * money_r)
    iter_money = 1

    money_pos_x_2 = None
    money_pos_y_2 = None
    money_r_2 = 5
    money_2 = pygame.image.load("data/animations/coin/1.png")
    money_2 = pygame.transform.scale(money_2, (2 * money_r_2, 2 * money_r_2))
    money_existence_2 = False
    money_rect_2 = pygame.Rect(0, 0, 2 * money_r_2, 2 * money_r_2)
    iter_money_2 = 1

    money_pos_x_3 = 0
    money_pos_y_3 = 0
    money_r_3 = 5
    money_3 = pygame.image.load("data/animations/coin/1.png")
    money_3 = pygame.transform.scale(money_3, (2 * money_r_3, 2 * money_r_3))
    money_existence_3 = False
    money_rect_3 = pygame.Rect(0, 0, 2 * money_r_3, 2 * money_r_3)
    iter_money_3 = 1

    screen_pos_x = random.randint(-1650, -750)
    screen_pos_y = random.randint(-1650, -750)

    music_start = False
    music_one_time = False

    licznik_mrowek = 0
    bug_resp = False
    bug_resp_2 = False
    bug_resp_3 = False

    bug_up_block = False
    bug_down_block = False
    bug_left_block = False
    bug_right_block = False
    bug_up_block_2 = False
    bug_down_block_2 = False
    bug_left_block_2 = False
    bug_right_block_2 = False
    bug_up_block_3 = False
    bug_down_block_3 = False
    bug_left_block_3 = False
    bug_right_block_3 = False

    coin_1 = None
    coin_2 = None
    coin_3 = None
    coin_creating_1 = False
    coin_creating_2 = False
    coin_creating_3 = False

    screen_up = False
    screen_down = False
    screen_right = False
    screen_left = False

    class Wrog:
        def __init__(self, kolor_hitboxu, nazwa_wroga, wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga,
                     grafika):
            self.nazwa = nazwa_wroga
            self.kolor = kolor_hitboxu
            self.rect = pygame.Rect(wspolrzedna_x, wspolrzedna_y, szerokosc_wroga, wysokosc_wroga)
            self.rect_hitbox = pygame.Rect(30, 30, szerokosc_wroga / 1.3, wysokosc_wroga / 1.2)
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

    class Projectile:
        def __init__(self, x, y, direction):
            self.x = x
            self.y = y
            self.direction = direction
            self.speed = 5
            self.projectile_width = 10  # Dostosuj wymiary pocisku według potrzeb
            self.projectile_height = 10
            self.rect = pygame.Rect(x, y, self.projectile_width, self.projectile_height)

        def move(self):
            if self.direction == "1":
                self.x += self.speed
            elif self.direction == "2":
                self.x -= self.speed
            self.rect.topleft = (self.x, self.y)

        def draw(self, surface):
            pygame.draw.rect(surface, (255, 0, 0), self.rect)

        def p_colliderect(self, other_rect):
            return self.rect.colliderect(other_rect)

    # animacja coin
    coin_animation = []
    for i in range(1, 36):
        coin_animation.append(
            pygame.transform.scale(pygame.image.load("data/animations/coin/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.1 * 20, 1.1 * 20)))

    class Coin:
        def __init__(self, coin_pos_x, coin_pos_y, coin_x_size=20, coin_y_size=20):
            self.coin_pos_x = coin_pos_x
            self.coin_pos_y = coin_pos_y
            self.coin_x_size = coin_x_size
            self.coin_y_size = coin_y_size
            self.coin_rect = pygame.Rect(coin_pos_x, coin_pos_y, coin_x_size, coin_y_size)
            self.coin_surface = pygame.transform.scale(pygame.image.load('data/animations/coin/1.png'),
                                                       (coin_x_size, coin_y_size))
            self.coin_exist = True
            self.coin_animation_list = coin_animation
            self.iter_coin = 1
            self.bank = 0

        def coin_draw(self):
            if self.coin_exist:
                screen.blit(self.coin_surface, (self.coin_pos_x, self.coin_pos_y))
                print("coin exists")

        def coin_collect(self, surface):
            if pygame.Rect.colliderect(surface, self.coin_rect) and self.coin_exist:
                self.bank += 1
                self.coin_exist = False
                print("coin exists")
                return True
            return False

        def coin_anim(self):
            self.coin_surface = self.coin_animation_list[self.iter_coin]
            self.iter_coin += 1
            print("coin exists")
            if self.iter_coin >= len(self.coin_animation_list):
                self.iter_coin = 1

    # informacje o mieczu
    sword_x_size = 70
    sword_y_size = 70

    # informacje o kamieniu
    stone_x_size = 81
    stone_y_size = 54

    stone = pygame.image.load('data/animations/player_spawn/1.png')
    stone = pygame.transform.scale(stone, (stone_x_size, stone_y_size))

    # informacje o chrząszczu
    bug_x_size = 75
    bug_y_size = 50

    bug_x_size_2 = 132
    bug_y_size_2 = 100

    bug_x_size_3 = 30
    bug_y_size_3 = 20

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

    bug_wrog = Wrog((255, 0, 0), "bug", bug_x_rand, bug_y_rand, bug_x_size, bug_y_size,
                    "data/animations/ant_move/1.png")
    bug_wrog_2 = Wrog((255, 0, 0), "bug_2", bug_x_rand_2, bug_y_rand_2, bug_x_size_2, bug_y_size_2,
                      "data/animations/spider_move/1.png")
    bug_wrog_3 = Wrog((255, 0, 0), "bug_3", bug_x_rand_3, bug_y_rand_3, bug_x_size_3, bug_y_size_3,
                      "data/animations/fly_move/1.png")

    bug = bug_wrog.create_surface()
    bug_2 = bug_wrog_2.create_surface()
    bug_3 = bug_wrog_3.create_surface()

    ant_attack_dmg = 18
    player_velocity = 400
    player_dmg = 9

    bug = pygame.transform.scale(bug, (bug_x_size, bug_y_size))
    bug_v_start = 225

    bug_2 = pygame.transform.scale(bug_2, (bug_x_size_2, bug_y_size_2))
    bug_v_start_2 = 150

    bug_3 = pygame.transform.scale(bug_3, (bug_x_size_3, bug_y_size_3))
    bug_v_start_3 = 300

    rect_bug = pygame.Rect(0, 0, 0, 0)
    rect_bug_hp = pygame.Rect(0, 0, 0, 0)

    rect_bug_2 = pygame.Rect(0, 0, 0, 0)
    rect_bug_hp_2 = pygame.Rect(0, 0, 0, 0)

    rect_bug_3 = pygame.Rect(0, 0, 0, 0)
    rect_bug_hp_3 = pygame.Rect(0, 0, 0, 0)

    # pozycja gracza
    player_pos = pygame.Vector2((screen.get_width() / 2) - stone_x_size / 2,
                                (screen.get_height() / 2) - stone_y_size / 2)

    # pozycja chrząszcza
    bug_pos = pygame.Vector2(bug_x_rand, bug_y_rand)
    bug_pos_2 = pygame.Vector2(bug_x_rand_2, bug_y_rand_2)
    bug_pos_3 = pygame.Vector2(bug_x_rand_3, bug_y_rand_3)

    # informacje o pocisku
    bullet_r = 5
    bullet_pos = pygame.Vector2(bug_pos.x, bug_pos.y)

    bullet = pygame.Rect(bullet_pos.x + 5, bullet_pos.y + 5, 2 * bullet_r, 2 * bullet_r)

    x_aim = 0
    y_aim = 0

    bullet_v_dx_start = 0
    bullet_v_dy_start = 0

    bullet_v = 1200

    # informacje o pocisku
    bullet_r_2 = 40
    bullet_pos_2 = pygame.Vector2(bug_pos.x, bug_pos.y)

    bullet_2_img = pygame.image.load("data/animations/spider_missile/1.png")
    bullet_2_img = pygame.transform.scale(bullet_2_img, (2 * bullet_r_2, 2 * bullet_r_2))
    bullet_2 = pygame.Rect(bullet_pos_2.x + 16, bullet_pos_2.y + 25, 2 * bullet_r_2, 1.3 * bullet_r_2)

    x_aim_2 = 0
    y_aim_2 = 0

    bullet_v_dx_start_2 = 0
    bullet_v_dy_start_2 = 0

    bullet_v_2 = 725

    # informacje o pocisku
    bullet_r_3 = 5
    bullet_pos_3 = pygame.Vector2(bug_pos.x, bug_pos.y)

    bullet_3 = pygame.Rect(bullet_pos_3.x + 5, bullet_pos_3.y + 5, 2 * bullet_r_3, 2 * bullet_r_3)

    x_aim_3 = 0
    y_aim_3 = 0

    bullet_v_dx_start_3 = 0
    bullet_v_dy_start_3 = 0

    bullet_v_3 = 1000

    melee_ant_attack = False
    melee_ant_attack_animation = False
    melee_ant_attack_block = False
    if_bonus = False
    bonus_time = False

    # zegar
    clock = pygame.time.Clock()
    dt = 0

    # funkcje logiczne
    program_running = True
    hitting = False

    # szanse respawnu (na 100000)
    chance_of_resp_melee_ant = 98000
    chance_of_resp_ranged_ant_1 = 97000
    chance_of_resp_ranged_ant_2 = 99000

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

    # atak robaka
    bug_attack = False
    bug_attack_start = False
    bug_attack_cast = False

    bug_attack_2 = False
    bug_attack_start_2 = False
    bug_attack_cast_2 = False

    bug_attack_3 = False
    bug_attack_start_3 = False
    bug_attack_cast_3 = False

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

    bullet_block = False
    bullet_block_2 = False
    bullet_block_3 = False

    bullet_block_time = 12
    ant_attack_block_time = 25

    attack_movement_block = False

    # start gry
    game_starting = True

    # funkcja logiczna - sprawdzenie czy następuje atak mieczem
    one_hit_stone = False
    one_hit_bug = False
    one_hit_bug_2 = False
    one_hit_bug_3 = False
    one_hit_bullet = False
    one_hit_bullet_2 = False
    one_hit_bullet_3 = False

    # punkty zdrowia
    stone_hp = 100
    bug_hp = 100
    bug_hp_2 = 175
    bug_hp_3 = 40

    game_end = False

    # animacja player_move
    player_move = []
    for i in range(1, 18):
        player_move.append(
            pygame.transform.scale(pygame.image.load("data/animations/player_move/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * stone_x_size, 1.5 * stone_y_size)))

    # animacja ant_move
    ant_move = []
    for i in range(1, 12):
        ant_move.append(
            pygame.transform.scale(pygame.image.load("data/animations/ant_move/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * bug_x_size, 1.5 * bug_y_size)))

    # animacja player_spawn
    player_spawn = []
    for i in range(1, 62):
        player_spawn.append(
            pygame.transform.scale(pygame.image.load("data/animations/player_spawn/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * stone_x_size, 1.5 * stone_y_size)))

    # animacja player_attack
    player_attack = []
    for i in range(1, 8):
        player_attack.append(
            pygame.transform.scale(pygame.image.load("data/animations/player_attack_1/" + str(i) + ".png"),
                                   (1.5 * sword_x_size, 1.5 * sword_y_size)))

    # animacja player_idle
    player_idle = []
    for i in range(1, 14):
        player_idle.append(
            pygame.transform.scale(pygame.image.load("data/animations/player_idle/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * stone_x_size, 1.5 * stone_y_size)))

    # animacja player_death
    player_death = []
    for i in range(1, 50):
        player_death.append(
            pygame.transform.scale(pygame.image.load("data/animations/player_death/" + str(math.ceil(i / 2)) + ".png"),
                                   (2 * stone_x_size, 2 * stone_y_size)))

    # animacja ant_attack
    ant_attack = []
    for i in range(1, 14):
        ant_attack.append(
            pygame.transform.scale(pygame.image.load("data/animations/ant_attack/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * bug_x_size, 2 * bug_y_size)))

    # animacja ant_death
    ant_death = []
    for i in range(1, 21):
        ant_death.append(
            pygame.transform.scale(pygame.image.load("data/animations/ant_death/" + str(math.ceil(i / 3)) + ".png"),
                                   (1.1 * bug_x_size, 1.1 * bug_y_size)))

    # animacja fly_move
    fly_move = []
    for i in range(1, 8):
        fly_move.append(
            pygame.transform.scale(pygame.image.load("data/animations/fly_move/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * bug_x_size_3, 1.5 * bug_y_size_3)))

    # animacja fly_death
    fly_death = []
    for i in range(1, 22):
        fly_death.append(
            pygame.transform.scale(pygame.image.load("data/animations/fly_death/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * bug_x_size_3, 1.5 * bug_y_size_3)))

    # animacja spider_move
    spider_move = []
    for i in range(1, 12):
        spider_move.append(
            pygame.transform.scale(pygame.image.load("data/animations/spider_move/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * bug_x_size_2, 1.5 * bug_y_size_2)))

    # animacja spider_death
    spider_death = []
    for i in range(1, 20):
        spider_death.append(
            pygame.transform.scale(pygame.image.load("data/animations/spider_death/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * bug_x_size_2, 1.5 * bug_y_size_2)))

    # animacja spider_missile
    spider_missile = []
    for i in range(1, 16):
        spider_missile.append(pygame.transform.scale(
            pygame.image.load("data/animations/spider_missile/" + str(math.ceil(i / 4)) + ".png"),
            (2.5 * bullet_r_2, 2.5 * bullet_r_2)))

    # animacja spider_attack
    spider_attack = []
    for i in range(1, 14):
        spider_attack.append(
            pygame.transform.scale(pygame.image.load("data/animations/spider_attack/" + str(math.ceil(i / 2)) + ".png"),
                                   (1.5 * bug_x_size_2, 1.5 * bug_y_size_2)))

    # iteratory
    iter_pm = 1
    iter_am = 1
    iter_am_2 = 1
    iter_am_3 = 1
    iter_ps = 1
    iter_bug_shoot = 1
    iter_bug_shoot_2 = 1
    iter_bug_shoot_3 = 1
    iter_player_attack = 1
    iter_block_bullet = 1
    iter_block_bullet_2 = 1
    iter_block_bullet_3 = 1
    iter_player_idle = 1
    iter_player_death = 1
    iter_ant_attack = 1
    iter_block_ant_attack = 1
    iter_bonus_time = 1

    while program_running:
        screen.blit(background, (screen_pos_x, screen_pos_y))

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

            # ustawienie funkcji logicznych odpowiedzialnych za atak mieczem na True pod wpływem wciśniętej spacji
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hitting = True
                    one_hit_stone = True
                if event.key == K_ESCAPE:
                    program_running = False
                    pygame.mixer.music.unload()
                    play_music("data/soundtrack/main_menu.mp3")

            if event.type == pygame.MOUSEBUTTONDOWN:
                hitting = True
                one_hit_stone = True
                mouse = True

        # wciśnięcie klawisza
        key_pressed = pygame.key.get_pressed()

        # prostokąty ustalające hitboxy danego obiektu (pisane ręcznie zamiast wykorzystania metody get_rect())
        if not left and not right:
            rect_sword = pygame.Rect(player_pos.x + (7 / 8 * stone_x_size), player_pos.y + (1 * stone_y_size / 5),
                                     sword_x_size + 5, 0.9 * sword_y_size)
        elif not last_left:
            rect_sword = pygame.Rect(player_pos.x + (7 / 8 * stone_x_size), player_pos.y + (1 * stone_y_size / 5),
                                     sword_x_size + 5, 0.9 * sword_y_size)
        else:
            rect_sword = pygame.Rect(player_pos.x - (3 / 4 * stone_x_size) + 30, player_pos.y + (1 * stone_y_size / 5),
                                     sword_x_size + 5, 0.9 * sword_y_size)

        rect_stone = pygame.Rect(player_pos.x + 0.3 * stone_x_size, player_pos.y + 0.5 * stone_y_size,
                                 0.8 * stone_x_size, 0.9 * stone_y_size)

        if bug_right:
            rect_melee_ant = pygame.Rect(bug_pos.x + 1.1 * bug_x_size, bug_pos.y + 0.2 * bug_y_size, 0.4 * bug_x_size,
                                         1.2 * bug_y_size)
        else:
            rect_melee_ant = pygame.Rect(bug_pos.x, bug_pos.y + 0.2 * bug_y_size, 0.4 * bug_x_size, 1.2 * bug_y_size)

        if bug_resp:
            rect_bug = pygame.Rect(bug_pos.x + 0.45 * bug_x_size, bug_pos.y + 0.6 * bug_y_size, 0.7 * bug_x_size,
                                   0.8 * bug_y_size)
        bug_hitbox = bug_wrog.rect
        bullet = pygame.Rect(bullet_pos.x + 5, bullet_pos.y + 5, 2 * bullet_r, 2 * bullet_r)

        if bug_resp_2:
            rect_bug_2 = pygame.Rect(bug_pos_2.x + 10, bug_pos_2.y + 5, 1.35 * bug_x_size_2, 1.35 * bug_y_size_2)
        bug_hitbox_2 = bug_wrog_2.rect
        bullet_2 = pygame.Rect(bullet_pos_2.x + 14, bullet_pos_2.y + 25, 2 * bullet_r_2, 1.2 * bullet_r_2)

        if bug_resp_3:
            rect_bug_3 = pygame.Rect(bug_pos_3.x, bug_pos_3.y, 1.35 * bug_x_size_3, 1.35 * bug_y_size_3)
        bug_hitbox_3 = bug_wrog_3.rect
        bullet_3 = pygame.Rect(bullet_pos_3.x + 5, bullet_pos_3.y + 5, 2 * bullet_r_3, 2 * bullet_r_3)

        # paski zdrowia
        rect_stone_hp = pygame.Rect(player_pos.x, player_pos.y - 20, stone_hp, 10)
        if bug_resp and not ant_dying:
            rect_bug_hp = pygame.Rect(bug_pos.x, bug_pos.y - 10, bug_hp, 10)

        rect_stone_hp_2 = pygame.Rect(player_pos.x, player_pos.y - 20, stone_hp, 10)
        if bug_resp_2 and not spider_dying:
            rect_bug_hp_2 = pygame.Rect(bug_pos_2.x + 10, bug_pos_2.y - 10, bug_hp_2, 10)

        rect_stone_hp_3 = pygame.Rect(player_pos.x, player_pos.y - 20, stone_hp, 10)
        if bug_resp_3 and not fly_dying:
            rect_bug_hp_3 = pygame.Rect(bug_pos_3.x, bug_pos_3.y - 10, bug_hp_3, 10)

        if money_pos_x and money_pos_y:
            money_rect = pygame.Rect(money_pos_x, money_pos_y, 2 * money_r, 2 * money_r)
        if money_pos_x_2 and money_pos_y_2:
            money_rect_2 = pygame.Rect(money_pos_x_2, money_pos_y_2, 2 * money_r_2, 2 * money_r_2)
        if money_pos_x_3 and money_pos_y_3:
            money_rect_3 = pygame.Rect(money_pos_x_3, money_pos_y_3, 2 * money_r_3, 2 * money_r_3)

        # zablokowanie ruchu, gdy bohater znajdzie się na brzegu ekranu
        if player_pos.x <= distance:
            movement_left = False
            if screen_pos_x <= (-1 / 2 * width) - 20:
                screen_left = True
                bug_pos.x += (player_velocity - bug_v_start) * dt
                bug_pos_2.x += (player_velocity - bug_v_start_2) * dt
                bug_pos_3.x += (player_velocity - bug_v_start_3) * dt
                if money_pos_x and money_pos_y:
                    money_pos_x += player_velocity * dt
                if money_pos_x_2 and money_pos_y_2:
                    money_pos_x_2 += player_velocity * dt
                if money_pos_x_3 and money_pos_y_3:
                    money_pos_x_3 += player_velocity * dt
                bullet_pos_2.x += player_velocity * dt
                bullet_pos_3.x += player_velocity * dt
            else:
                screen_left = False
        if player_pos.x >= width - stone_x_size - distance:
            movement_right = False
            if screen_pos_x >= -2300 + (1 / 2 * width) + 20:
                screen_right = True
                bug_pos.x -= (player_velocity - bug_v_start) * dt
                bug_pos_2.x -= (player_velocity - bug_v_start_2) * dt
                bug_pos_3.x -= (player_velocity - bug_v_start_3) * dt
                if money_pos_x and money_pos_y:
                    money_pos_x -= player_velocity * dt
                if money_pos_x_2 and money_pos_y_2:
                    money_pos_x_2 -= player_velocity * dt
                if money_pos_x_3 and money_pos_y_3:
                    money_pos_x_3 -= player_velocity * dt
                bullet_pos_2.x -= player_velocity * dt
                bullet_pos_3.x -= player_velocity * dt
            else:
                screen_right = False
        if player_pos.y <= distance * 1.5:
            movement_up = False
            if screen_pos_y <= (-1 / 2 * height) - 20:
                screen_up = True
                bug_pos.y += (player_velocity - bug_v_start) * dt
                bug_pos_2.y += (player_velocity - bug_v_start_2) * dt
                bug_pos_3.y += (player_velocity - bug_v_start_3) * dt
                if money_pos_x and money_pos_y:
                    money_pos_y += player_velocity * dt
                if money_pos_x_2 and money_pos_y_2:
                    money_pos_y_2 += player_velocity * dt
                if money_pos_x_3 and money_pos_y_3:
                    money_pos_y_3 += player_velocity * dt
                bullet_pos_2.y += player_velocity * dt
                bullet_pos_3.y += player_velocity * dt
            else:
                screen_up = False
        if player_pos.y >= height - stone_y_size - distance * 1.5:
            movement_down = False
            if screen_pos_y >= -2500 + (1 / 2 * height) + 20:
                screen_down = True
                bug_pos.y -= (player_velocity - bug_v_start) * dt
                bug_pos_2.y -= (player_velocity - bug_v_start_2) * dt
                bug_pos_3.y -= (player_velocity - bug_v_start_3) * dt
                if money_pos_x and money_pos_y:
                    money_pos_y -= player_velocity * dt
                if money_pos_x_2 and money_pos_y_2:
                    money_pos_y_2 -= player_velocity * dt
                if money_pos_x_3 and money_pos_y_3:
                    money_pos_y_3 -= player_velocity * dt
                bullet_pos_2.y -= player_velocity * dt
                bullet_pos_3.y -= player_velocity * dt
            else:
                screen_down = False
        if distance < player_pos.x < width - stone_x_size - distance:
            movement_right = True
            movement_left = True
            screen_left = False
            screen_right = False
        if distance < player_pos.y < height - stone_y_size - distance * 1.5:
            movement_up = True
            movement_down = True
            screen_up = False
            screen_down = False

        # ruch postaci (strzałkami lub WASD)
        if not game_starting:
            if (key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]) and movement_up and stone_hp > 0:
                player_pos.y -= player_velocity * dt
                up = True
                down = False
                stone = player_move[iter_pm]
            elif (key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]) and movement_down and stone_hp > 0:
                player_pos.y += player_velocity * dt
                down = True
                up = False
                stone = player_move[iter_pm]
            elif (key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]) and movement_left and stone_hp > 0:
                player_pos.x -= player_velocity * dt
                left = True
                last_left = True
                right = False
                last_right = False
                stone = player_move[iter_pm]
            elif (key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]) and movement_right and stone_hp > 0:
                player_pos.x += player_velocity * dt
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
                if not hitting and stone_hp > 0:
                    stone = player_idle[iter_player_idle]
                    iter_player_idle += 1

        if screen_up:
            bug_up_block = True
            bug_up_block_2 = True
            bug_up_block_3 = True
            screen_pos_y += player_velocity * dt
            stone = player_move[iter_pm]
        else:
            bug_up_block = False
            bug_up_block_2 = False
            bug_up_block_3 = False

        if screen_down:
            bug_down_block = True
            bug_down_block_2 = True
            bug_down_block_3 = True
            screen_pos_y -= player_velocity * dt
            stone = player_move[iter_pm]
        else:
            bug_down_block = False
            bug_down_block_2 = False
            bug_down_block_3 = False

        if screen_left:
            bug_left_block = True
            bug_left_block_2 = True
            bug_left_block_3 = True
            screen_pos_x += player_velocity * dt
            stone = player_move[iter_pm]
        else:
            bug_left_block = False
            bug_left_block_2 = False
            bug_left_block_3 = False

        if screen_right:
            bug_right_block = True
            bug_right_block_2 = True
            bug_right_block_3 = True
            screen_pos_x -= player_velocity * dt
            stone = player_move[iter_pm]
        else:
            bug_right_block = False
            bug_right_block_2 = False
            bug_right_block_3 = False

        if iter_player_idle >= len(player_idle):
            iter_player_idle = 1

        if mouse:
            x, y = pygame.mouse.get_pos()

            if x < player_pos.x + stone_x_size / 2:
                left = True
                last_left = True
                right = False
                last_right = False
            elif x > player_pos.x + stone_x_size / 2:
                left = False
                last_left = False
                right = True
                last_right = True
            else:
                left = False
                last_left = False
                right = False
                last_right = False

        # ruch wroga
        if bug_resp:
            if game_starting:
                bug_v = 1 / 2 * bug_v_start
            else:
                bug_v = bug_v_start

            bug_v_dx = abs(player_pos.x - bug_pos.x)
            bug_v_dy = abs(player_pos.y - bug_pos.y)

            bug_v_y = bug_v * bug_v_dy * math.sqrt(1 / ((bug_v_dx * bug_v_dx) + (bug_v_dy * bug_v_dy)))
            bug_v_x = bug_v_y * (bug_v_dx / bug_v_dy)

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

            if bug_movement_x and not bug_left_block and not bug_right_block and not ant_dying:
                if bug_pos.x - player_pos.x - 10 > mistake_range:
                    bug_v_x = -bug_v_x
                    bug_left = True
                    bug_right = False
                else:
                    bug_left = False
                    bug_right = True
                bug_pos.x += bug_v_x * dt

            if bug_movement_y and not bug_up_block and not bug_down_block and not ant_dying:
                if bug_pos.y - player_pos.y > mistake_range:
                    bug_v_y = -bug_v_y
                    bug_up = True
                    bug_down = False
                else:
                    bug_up = False
                    bug_down = True
                bug_pos.y += bug_v_y * dt

        if bug_movement and not ant_dying:
            bug = ant_move[iter_am]
            iter_am += 1

        if not melee_ant_attack and not melee_ant_attack_animation and not melee_ant_attack_block and not ant_dying:
            if abs(bug_pos.x - player_pos.y) < 250 and abs(bug_pos.y - player_pos.y) < 200:
                if_ant_attack = random.randint(0, 100)
                if if_ant_attack <= 85:
                    melee_ant_attack = True
                    melee_ant_attack_animation = True

        if melee_ant_attack and not melee_ant_attack_block and pygame.Rect.colliderect(rect_melee_ant, rect_stone):
            stone_hp -= ant_attack_dmg
            melee_ant_attack = False
            melee_ant_attack_block = True
            print("attack!")
        else:
            melee_ant_attack = False
            melee_ant_attack_block = True

        if melee_ant_attack_block:
            iter_block_ant_attack += 1

        if iter_block_ant_attack >= 2 * ant_attack_block_time:
            melee_ant_attack_block = False
            iter_block_ant_attack = 1

        if melee_ant_attack_animation:
            bug = ant_attack[iter_ant_attack]
            iter_ant_attack += 1

        if iter_ant_attack >= len(ant_attack):
            iter_ant_attack = 1
            melee_ant_attack_animation = False

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

            if bug_movement_x_2 and not bug_left_block_2 and not bug_right_block_2 and not spider_dying:
                if bug_pos_2.x - player_pos.x - 10 > mistake_range_2:
                    bug_v_x_2 = -bug_v_x_2
                    bug_left_2 = True
                    bug_right_2 = False
                else:
                    bug_left_2 = False
                    bug_right_2 = True
                bug_pos_2.x += bug_v_x_2 * dt

            if bug_movement_y_2 and not bug_up_block and not bug_down_block_2 and not spider_dying:
                if bug_pos_2.y - player_pos.y > mistake_range_2:
                    bug_v_y_2 = -bug_v_y_2
                    bug_up_2 = True
                    bug_down_2 = False
                else:
                    bug_up_2 = False
                    bug_down_2 = True
                bug_pos_2.y += bug_v_y_2 * dt

            # ruch pocisku
            if not bug_attack_start_2 and not bug_attack_2 and not bullet_block_2 and not spider_dying:
                if_attack_2 = random.randint(0, 1000)
                if if_attack_2 <= 8:
                    bug_attack_start_2 = True
                    spider_attack_animation = True

            if bug_attack_cast_2:
                a_2 = 0

            if spider_attack_animation and not spider_dying:
                bug_2 = spider_attack[iter_spider_attack]
                iter_spider_attack += 1
                if iter_spider_attack >= len(spider_attack):
                    iter_spider_attack = 1
                    spider_attack_animation = False

            if bug_attack_start_2 and not spider_attack_animation:
                x_aim_2 = player_pos.x + 30
                y_aim_2 = player_pos.y + 40

                bullet_pos_2.x = bug_pos_2.x + 5
                bullet_pos_2.y = bug_pos_2.y + 5

                predict_2 = 200
                predict_x_2 = 0
                predict_y_2 = 0
                if up:
                    predict_y_2 = predict_2
                elif down:
                    predict_y_2 = -predict_2
                elif right:
                    predict_x_2 = -1.5 * predict_2
                elif left:
                    predict_x_2 = 1.5 * predict_2

                bullet_v_dx_start_2 = bullet_pos_2.x - x_aim_2 + predict_x_2
                bullet_v_dy_start_2 = bullet_pos_2.y - y_aim_2 + predict_y_2

                bug_attack_start_2 = False
                bug_attack_2 = True

        if bug_attack_2:
            bullet_2_img = spider_missile[iter_spider_missile]
            iter_spider_missile += 1
            if iter_spider_missile >= len(spider_missile):
                iter_spider_missile = 1
            screen.blit(bullet_2_img, (bullet_pos_2.x, bullet_pos_2.y))

            mistake_range_bug_2 = 5

            bullet_v_dx_2 = abs(bullet_pos_2.x - x_aim_2)
            bullet_v_dy_2 = abs(bullet_pos_2.y - y_aim_2)

            bullet_v_y_2 = bullet_v_2 * abs(bullet_v_dy_start_2) * math.sqrt(1 / (
                        (abs(bullet_v_dx_start_2) * abs(bullet_v_dx_start_2)) + (
                            abs(bullet_v_dy_start_2) * abs(bullet_v_dy_start_2))))
            bullet_v_x_2 = bullet_v_y_2 * (abs(bullet_v_dx_start_2) / abs(bullet_v_dy_start_2))

            if bullet_v_dx_start_2 > 0:
                bullet_v_x_2 = -bullet_v_x_2

            if bullet_v_dy_start_2 > 0:
                bullet_v_y_2 = -bullet_v_y_2

            if pygame.Rect.colliderect(bullet_2, rect_stone):
                one_hit_bullet_2 = True

            if 0 < bullet_pos_2.x < width and 0 < bullet_pos_2.y < height and (
                    pygame.Rect.colliderect(bullet_2, rect_stone) == False):
                player_velocity = 400
                bullet_pos_2.x += bullet_v_x_2 * dt
                bullet_pos_2.y += bullet_v_y_2 * dt
            elif one_hit_bullet_2:
                player_velocity -= 180
                player_slow = True
                stone_hp -= 2 * ant_attack_dmg
                one_hit_bullet_2 = False
                bug_attack_2 = False
                bullet_block_2 = True
            else:
                bug_attack_2 = False
                bullet_block_2 = True
                player_velocity = 400

        if bug_movement_2 and not spider_dying and not spider_attack_animation:
            bug_2 = spider_move[iter_spider_move]
            iter_spider_move += 1

        if bullet_block_2:
            iter_block_bullet_2 += 1

        if iter_block_bullet_2 > bullet_block_time:
            bullet_block_2 = False
            iter_block_bullet_2 = 1

        if player_slow:
            iter_player_slow += 1
            player_velocity += 1
            if iter_player_slow >= 180:
                iter_player_slow = 1
                player_slow = False

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

            if bug_movement_x_3 and not bug_left_block_3 and not bug_right_block_3 and not fly_dying:
                if bug_pos_3.x - player_pos.x - 10 > mistake_range_3:
                    bug_v_x_3 = -bug_v_x_3
                    bug_left_3 = True
                    bug_right_3 = False
                else:
                    bug_left_3 = False
                    bug_right_3 = True
                bug_pos_3.x += bug_v_x_3 * dt

            if bug_movement_y_3 and not bug_up_block_3 and not bug_down_block_3 and not fly_dying:
                if bug_pos_3.y - player_pos.y > mistake_range_3:
                    bug_v_y_3 = -bug_v_y_3
                    bug_up_3 = True
                    bug_down_3 = False
                else:
                    bug_up_3 = False
                    bug_down_3 = True
                bug_pos_3.y += bug_v_y_3 * dt

            # ruch pocisku
            if not bug_attack_start_3 and not bug_attack_3 and not bullet_block_3 and not fly_dying:
                if_attack_3 = random.randint(0, 1000)
                if if_attack_3 <= 12:
                    bug_attack_start_3 = True

            if bug_attack_cast_3:
                a_3 = 0

            if bug_attack_start_3:
                x_aim_3 = player_pos.x + 30
                y_aim_3 = player_pos.y + 40

                bullet_pos_3.x = bug_pos_3.x + 5
                bullet_pos_3.y = bug_pos_3.y + 5

                predict_3 = 200
                predict_x_3 = 0
                predict_y_3 = 0
                if up:
                    predict_y_3 = predict_3
                elif down:
                    predict_y_3 = -predict_3
                elif right:
                    predict_x_3 = -1.5 * predict_3
                elif left:
                    predict_x_3 = 1.5 * predict_3

                bullet_v_dx_start_3 = bullet_pos_3.x - x_aim_3 + predict_x_3
                bullet_v_dy_start_3 = bullet_pos_3.y - y_aim_3 + predict_y_3

                bug_attack_start_3 = False
                bug_attack_3 = True

        if bug_attack_3:
            mistake_range_bug_3 = 5

            bullet_v_dx_3 = abs(bullet_pos_3.x - x_aim_3)
            bullet_v_dy_3 = abs(bullet_pos_3.y - y_aim_3)

            bullet_v_y_3 = bullet_v_3 * abs(bullet_v_dy_start_3) * math.sqrt(1 / (
                        (abs(bullet_v_dx_start_3) * abs(bullet_v_dx_start_3)) + (
                            abs(bullet_v_dy_start_3) * abs(bullet_v_dy_start_3))))
            bullet_v_x_3 = bullet_v_y_3 * (abs(bullet_v_dx_start_3) / abs(bullet_v_dy_start_3))

            if bullet_v_dx_start_3 > 0:
                bullet_v_x_3 = -bullet_v_x_3

            if bullet_v_dy_start_3 > 0:
                bullet_v_y_3 = -bullet_v_y_3

            if pygame.Rect.colliderect(bullet_3, rect_stone):
                one_hit_bullet_3 = True

            if 0 < bullet_pos_3.x < width and 0 < bullet_pos_3.y < height and (
                    pygame.Rect.colliderect(bullet_3, rect_stone) == False):
                bullet_pos_3.x += bullet_v_x_3 * dt
                bullet_pos_3.y += bullet_v_y_3 * dt
            elif one_hit_bullet_3:
                stone_hp -= ant_attack_dmg
                one_hit_bullet_3 = False
                bug_attack_3 = False
                bullet_block_3 = True
            else:
                bug_attack_3 = False
                bullet_block_3 = True

        if bug_movement_3 and not fly_dying:
            bug_3 = fly_move[iter_fly_move]
            iter_fly_move += 1

        if bullet_block_3:
            iter_block_bullet_3 += 1

        if iter_block_bullet_3 > bullet_block_time:
            bullet_block_3 = False
            iter_block_bullet_3 = 1

        if iter_am >= len(ant_move):
            iter_am = 1

        if iter_am_2 >= len(ant_move):
            iter_am_2 = 1

        if iter_fly_move >= len(fly_move):
            iter_fly_move = 1

        if iter_am_3 >= len(ant_move):
            iter_am_3 = 1

        if iter_spider_move >= len(spider_move):
            iter_spider_move = 1

        # zwiększenie wartości iteratora za każdym razem, gdy trwa atak mieczem (pozwalające kontynuować animację)
        if hitting and stone_hp > 0:
            iter_player_attack += 1

        # zakończenie ruchu mieczem - funkcja odpowiedzialna za atak przyjmuje wartość fałsz, a iterator wraca do wartości początkowej
        if iter_player_attack >= len(player_attack):
            iter_player_attack = 0
            hitting = False

        if (movement_up or movement_left or movement_down or movement_right) and not attack_movement_block:
            iter_pm += 1

        if iter_pm >= len(player_move):
            iter_pm = 1

        # animacja
        if hitting and stone_hp > 0:
            stone = player_attack[iter_player_attack]
            attack_movement_block = True
        else:
            attack_movement_block = False

        if left:
            stone = pygame.transform.flip(stone, True, False)
            screen.blit(stone, (player_pos.x, player_pos.y))
        else:
            screen.blit(stone, (player_pos.x, player_pos.y))

        if not bug_resp_2:
            bug_resp_2 = (random.randint(0, 100000 - chance_of_resp_ranged_ant_1) <= 3)

        if bug_resp_2:
            if bug_right_2:
                bug_2 = pygame.transform.flip(bug_2, True, False)
                screen.blit(bug_2, (bug_pos_2.x, bug_pos_2.y))
            else:
                screen.blit(bug_2, (bug_pos_2.x, bug_pos_2.y))

        if not bug_resp_3:
            bug_resp_3 = (random.randint(0, 100000 - chance_of_resp_ranged_ant_2) <= 3)

        if bug_resp_3:
            if bug_right_3:
                bug_3 = pygame.transform.flip(bug_3, True, False)
                screen.blit(bug_3, (bug_pos_3.x, bug_pos_3.y))
            else:
                screen.blit(bug_3, (bug_pos_3.x, bug_pos_3.y))

        if not bug_resp:
            bug_resp = (random.randint(0, 100000 - chance_of_resp_melee_ant) <= 3)

        if bug_resp:
            if bug_right:
                bug = pygame.transform.flip(bug, True, False)
                screen.blit(bug, (bug_pos.x, bug_pos.y))
            else:
                screen.blit(bug, (bug_pos.x, bug_pos.y))

        pygame.draw.rect(screen, (0, 128, 0), rect_stone_hp)

        if bug_resp:
            pygame.draw.rect(screen, (0, 0, 255, 0), rect_bug_hp)

        if bug_resp_2:
            pygame.draw.rect(screen, (255, 255, 255, 0), rect_bug_hp_2)

        if bug_resp_3:
            pygame.draw.rect(screen, (255, 0, 0, 0), rect_bug_hp_3)

        if pygame.Rect.colliderect(rect_sword, rect_bug) and one_hit_stone:
            bug_hp -= player_dmg
            one_hit_stone = False
        if pygame.Rect.colliderect(rect_sword, rect_bug_2) and one_hit_stone:
            bug_hp_2 -= player_dmg
            one_hit_stone = False
        if pygame.Rect.colliderect(rect_sword, rect_bug_3) and one_hit_stone:
            bug_hp_3 -= player_dmg
            one_hit_stone = False

        if pygame.Rect.colliderect(rect_bug, rect_stone) and bug_resp:
            stone_hp -= ant_attack_dmg / 15
        if pygame.Rect.colliderect(rect_bug_3, rect_stone) and bug_resp_3:
            stone_hp -= ant_attack_dmg / 15

        if bug_attack_3:
            pygame.draw.circle(screen, (40, 40, 0), (bullet_pos_3.x + bullet_r_3, bullet_pos_3.y + bullet_r_3),
                               bullet_r_3)

        # zatrzymanie gry, gdy zdrowie kamienia lub przeciwnika spadnie do zera
        # - gdy kamień zginie, wyświetla się informacja o zwycięstwie (w konsoli)
        # - gdy zginie przeciwnik, wyświetla się informacja o porażce (również w konsoli)

        if bug_hp <= 0 or bug_hp_2 <= 0 or bug_hp_3 <= 0:
            if_bonus = True
            bonus_time = True

        if bonus_time:
            iter_bonus_time += 1

        if iter_bonus_time >= 300:
            bonus_time = False
            iter_bonus_time = 1

        if if_bonus and bonus_time:
            bonus = random.randint(1, 400)
            if bonus <= 100:
                print("hp bonus")
                stone_hp += 30
            elif bonus <= 200:
                print("movement speed bonus")
                player_velocity *= 1.5
            elif bonus <= 300:
                print("armor bonus")
                ant_attack_dmg /= 2.4
            else:
                print("attack damage bonus")
                player_dmg *= 1.8
            if_bonus = False

        if not bonus_time:
            player_velocity = 400
            ant_attack_dmg = 15
            player_dmg = 10

        if bug_hp <= 0:
            licznik_mrowek += 1
            ant_dying = True
            pygame.time.wait(50)
            coin_creating_1 = True
            money_existence = True
            money_pos_x = bug_pos.x - 8
            money_pos_y = bug_pos.y - 6
            bug_hp = 100

        if ant_dying:
            bug = ant_death[iter_ant_death]
            iter_ant_death += 1
            if iter_ant_death >= len(ant_death):
                iter_ant_death = 1
                bug_x_rng = random.randint(0, width - 320)
                bug_y_rng = random.randint(0, height - 180)
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
                bug_resp = False
                ant_dying = False

        if coin_creating_1:
            coin_1 = Coin(bug_pos.x, bug_pos.y)

        if bug_hp_2 <= 0:
            licznik_mrowek += 1
            spider_dying = True
            pygame.time.wait(50)
            coin_creating_2 = True
            money_existence_2 = True
            money_pos_x_2 = bug_pos_2.x
            money_pos_y_2 = bug_pos_2.y
            bug_hp_2 = 180

        if spider_dying:
            bug_2 = spider_death[iter_spider_death]
            iter_spider_death += 1
            if iter_spider_death >= len(spider_death):
                iter_spider_death = 1
                bug_x_rng_2 = random.randint(0, width - 320)
                bug_y_rng_2 = random.randint(0, height - 180)
                if bug_x_rng_2 <= player_pos.x - 160:
                    bug_pos_2.x = bug_x_rng_2
                else:
                    bug_pos_2.x = bug_x_rng_2 + 320

                if bug_y_rng <= player_pos.y - 90:
                    bug_pos_2.y = bug_y_rng_2
                else:
                    bug_pos_2.y = bug_y_rng_2 + 180
                bug_2 = bug_wrog_2.create_surface()
                bug_2 = pygame.transform.scale(bug_2, (bug_x_size_2, bug_y_size_2))
                bug_resp_2 = False
                spider_dying = False

        if coin_creating_2:
            coin_2 = Coin(bug_pos_2.x, bug_pos_2.y)

        if bug_hp_3 <= 0:
            licznik_mrowek += 1
            fly_dying = True
            pygame.time.wait(50)
            coin_creating_3 = True
            money_existence_3 = True
            money_pos_x_3 = bug_pos_3.x - 15
            money_pos_y_3 = bug_pos_3.y - 15
            bug_hp_3 = 40

        if fly_dying:
            bug_3 = fly_death[iter_fly_death]
            iter_fly_death += 1
            if iter_fly_death >= len(fly_death):
                iter_fly_death = 1
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
                bug_resp_3 = False
                fly_dying = False

        if coin_creating_3:
            coin_3 = Coin(bug_pos_3.x, bug_pos_3.y)

        """
        if coin_1 is not None:
            coin_1.coin_draw()
            coin_1.coin_anim()
            coin_1.coin_collect(rect_stone)
            if coin_1.coin_collect(rect_stone):
                coin_creating_1 = False

        if coin_2 is not None:
            coin_2.coin_draw()
            coin_2.coin_anim()
            coin_2.coin_collect(rect_stone)
            if coin_2.coin_collect(rect_stone):
                coin_creating_2 = False

        if coin_3 is not None:
            coin_3.coin_draw()
            coin_3.coin_anim()
            coin_3.coin_collect(rect_stone)
            if coin_3.coin_collect(rect_stone):
                coin_creating_3 = False
        """

        if money_existence:
            screen.blit(money, (money_pos_x, money_pos_y))
            money = coin_animation[iter_money]
            iter_money += 1
            if iter_money >= len(coin_animation):
                iter_money = 1
            if pygame.Rect.colliderect(rect_stone, money_rect):
                money_counter += 1
                print("Money:", money_counter)
                stone_hp += 10
                money_existence = False
            if pygame.Rect.colliderect(money_rect, rect_bug) or pygame.Rect.colliderect(money_rect,
                                                                                        rect_bug_2) or pygame.Rect.colliderect(
                    money_rect, rect_bug_3):
                money_existence = False

        if money_existence_2:
            screen.blit(money_2, (money_pos_x_2, money_pos_y_2))
            money_2 = coin_animation[iter_money_2]
            iter_money_2 += 1
            if iter_money_2 >= len(coin_animation):
                iter_money_2 = 1
            if pygame.Rect.colliderect(rect_stone, money_rect_2):
                money_counter += 1
                print("Money:", money_counter)
                stone_hp += 25
                money_existence_2 = False
            if pygame.Rect.colliderect(money_rect_2, rect_bug) or pygame.Rect.colliderect(money_rect_2,
                                                                                          rect_bug_2) or pygame.Rect.colliderect(
                    money_rect_2, rect_bug_3):
                money_existence_2 = False

        if money_existence_3:
            screen.blit(money_3, (money_pos_x_3, money_pos_y_3))
            money_3 = coin_animation[iter_money_3]
            iter_money_3 += 1
            if iter_money_3 >= len(coin_animation):
                iter_money_3 = 1
            if pygame.Rect.colliderect(rect_stone, money_rect_3):
                money_counter += 1
                print("Money:", money_counter)
                stone_hp += 4
                money_existence_3 = False
            if pygame.Rect.colliderect(money_rect_3, rect_bug) or pygame.Rect.colliderect(money_rect_3,
                                                                                          rect_bug_2) or pygame.Rect.colliderect(
                    money_rect_3, rect_bug_3):
                money_existence_3 = False

        if money_counter >= 10 and not bug_resp and not bug_resp_2 and not bug_resp_3:
            print("Congratulations. You won")
            program_running = False

        if music_start == False and stone_hp < 1:
            music_start = True

        if stone_hp <= 0:
            player_dying = True
            if music_start and not music_one_time:
                music_one_time = True
                pygame.mixer.music.unload()
                pygame.mixer.music.load('data/sfx/explosion.mp3')
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(1)
                pygame.time.wait(900)
                music_start = False
            stone = player_death[iter_player_death]
            iter_player_death += 1
            if iter_player_death >= len(player_death):
                game_end = True
                iter_player_death = 1

        screen.blit(trees, (screen_pos_x, screen_pos_y))

        # poniżej zakomentowane metody pozwalające pokolorować hitboxy poszczególnych obiektów, w celu sprawdzenia sposobu ich zachowania się

        """
        pygame.draw.rect(screen, (0, 0, 0), rect_stone)
        pygame.draw.rect(screen, (0, 0, 255), rect_sword)    
        pygame.draw.rect(screen, (0, 255, 0), rect_bug)
        pygame.draw.rect(screen, (0, 255, 0), rect_bug_2)
        pygame.draw.rect(screen, (0, 255, 0), rect_bug_3)
        pygame.draw.rect(screen, (0, 255, 0), bullet_2)
        pygame.draw.rect(screen, (0, 255, 0), rect_melee_ant)
        """

        # update wyświetlanych na ekranie obiektów przy każdej iteracji pętli
        pygame.display.update()

        # zmienna pomocnicza niezbędna przy mechanice sterowania klawiszami
        dt = clock.tick(60) / 1000

        if game_end:
            print("Game over")
            program_running = False

def quit_game():
    pygame.quit()
    sys.exit()

def back_to_menu():
    global settings_running
    settings_running = False

def open_settings():
    volume_rect = None
    global settings_running
    settings_running = True
    volume = 50

    while settings_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    settings_running = False
            elif event.type == MOUSEBUTTONDOWN:
                if volume_rect.collidepoint(event.pos):
                    volume = (event.pos[0] - volume_rect.x) / volume_rect.width * 100

        screen.fill(GRAY)

        # Rysowanie paska głośności
        volume_rect = pygame.Rect(100, 100, 300, 40)
        pygame.draw.rect(screen, BLUE, volume_rect)
        handle_rect = pygame.Rect(volume_rect.x + volume * (volume_rect.width / 100) - 10, volume_rect.y, 20, 40)
        pygame.draw.rect(screen, HOVER_COLOR if handle_rect.collidepoint(pygame.mouse.get_pos()) else BLACK, handle_rect)
        volume_label = font.render(f"Głośność: {int(volume)}", True, BLACK)
        screen.blit(volume_label, (volume_rect.x, volume_rect.y - 40))

        # Przycisk powrotu do menu
        back_button_rect = pygame.Rect(100, 300, 200, 50)
        draw_button("Powrót do menu", back_button_rect, BLUE, HOVER_COLOR, back_to_menu)

        pygame.display.flip()

def open_stats():
    print("Statystyki otwarte!")

# Funkcja do rysowania przycisków
def draw_button(text, rect, color, hover_color, action=None):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, rect)
        if mouse_click[0] and action:
            action()
    else:
        pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

# Główna pętla gry
running = True
while running:
    screen.blit(background_image, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # Względne pozycje i stany przycisków
    buttons = [
        (button_play_image, button_play_hovered_image, (screen_width * 0.636, screen_height * 0.511), start_game),
        (button_settings_image, button_settings_hovered_image, (screen_width * 0.672, screen_height * 0.632), open_settings),
        (button_stats_image, button_stats_hovered_image, (screen_width * 0.63, screen_height * 0.78), open_stats),
        (button_quit_image, button_quit_hovered_image, (screen_width * 0.17, screen_height * 0.82), quit_game),
    ]

    for button, button_hovered, pos, action in buttons:
        rect = button.get_rect(center=pos)
        if rect.collidepoint(mouse_pos):
            screen.blit(button_hovered, rect.topleft)
            if mouse_click[0]:
                action()
        else:
            screen.blit(button, rect.topleft)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
