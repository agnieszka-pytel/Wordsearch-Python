#-*- coding: utf-8 -*-

"""
Wordsearch - main module
Agnieszka Pytel
"""

import random, marshal, time
from random import randint

class Wordsearch():
	def __init__(self,size):
		self.grid = []
		self.size = size
		self.words_on_board = {}
		self.words_on_board_list = []
		self.chosen_words = []
		self.slownik = marshal.load(open('slownik_prawidlowa_kolejnosc10.txt','rb'))
		if size < 10:
			wordlist_to_open = 'slownik'+str(size)+'.txt'
		else:
			wordlist_to_open = 'slownik10.txt'
		self.wordlist = marshal.load(open(wordlist_to_open,'rb'))
		self.score = 0
		
	def print_words(self):
		for key,word in self.words_on_board.items():
			print(word)
			
	def print_words_to_find(self):
		print(self.chosen_words)
		
	def initialize_empty_board(self):
		"""
		Tworzy pustą planszę
		"""
		self.grid = [['-']*size for n in range(size)]
		
	def draw(self):
		"""
		Funkcja rysująca ostateczną planszę
		"""
		for row in self.grid:
			print(row)
	
	def place_first_word(self):
		"""
		Układa pierwsze słowo na planszy
		"""
		first_word = Word(random.choice(list(self.wordlist)))
	
		if first_word.word in self.slownik:
			self.chosen_words.append(first_word.word)
		else: 
			self.chosen_words.append(first_word.word[::-1])
		x = 0
		start = randint(0,size-1)
		for i in range(len(first_word.word)):
			self.grid[start][i] = first_word.word[i]
			x += 1
		first_word.start = [start,0]
		first_word.end = [start,x-1]
		
		first_word.horizontal = bool(first_word.start[0] == first_word.end[0])
		self.words_on_board[first_word.word] = first_word
		self.words_on_board_list = list(self.words_on_board.keys())
		#self.chosen_words.pop(0)
		
	def place_first_word_v(self):
		"""
		Układa pierwsze słowo na planszy
		"""
		first_word = Word(random.choice(list(self.wordlist)))
	
		if first_word.word in self.slownik:
			self.chosen_words.append(first_word.word)
		else: 
			self.chosen_words.append(first_word.word[::-1])
		x = 0
		start = randint(0,size-1)
		for i in range(len(first_word.word)):
			self.grid[i][start] = first_word.word[i]
			x += 1
		first_word.start = [0,start]
		first_word.end = [x-1,start]
		
		first_word.horizontal = bool(first_word.start[0] == first_word.end[0])
		self.words_on_board[first_word.word] = first_word
		self.words_on_board_list = list(self.words_on_board.keys())
		#self.chosen_words.pop(0)
		
	def place_another_word(self):
		"""
		Dokładanie kolejnego słowa
		"""
		indeks = randint(0,len(self.words_on_board_list)-1)
		slowo_na_planszy_word = self.words_on_board_list[indeks]
		slowo_na_planszy = self.words_on_board[slowo_na_planszy_word]
		indeks_litery = randint(0,slowo_na_planszy.len-1)
		litera = slowo_na_planszy.word[indeks_litery]
		slownik_do_otwarcia = litera+'.txt'
	
		czy_dolozono = False
	
		while czy_dolozono == False:
		
			#---------Losowanie nowego słowa, które przecina słowo na planszy literą 'litera'
			def losuj_slowo():
				
				def losuj():
					global losowy_index
					losowy_index = randint(0,size)
					try:
						wylosowane = random.choice(marshal.load(open(slownik_do_otwarcia,'rb'))[losowy_index])
						if wylosowane in self.words_on_board_list:
							raise ValueError
						return True
					except Exception:
						return False
						
				flaga = False
				while flaga == False:
					flaga = losuj()
				wylosowane = Word(random.choice(marshal.load(open(slownik_do_otwarcia,'rb'))[losowy_index]))
				
				return wylosowane
			
			#---------Próba ułożenia nowego słowa na planszy
			
			def uloz_wybrane_slowo():
				board = self
				
				wylosowane_slowo = losuj_slowo()
				miejsce_przeciecia_nowe_slowo = wylosowane_slowo.word.find(litera)
				#---------Ustalenie współrzędnych przecięcia
				
				miejsce_przeciecia_stare_slowo = indeks_litery
				
				if(slowo_na_planszy.horizontal):
					przeciecie_x = slowo_na_planszy.start[1]+miejsce_przeciecia_stare_slowo
					przeciecie_y = slowo_na_planszy.start[0]
				else:
					przeciecie_x = slowo_na_planszy.start[1]
					przeciecie_y = slowo_na_planszy.start[0]+miejsce_przeciecia_stare_slowo
				
				
				def fit_word(word_on_board,word,cross_new_word,x,y):
					"""
					Sprawdza, czy słowo mieści się na planszy i czy pola, gdzie ma być dołożone, są wolne
					"""
					if(word_on_board.horizontal):
						try:
							for i in range(0,word.len):
								if ((y-cross_new_word+i) not in range(0,self.size)) or ((y-cross_new_word+word.len-1) not in range(0,self.size)):
									raise IndexError
								else:
									if i != cross_new_word:
										if self.grid[y-cross_new_word+i][x] != '-':
											raise ValueError
										else:
											i+=1
									else:
										i+=1
							return True
						except Exception as e:
							return False
					else:
						try:
							for i in range(0,word.len):
								if ((x-cross_new_word+i) not in range(0,self.size)) or ((x-cross_new_word+word.len-1) not in range(0,self.size)):
									raise IndexError
								else:
									if i != cross_new_word:
										if self.grid[y][x-cross_new_word+i] != '-':
											raise ValueError
										else:
											i+=1
									else:
										i+=1
							return True
						except Exception:
							return False
				
				#print('Czy się miesci: ',fit_word(slowo_na_planszy,wylosowane_slowo,miejsce_przeciecia_nowe_slowo,przeciecie_x,przeciecie_y))
				
				if(fit_word(slowo_na_planszy,wylosowane_slowo,miejsce_przeciecia_nowe_slowo,przeciecie_x,przeciecie_y)):
					for i in range(0,wylosowane_slowo.len):
						"""
						Ułóż słowo na planszy
						"""
						if i != miejsce_przeciecia_nowe_slowo:
							if(slowo_na_planszy.horizontal):
								board.grid[przeciecie_y-miejsce_przeciecia_nowe_slowo+i][przeciecie_x] = wylosowane_slowo.word[i]
							else:
								board.grid[przeciecie_y][przeciecie_x-miejsce_przeciecia_nowe_slowo+i] = wylosowane_slowo.word[i]
							i+=1
						else:
							i+=1
					if(slowo_na_planszy.horizontal):
						"""
						Dopisz do listy współrzędne i orientację słowa
						"""
						wylosowane_slowo.start = [przeciecie_y-miejsce_przeciecia_nowe_slowo,przeciecie_x]
						wylosowane_slowo.end = [przeciecie_y-miejsce_przeciecia_nowe_slowo+wylosowane_slowo.len-1,przeciecie_x]
					else:
						wylosowane_slowo.start = [przeciecie_y,przeciecie_x-miejsce_przeciecia_nowe_slowo]
						wylosowane_slowo.end = [przeciecie_y,przeciecie_x-miejsce_przeciecia_nowe_slowo+wylosowane_slowo.len-1]
					wylosowane_slowo.horizontal = bool(wylosowane_slowo.start[0] == wylosowane_slowo.end[0])
					self.words_on_board[wylosowane_slowo.word] = wylosowane_slowo
					if wylosowane_slowo.word in self.slownik:
						self.chosen_words.append(wylosowane_slowo.word)
					else: 
						self.chosen_words.append(wylosowane_slowo.word[::-1])
					self.score += 1
				else: 
					pass
			czy_dolozono = True

			uloz_wybrane_slowo()	
		
		self.words_on_board_list = list(self.words_on_board.keys())
		
		return True
		
	def try_to_create_board(self):
		"""
		Tworzy wykreślankę z co najmniej tyloma słowami, ile wynosi rozmiar tabeli
		"""
		if self.size < 10:
			while len(self.words_on_board_list) < self.size:
				self.place_another_word()
		else:
			while len(self.words_on_board_list) < 1.5*self.size:
				self.place_another_word()
		return self
		
	def try_to_create_board_in_5s(self):
		"""
		Tworzy wykreślankę z co najmniej tyloma słowami, ile wynosi rozmiar tabeli
		"""
		time_permitted = 5.0
		time_permitted = float(time_permitted)
		start_time = time.time()
		
		while time.time() - start_time < time_permitted:
			self.place_another_word()
		
		return self	
			
	def fill_with_random_letters(self):
		"""
		Wypełnia puste miejsca losowymi literami
		"""
		alfabet = ('a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż') 
		for i in range(0,size):
			for j in range(0,size):
				if self.grid[i][j] == '-':
					self.grid[i][j] = random.choice(alfabet)
				else: pass
				
		return self
	
class Word():
	def __init__(self, word=None):
		self.word = word
		self.start = []
		self.end = []
		self.len = len(self.word)
		self.horizontal = None
		
	def __repr__(self):
		return 'Słowo: {0}, start: {1}, koniec: {2}, długość: {3}, poziomo: {4}'.format(self.word,self.start,self.end,self.len,self.horizontal)

def create_wordsearch(size):
	w = Wordsearch(size)
	w.initialize_empty_board()
	w.place_first_word_v()
	w.try_to_create_board_in_5s()
	w.fill_with_random_letters()
	
	return w
		
start_time = time.time()	
size = 14
a = create_wordsearch(size)
a.draw()
a.print_words_to_find()

print("--- %s seconds ---" % (time.time() - start_time))