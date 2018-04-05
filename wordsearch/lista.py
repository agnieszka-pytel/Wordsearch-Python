#-*- coding: utf-8 -*-

"""
Wordsearch - wordlist
Agnieszka Pytel
"""

import marshal, re

def _words_from_line(line):
    "Zwraca listę słów dla linijki tekstu unicode."
    words = re.split('[\W\d]+', line)
    return [w.lower() for w in words if w]

def unique_words(in_filename,out_filename,max_len):
	"""
	Zwraca posortowaną alfabetycznie listę wszystkich słów z pliku.
	"""
	wordset = set()

	source_file = open(in_filename, 'r', encoding='utf-8')
	dictionary = 'slownik_prawidlowa_kolejnosc'+str(max_len)+'.txt'
	file_with_dictionary = open(dictionary,'wb')
	end_file = open(out_filename, 'wb')
	slownik_prawidlowa_kolejnosc = set()
	for line in source_file:
		words = _words_from_line(line)
		if len(line) > 2:
			if len(line) < max_len:
				for word in words:
				   slownik_prawidlowa_kolejnosc.add(word)
				   wordset.add(word)
				   wordset.add(word[::-1])
	marshal.dump(slownik_prawidlowa_kolejnosc,file_with_dictionary)
	marshal.dump(wordset,end_file)
	file_with_dictionary.close()
	
	source_file.close()
	end_file.close()

	return wordset
	
def utworz_slowniki(filename, wordlist):
	alfabet = ('a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż')
	   
	dict_list = []
	for x in range(len(alfabet)):
		dict_list.append({0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]})
	
	#source_file = marshal.load(open('slownik.txt','rb'))
	for line in wordlist:
		for i in range(len(alfabet)):
			for j in range(len(line)):
				if alfabet[i] == line[j]:
					dict_list[i][j].append(line)
	
	files = []
	
	for x in range(len(dict_list)):
		format = '.txt'
		files.append(str(alfabet[x])+format)
		file_to_write = open(files[x], 'wb')
		marshal.dump(dict_list[x],file_to_write)
		file_to_write.close()
	
	#source_file.close()
	return True
	
import time
start_time = time.time()

#utwórz słowniki słow max pięcioliterowych do max dziesięcioliterowych
for i in range(5,10):
	format = 'slownik'+str(i)+'.txt'
	unique_words('lista2.txt',format,i)	
slowa = unique_words('lista2.txt','slownik10.txt',10)	
utworz_slowniki('slownik10.txt',slowa)

print("--- %s seconds ---" % (time.time() - start_time))