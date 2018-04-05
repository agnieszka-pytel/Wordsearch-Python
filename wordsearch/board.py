#-*- coding: utf-8 -*-

"""
Wordsearch - board
Agnieszka Pytel
"""

#size = input("Podaj rozmiar tabeli (długość boku): ")

size = 5

size = int(size)
grid = [1 for n in range(size)]
grid = [[1]*size for n in range(size)]

def draw_grid():
	for row in grid:
		print(row)
		
draw_grid()
