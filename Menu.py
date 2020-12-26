import pygame
import random
import sys
import algorithms
import SortDisplay

pygame.init()

HEIGHT = 512
WIDTH = 1024
display = pygame.display.set_mode((WIDTH, HEIGHT))

STATUS = 'Sorting ...'

class button():
	def __init__(self, x, y, text = ''):
		self.color = (204,255,255)
		self.x = x
		self.width = 250
		self.y = y
		self.height = 50
		self.text = text

	def draw(self, window, outline = None):
		if outline:
			pygame.draw.rect(window, outline, (self.x-2, self.y - 2, self.width + 4, self.height + 4), 0)
		pygame.draw.rect(window, self.color, (self.x, self.y , self.width, self.height), 0)

		if self.text != '':
			font = pygame.font.SysFont('Arial', 30)
			text = font.render(self.text, 1, (0,0,0))
			window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	def isOver(self, pos):
	 	if pos[0] > self.x and pos[0] < self.x + self.width:
	 		if pos[1] > self.y and pos[1] < self.y + self.height:
	 			return True
	 	return False

def Menu(display):
	display.fill((96,96,96))
	isOverButtonColor = (192,192,192)
	defaultButtonColor = (204,255,255)
	main_font = pygame.font.SysFont('Arial', 30)

	LeftSideCoordenates = [130, [i for i in range(45, 60*6, 60)]]
	RightSideCoordenates = [600, [i for i in range(50, 60*6, 60)]]

	algorithmType_label = main_font.render(f'Ordenar: ', 1, (0,0,0))
	display.blit(algorithmType_label, (660, RightSideCoordenates[1][0]))

	algorithm_label = main_font.render(f'Seleccione el algoritmo:', 1, (0,0,0))
	display.blit(algorithm_label, (135,LeftSideCoordenates[1][0]))

	SelectionSort = button(LeftSideCoordenates[0], LeftSideCoordenates[1][1], algorithms.SelectionSort().name)
	BubbleSort = button(LeftSideCoordenates[0], LeftSideCoordenates[1][2], algorithms.BubbleSort().name)
	InsertionSort = button(LeftSideCoordenates[0], LeftSideCoordenates[1][3], algorithms.InsertionSort().name)
	CocktailSort = button(LeftSideCoordenates[0], LeftSideCoordenates[1][4], algorithms.CocktailSort().name)
	QuickSort = button(LeftSideCoordenates[0], LeftSideCoordenates[1][5], algorithms.QuickSort().name)

	BotonColores = button(RightSideCoordenates[0], RightSideCoordenates[1][1], 'Colores')
	BotonBarrasAnchas = button(RightSideCoordenates[0], RightSideCoordenates[1][2], 'Barras Anchas')
	BotonBarrasDelgadas = button(RightSideCoordenates[0], RightSideCoordenates[1][3], 'Barras Delgadas')

	RunButton = button(RightSideCoordenates[0], RightSideCoordenates[1][5], 'RUN')
	
	RunButton.height = 100
	RunButton.color = (153, 153, 153)

	while True:
		pygame.display.update()
		SelectionSort.draw(display, (0,0,0))
		BubbleSort.draw(display, (0,0,0))
		InsertionSort.draw(display, (0,0,0))
		CocktailSort.draw(display, (0,0,0))
		QuickSort.draw(display, (0,0,0))
		BotonColores.draw(display, (0,0,0))
		BotonBarrasAnchas.draw(display, (0,0,0))
		BotonBarrasDelgadas.draw(display, (0,0,0))
		RunButton.draw(display, (0,0,0))
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:

				if SelectionSort.isOver(pos):

					SelectionSort.color = (204, 99, 81)
					QuickSort.color = CocktailSort.color = InsertionSort.color = BubbleSort.color = defaultButtonColor
					algorithms.toDo['Algoritmo'] = algorithms.SelectionSort()

				elif BubbleSort.isOver(pos):

					BubbleSort.color = (204, 99, 81)
					QuickSort.color = SelectionSort.color = CocktailSort.color = InsertionSort.color =  defaultButtonColor
					algorithms.toDo['Algoritmo'] = algorithms.BubbleSort()

				elif InsertionSort.isOver(pos):

					InsertionSort.color = (204, 99, 81)
					QuickSort.color = SelectionSort.color = CocktailSort.color = BubbleSort.color = defaultButtonColor
					algorithms.toDo['Algoritmo'] = algorithms.InsertionSort()

				elif CocktailSort.isOver(pos):

					CocktailSort.color = (204, 99, 81)
					QuickSort.color = SelectionSort.color = InsertionSort.color = BubbleSort.color = defaultButtonColor
					algorithms.toDo['Algoritmo'] = algorithms.CocktailSort()

				elif QuickSort.isOver(pos):

					QuickSort.color = (204, 99, 81)
					SelectionSort.color = CocktailSort.color = InsertionSort.color = BubbleSort.color = defaultButtonColor
					algorithms.toDo['Algoritmo'] = algorithms.QuickSort()

				elif BotonColores.isOver(pos):

					BotonColores.color = (204, 99, 81)
					BotonBarrasDelgadas.color = defaultButtonColor
					BotonBarrasAnchas.color = defaultButtonColor
					algorithms.toDo['Algoritmo'].number = 512
					algorithms.toDo['Tipo'] = 0

				elif BotonBarrasAnchas.isOver(pos):
					BotonBarrasAnchas.color = (204, 99, 81)
					BotonColores.color = defaultButtonColor
					BotonBarrasDelgadas.color = defaultButtonColor
					algorithms.toDo['Algoritmo'].number = 64
					algorithms.toDo['Tipo'] = 1

				elif BotonBarrasDelgadas.isOver(pos):
					BotonBarrasDelgadas.color = (204, 99, 81)
					BotonColores.color = defaultButtonColor
					BotonBarrasAnchas.color = defaultButtonColor
					algorithms.toDo['Algoritmo'].number = 512
					algorithms.toDo['Tipo'] = 2

				elif RunButton.isOver(pos):
					return

def main():
	Menu(display)
	algorithms.toDo['Algoritmo'].GenerateArr()
	time = algorithms.toDo['Algoritmo'].run()[1]
	STATUS = 'Sorted!'
	SortDisplay.FinishedSort(time)

if __name__ == "__main__":

	main()
