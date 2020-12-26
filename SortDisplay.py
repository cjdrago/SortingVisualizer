import pygame
import algorithms
import os
import time
import sys
import Menu

def updateScreen(algoritmo, swap1 = None, swap2 = None, display = Menu.display):

	main_font = pygame.font.SysFont('comicsans', 38)
	if(algorithms.toDo['Tipo'] != 0):
		display.fill(pygame.Color("#4e60ab"))
	
	algoritmo.Choose_Sort_Type(swap1, swap2, Menu.display)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	
	algorithm_label = main_font.render(f'Algoritmo: {algoritmo.name}', 1, (255,255,255))
	time_label = main_font.render('Time: {:.2f}'.format(time.time() - algoritmo.start), 2, (255,255,255))
	status_label = main_font.render(f'Status: {Menu.STATUS}', 1, (255,255,255))

	display.blit(algorithm_label, (10,10))
	display.blit(status_label, (10,40))
	display.blit(time_label, (10,65))
	
	pygame.display.set_caption(f"Sorting Visualizer")
	pygame.display.update()

def FinishedSort(time, display = Menu.display):
	time = format(time, '.2f')
	main_font = pygame.font.SysFont('comicsans', 38)
	if(algorithms.toDo['Tipo'] != 0):
		status_label = main_font.render(f'Status: Sorted!!    ', 1, (255,255,255),  pygame.Color("#4e60ab"))
	else:
		status_label = main_font.render(f'Status: Sorted!!    ', 1, (255,255,255))
	
	display.blit(status_label, (10,40))
	
	RunAgain = Menu.button(370, 220, 'Run Again')
	RunAgain.draw(display, (0,0,0))
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			pos = pygame.mouse.get_pos()

			if event.type == pygame.MOUSEBUTTONDOWN:

				if RunAgain.isOver(pos):
					RunAgain.color = (204, 99, 81)
					Menu.main()

		pygame.display.update()


