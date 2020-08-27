import random
import time
import pygame

toDo = {
		 "Algoritmo": None,
		 "Tipo": None
		}

class algoritmos():
	def __init__(self, name):
		self.number = None
		self.arr = None
		self.name = name

	def GenerateArr(self):
		self.arr = random.sample(range(self.number), self.number)

	def showSwap(self, swap1=None, swap2=None):
		import SortDisplay
		SortDisplay.updateScreen(self, swap1, swap2)

	def run(self):
		self.start = time.time()
		self.sort()
		time_elapsed = time.time() - self.start
		return self.arr, time_elapsed

	def Choose_Sort_Type(self, Swap_Value_1 , Swap_Value_2, display):
		if toDo['Tipo'] == 1:
			self.SortWideBars(Swap_Value_1, Swap_Value_2, display)

		elif toDo['Tipo'] == 2:
			self.SortThinBars(Swap_Value_1, Swap_Value_2, display)

		else:
			self.SortColours(display)

	def SortWideBars(self, Swap_Value_1, Swap_Value_2, display):
		WIDTH, HEIGHT = pygame.display.get_surface().get_size()
		bar_Width = int(WIDTH/(len(self.arr)))

		for i in range(len(self.arr)):
			pygame.time.wait(1)
			colour = (255,82,199)
			if Swap_Value_1 == self.arr[i]:
				colour = (0,0,0)
			elif Swap_Value_2 == self.arr[i]:
				colour = (100,255,255)

			pygame.draw.rect(display, (0,0,0), (i*bar_Width-2, HEIGHT - 2, bar_Width + 4, -self.arr[i]*8 + 4), 0)
			filled_rect = pygame.Rect(i*bar_Width, HEIGHT, bar_Width, -self.arr[i]*8)
			pygame.draw.rect(display, colour, filled_rect)

	def SortThinBars(self, Swap_Value_1, Swap_Value_2, display):
		WIDTH, HEIGHT = pygame.display.get_surface().get_size()
		bar_Width = int(WIDTH/(len(self.arr)))

		for i in range(len(self.arr)):
			colour = (255,82,199)
			if Swap_Value_1 == self.arr[i]:
				colour = (0,0,0)
			elif Swap_Value_2 == self.arr[i]:
				colour = (100,255,255)

			pygame.draw.rect(display, (0,0,0), (i*bar_Width-0.1, HEIGHT - 0.1, bar_Width + 0.1, -self.arr[i] + 0.1), 0)
			filled_rect = pygame.Rect(i*bar_Width, HEIGHT, bar_Width, -self.arr[i])
			pygame.draw.rect(display, colour, filled_rect)

	def SortColours(self, display):
		WIDTH, HEIGHT = pygame.display.get_surface().get_size()
		bar_Width = int(WIDTH/(len(self.arr)))

		for i in range (len(self.arr)):
			if self.arr[i] < 255 :
				colour = (self.arr[i],0,0)
			elif self.arr[i] > 255 :
				colour = (255,self.arr[i]-256,0)
				if self.arr[i]-256 > 255:
					colour = (255,255,self.arr[i]-256-255)

			filled_rect = pygame.Rect(i*bar_Width, HEIGHT, bar_Width, -HEIGHT)
			pygame.draw.rect(display, colour, filled_rect)

class SelectionSort(algoritmos):
	def __init__(self):
		super().__init__("SelectionSort")

	def sort(self):
		for i in range(len(self.arr)):
			minim = i
			for j in range(i+1, len(self.arr)):
				if self.arr[minim] > self.arr[j]:
					minim = j
			self.arr[i], self.arr[minim] = self.arr[minim], self.arr[i]
			self.showSwap(self.arr[i], self.arr[minim])

class BubbleSort(algoritmos):
	def __init__(self):
		super().__init__("BubbleSort")

	def sort(self):
		for i in range(len(self.arr)):
			for j in range(len(self.arr)-1-i):
				if self.arr[j] > self.arr[j+1]:

					self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

			self.showSwap(self.arr[j+1], self.arr[j])

class InsertionSort(algoritmos):
	def __init__(self):
		super().__init__('InsertionSort')

	def sort(self):
		for i in range(1, len(self.arr)):
			key = self.arr[i]
			j = i-1
			while(j>=0 and key < self.arr[j]):
				self.arr[j+1] = self.arr[j]
				# self.showSwap(self.arr[j], self.arr[j+1])
				j-=1
			self.arr[j+1] = key
			self.showSwap(self.arr[i], self.arr[j+1])

class CocktailSort(algoritmos):
    def __init__(self):
        super().__init__("CocktailSort")

    def sort(self):
        swapped = True
        start = 0
        end = len(self.arr) - 1
        while swapped == True:
            swapped = False
            for i in range(start, end):
                if (self.arr[i] > self.arr[i+1]):
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    swapped = True
            self.showSwap(self.arr[i], self.arr[self.arr[i+1]])
            if swapped == False:
                break
            swapped == False
            end -= 1
            for i in range(end-1, start-1, -1):
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    swapped = True
            self.showSwap(self.arr[i], self.arr[self.arr[i+1]])
        start += 1

class QuickSort(algoritmos):
	def __init__(self):
		super().__init__('QuickSort')

	def sort(self, arr = [], low = 0, high = 0):
		if arr == []:
			arr = self.arr
			high = len(arr) - 1

		if low < high:
			pivot = self.partition(arr, low, high)
			self.sort(arr, low, pivot-1)
			self.sort(arr, pivot+1, high)

	def partition(self, arr, low, high):
		pivot = arr[high]
		i = low - 1
		for j in range(low, high):
			if arr[j] <= pivot:
				i+=1
				arr[i], arr[j] = arr[j], arr[i]

		arr[i+1],arr[high] = arr[high],arr[i+1]
		self.showSwap(arr[i+1], arr[high])
		return(i+1)
