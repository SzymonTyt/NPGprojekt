
#funkcja która po wywołaniu odpali raz dźwięk
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()



#za filepath w tym kodzie trzeba podać ścieżkę do pliku z muzyką
if not game_starting:
    if (key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]) and movement_up:
        player_pos.y -= 400 * dt
        play_music(file_path)
        up = True
        down = False
        stone = player_move[iter_pm]
    elif (key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]) and movement_down:
        player_pos.y += 400 * dt
        play_music(file_path)
        down = True
        up = False
        stone = player_move[iter_pm]
    elif (key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]) and movement_left:
        player_pos.x -= 400 * dt
        play_music(file_path)
        left = True
        last_left = True
        right = False
        last_right = False
        stone = player_move[iter_pm]
    elif (key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]) and movement_right:
        player_pos.x += 400 * dt
        play_music(file_path)
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

    if x < player_pos.x:
        play_music(file_path)
        left = True
        last_left = True
        right = False
        last_right = False
    elif x > player_pos.x:
        play_music(file_path)
        left = False
        last_left = False
        right = True
        last_right = True
    else:
        play_music(file_path)
        left = False
        last_left = False
        right = False
        last_right = False