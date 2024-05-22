import pygame
def pause_menu():
	pygame.draw.rect(surface, (127, 127, 127, 150), [0,0, WIDTH, HEIGHT])
	pygame.draw.rect(surface, 'gray' , [200,150, 600, 50],0, 10)
	resume = pygame.draw.rect(surface, 'black' , [200,220, 280, 50],0, 10)
	exit= pygame.draw.rect(surface, 'black' , [520,220, 280, 50],0, 10)
	surface.blit(font.render('Pause', True, 'white'), (220,160))
	surface.blit(font.render('Resume', True, 'white'), (220,230))
	surface.blit(font.render('Exit', True, 'white'), (540,230))
	screen.blit(surface, (0,0))