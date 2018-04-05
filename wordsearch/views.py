from flask import Flask, render_template, request, session
from collections import OrderedDict

app = Flask(__name__)
import wordsearch, pickle

@app.route("/")
def index():
	return render_template('index.htm')
	
@app.route("/board",methods=['POST'])
def board():
	size = int(request.form.get('board_size'))
	board = wordsearch.create_wordsearch(size)
	words = board.chosen_words
	grid = board.grid
	number_to_find = len(board.chosen_words)
	number_of_words = len(board.words_on_board_list)
	pickle.dump(board,open('board.txt', 'wb'))
	return render_template('board.htm', number_to_find = number_to_find, number_of_words = number_of_words, size = size, words = words, grid = grid, board = board)

@app.route("/board/solve",methods=['POST'])
def board_solve():
	found_word = str(request.form.get('found_word')).lower()
	board = pickle.load(open('board.txt','rb'))
	words = board.full_word_list
	grid = board.grid
	size = board.size
	board.found_words.append(found_word)
	if found_word in words and found_word in board.chosen_words:
		board.chosen_words.remove(found_word)
	number_of_words = len(board.words_on_board_list)
	found = board.found_words
	number_to_find = len(board.chosen_words)
	pickle.dump(board,open('board.txt', 'wb'))
	if number_to_find == 0:
		return render_template('winner.htm')
	else:
		return render_template('board_solve.htm', number_of_words = number_of_words, number_to_find = number_to_find, size = size, found = found, words = words, grid = grid)

	
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5023, debug=True)