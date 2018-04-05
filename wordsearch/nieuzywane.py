def skrzyzowania():
		"""
		Wyświetla słowa z największą liczbą "skrzyżowań" ze słowami na planszy
		"""
		for word in chosen_words:
			matching_words = []
			licznik = 0
			for i in range(len(word)):
				for word_to_fit in words_on_board:
					for j in range(len(word_to_fit)):
						if word[i] == word_to_fit[j]:
							licznik+=1
							print('Litera: ',word[i],'[',j,']')
			if licznik: matching_words.append(word)
			print('Skrzyżowania: ',licznik,'\nPasujące słowa: ',matching_words,'\n')


	def skrzyzowania(word,new_word):
		"""
		Wyświetla miejsca "skrzyżowań" słowa z planszy ze słowem dodawanym
		"""
		miejsca_skrzyzowan = {}
		for i in range(len(word)):
				for j in range(len(new_word)):
					if word[i] == new_word[j]:
						licznik+=1
						print('Litera: ',word[i],'[',j,']')
						miejsca_skrzyzowan.update(licznik:[i,j]) 
		print('Skrzyżowania: ',licznik,'\n')
		return miejsca_skrzyzowan
	
