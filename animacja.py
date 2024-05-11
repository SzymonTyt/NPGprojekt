# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

height = 720
width = 1280

screen = pygame.display.set_mode((width, height))


#informacje o mieczu
sword_x_size = 70
sword_y_size = 70

sword = pygame.image.load("Iron_Sword_JE2_BE2.webp")
sword = pygame.transform.scale(sword, (sword_x_size, sword_y_size))


#animacja
sword_sprite_1 = []
for i in range(5):
    sword_sprite_1.append(pygame.transform.rotate(sword, -10*i))

sword_sprite_2 = []
for i in range(2):
    sword_sprite_2.append(pygame.transform.rotate(sword, -25*(1-i)))

sword_sprite = sword_sprite_1 + [pygame.transform.rotate(sword, -50)] + sword_sprite_2


#kamień

stone_x_size = 60
stone_y_size = 40

stone = pygame.image.load('kamien.png')
stone = pygame.transform.scale(stone, (stone_x_size, stone_y_size))


#pozycja gracza
player_pos = pygame.Vector2((screen.get_width() / 2) - stone_x_size/2, (screen.get_height() / 2) - stone_y_size/2)


#zegar
clock = pygame.time.Clock()

#reszta
iter = 0
running = True
hitting = False
dt = 0


#prostokąty
rect_stone = stone.get_rect()
rect_sword = sword.get_rect()


while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                hitting = False
                iter = 0

    key_pressed = pygame.key.get_pressed()


    if player_pos.x > 0 and player_pos.y > 0 and player_pos.x < (width - stone_x_size - sword_x_size) and player_pos.y < (height - stone_y_size):
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            player_pos.y -= 300 * dt
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            player_pos.y += 300 * dt
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            player_pos.x -= 300 * dt
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            player_pos.x += 300 * dt
    elif player_pos.x <= 0:
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            player_pos.y -= 300 * dt
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            player_pos.y += 300 * dt
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            player_pos.x += 300 * dt
    elif player_pos.x >= (width - stone_x_size - sword_x_size):
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            player_pos.y -= 300 * dt
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            player_pos.y += 300 * dt
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            player_pos.x -= 300 * dt
    elif player_pos.y <= 0:
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            player_pos.y += 300 * dt
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            player_pos.x -= 300 * dt
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            player_pos.x += 300 * dt
    elif player_pos.y >= (height - stone_y_size):
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            player_pos.y -= 300 * dt
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            player_pos.x -= 300 * dt
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            player_pos.x += 300 * dt
    elif player_pos.y >= (height - stone_y_size) and player_pos.x >= (width - stone_x_size - sword_x_size):
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            player_pos.x -= 300 * dt
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            player_pos.y -= 300 * dt
    elif player_pos.y >= (height - stone_y_size) and player_pos.x <= 0:
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            player_pos.y -= 300 * dt
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            player_pos.x += 300 * dt
    elif player_pos.y <= 0 and player_pos.x >= (width - stone_x_size - sword_x_size):
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            player_pos.x -= 300 * dt
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            player_pos.y += 300 * dt
    elif player_pos.y <= 0 and player_pos.x <= 0:
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            player_pos.y += 300 * dt
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            player_pos.x += 300 * dt

    if key_pressed[pygame.K_SPACE]:
        hitting = True

    if hitting:
        iter += 1

    if iter >= len(sword_sprite):
        iter = 0

    sword = sword_sprite[iter]

    sword = pygame.transform.scale(sword, (sword_x_size, sword_y_size))

    screen.blit(sword, (player_pos.x + stone_x_size, player_pos.y - stone_y_size/2))

    screen.blit(stone, (player_pos.x, player_pos.y))

    pygame.display.update()

    screen.fill("white")

    dt = clock.tick(60)/1000
