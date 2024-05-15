# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()

height = 720
width = 1280
screen = pygame.display.set_mode((width, height))


#informacje o mieczu
sword_x_size = 70
sword_y_size = 70

sword = pygame.image.load("miecz.jpg")
sword = pygame.transform.scale(sword, (sword_x_size, sword_y_size))

#animacja miecza
sword_sprite_1 = []
for i in range(5):
    sword_sprite_1.append(pygame.transform.rotate(sword, -10*i))

sword_sprite_2 = []
for i in range(2):
    sword_sprite_2.append(pygame.transform.rotate(sword, -25*(1-i)))

sword_sprite = sword_sprite_1 + [pygame.transform.rotate(sword, -50)] + sword_sprite_2


#informacje o kamieniu
stone_x_size = 81
stone_y_size = 54

stone = pygame.image.load('kamien.png')
stone = pygame.transform.scale(stone, (stone_x_size, stone_y_size))

#informacje o chrząszczu
bug_x_size = 75
bug_y_size = 50

bug = pygame.image.load('chrzaszcz.png')
bug = pygame.transform.scale(bug, (bug_x_size, bug_y_size))
bug_x_rand = random.randint(60, 1220)
bug_y_rand = random.randint(40, 680)


#pozycja gracza
player_pos = pygame.Vector2((screen.get_width() / 2) - stone_x_size/2, (screen.get_height() / 2) - stone_y_size/2)

#zegar
clock = pygame.time.Clock()
dt = 0

#iterator
iter = 0

#funkcje logiczne
program_running = True
hitting = False

movement_left = True
movement_up = True
movement_right = True
movement_down = True

while program_running:
    clock.tick(60)

    #wyłączanie programu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hitting = True
                one_hit_stone = True

    key_pressed = pygame.key.get_pressed()

    rect_sword = pygame.Rect(player_pos.x + stone_x_size, player_pos.y - sword_y_size + (4 * stone_y_size / 5), 1.1*sword_x_size, 1.1*sword_y_size)
    rect_stone = pygame.Rect(player_pos.x, player_pos.y + 0.1 * stone_y_size, 1.1 * stone_x_size, stone_y_size)
    rect_bug = pygame.Rect(bug_x_rand + 0.1 * bug_x_size, bug_y_rand + 0.2 * bug_y_size, 0.8*bug_x_size, 0.8*bug_y_size)

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

    if (key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]) and movement_up:
        player_pos.y -= 400 * dt
    if (key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]) and movement_down:
        player_pos.y += 400 * dt
    if (key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]) and movement_left:
        player_pos.x -= 400 * dt
    if (key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]) and movement_right:
        player_pos.x += 400 * dt

    if hitting:
        iter += 1

    if iter >= len(sword_sprite):
        iter = 0
        hitting = False

    sword = sword_sprite[iter]

    sword = pygame.transform.scale(sword, (sword_x_size, sword_y_size))
    screen.blit(sword, (player_pos.x + stone_x_size, player_pos.y - stone_y_size/2))

    screen.blit(stone, (player_pos.x, player_pos.y))

    screen.blit(bug, (bug_x_rand, bug_y_rand))

    if pygame.Rect.colliderect(rect_sword, rect_bug):
        print("Congratulations. You won")
        program_running = False
    if pygame.Rect.colliderect(rect_bug, rect_stone):
        print("Game over")
        program_running = False


    #pygame.draw.rect(screen, (0, 0, 0), rect_stone)
    #pygame.draw.rect(screen, (0, 0, 255), rect_sword)
    #pygame.draw.rect(screen, (0, 255, 0), rect_bug)

    pygame.display.update()

    screen.fill("white")

    dt = clock.tick(60)/1000
