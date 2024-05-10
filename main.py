# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

height = 720
width = 1280


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#kamień

stone_x_size = 60
stone_y_size = 40

stone = pygame.image.load('kamien.png')
stone = pygame.transform.scale(stone, (stone_x_size, stone_y_size))


#information about sword
sword_x_size = 60
sword_y_size = 60
sword_holder_x_size = sword_x_size/8
sword_holder_y_size = sword_y_size/8

sword = pygame.image.load('Iron_Sword_JE2_BE2.webp')
sword = pygame.transform.scale(sword, (sword_x_size, sword_y_size))


def swordSwing():
    transformed_sword = pygame.transform.rotate(sword, -90)
    screen.blit(transformed_sword, (player_pos.x + 10, player_pos.y - 5 - sword_holder_y_size))
    pygame.display.update()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


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

    #f key_pressed[pygame.K_SPACE]:
       # swordSwing()

    screen.blit(sword, (player_pos.x + stone_x_size, player_pos.y - stone_y_size / 2))

    screen.blit(stone, (player_pos.x, player_pos.y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
