import pygame
import pickle
import string
import random
import time
import sys
import unicodedata
from Modules.text import Text
from Modules.song import Song

# Add path to Modules to enable Song objects to be launched 
sys.path.append('C:/Users/lucas/Documents/Programmation/Python/Melomaniac/Modules')



class Game():


	def __init__(self, master):
		self.master = master
		self.already_used_words = []
		self.round = 0
		self.score = 0
		self.bonus = 1

		self.display_singer_solution = False
		self.display_solution_examples = False


	# Reset parameters after finishing a game
	def Reset_Game(self):
		self.round = 0
		self.score = 0
		self.bonus = 1
		self.display_singer_solution = False
		self.display_solution_examples = False


	def Launch_Round(self):
		self.round += 1

		if self.round < 6 :
			self.word = self.Get_Random_Word(self.master.game_level)
			#self.word = "fête"
			self.solutions = self.Get_Solution()

			self.word_text = Text(self.master, 0, 300, self.word, size=60, font="ARIALBD")
			self.round_text = Text(self.master, 980, 50, f"Manche : {self.round}/5", size=32, font="ARIALBD", center=False)
			self.score_text = Text(self.master, 980, 100, f"Score : {self.score}", size=32, font="ARIALBD", center=False)

			self.answer_title = ""
			self.answer_singer = ""

			for box in self.master.input_boxes:
				box.text = ""
		else:
			self.master.end_screen = True
			self.master.is_running = False
			self.time_end_screen = time.time()


	# Get answers from input boxes
	def Validate_Answer(self):
		self.answer_title = self.master.input_boxes[0].text
		self.answer_singer = self.master.input_boxes[1].text
		self.Correct_Anwers()


	def Correct_Anwers(self):
		# If title answered is correct, give points
		if self.Is_Title_A_Solution():
			self.display_solution_examples = False

			# If singer answered correct, give more points
			if self.Is_It_Good_Singer(self.Simplify(self.answer_title), self.Simplify(self.answer_singer)):
				self.score += (200 * self.bonus)
				self.display_singer_solution = False
			else:
				self.score += (100 * self.bonus)
				self.display_singer_solution = True
				self.solution_singer = self.Get_Solution_Singer()
				self.Set_Singer_Solution_Text()
			self.bonus += 1

		else:
			self.display_solution_examples = True
			self.Set_Solution_Examples_Text()
			self.bonus = 1
		self.Set_End_Screen_Score_Text()


	# Return a random word we've never played with depending of difficulty level
	def Get_Random_Word(self, difficulty_level):
		word = str()

		if difficulty_level == 1:
			with open("System/words_lvl_1", "rb") as file:
				Unpickler = pickle.Unpickler(file)
				word_list = Unpickler.load()
			while word in self.already_used_words or word == "":
				word = random.choice(word_list)
			self.already_used_words.append(word)

		elif difficulty_level == 2:
			with open("System/words_lvl_2", "rb") as file:
				Unpickler = pickle.Unpickler(file)
				word_list = Unpickler.load()
			while word in self.already_used_words or word == "":
				word = random.choice(word_list)
			self.already_used_words.append(word)

		elif difficulty_level == 3:
			with open("System/words_lvl_3", "rb") as file:
				Unpickler = pickle.Unpickler(file)
				word_list = Unpickler.load()
			while word in self.already_used_words or word == "":
				word = random.choice(word_list)
			self.already_used_words.append(word)

		return word


	# Remove punctuation, accents and spaces
	def Simplify(self, to_simplify):
		simplified = to_simplify.lower()
		for punctuation in string.punctuation:
			simplified = simplified.replace(punctuation, " ")
		simplified = ''.join((c for c in unicodedata.normalize('NFD', simplified) if unicodedata.category(c) != 'Mn')) #To take off accents and special characters, such as "ç"
		simplified_elts = simplified.split()
		simplified = ""
		for elt in simplified_elts:
			simplified += elt
		return simplified


	# Return a list with different versions of word to find in lyrics
	def SimplifyWordToList(self, word):
		word = word.lower()
		word_no_accent = ''.join((c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')) #To take off accents and special characters, such as "ç"
		words = [word, word_no_accent, word+"s", word_no_accent+"s"]
		return words


	# Return list of possible solutions
	def Get_Solution(self):
		words = self.SimplifyWordToList(self.word)
		solutions_list = []
		with open("System/Songs", "rb") as file:
			unpickler = pickle.Unpickler(file)
			songs_list = unpickler.load()
		for word in words:
			for song in songs_list:
				if word in song.lyrics:
					if (song.singer, song.title) not in solutions_list:
						solutions_list.append((song.singer, song.title))
		return(solutions_list)


	# Check if answered title in list of solutions
	def Is_Title_A_Solution(self):
		for song in self.solutions:
			if self.Simplify(self.answer_title) == self.Simplify(song[1]):
				return True
		return False


	# Check if singer corresponds to the title answered
	def Is_It_Good_Singer(self, title, singer):
		# List of all good singers possible with the title answered
		good_singers = []
		for solution in self.solutions:
			# If title answered in list of solutions
			if title == self.Simplify(solution[1]):
				# Add corresponding singer to list of good singers
				good_singers.append(self.Simplify(solution[0]))

		if singer in good_singers:
			return True
		else:
			return False


	# Return the singer of the the song in case the user found a good title, but not the corresponding singer
	def Get_Solution_Singer(self):
		for solution in self.solutions: 
			if self.Simplify(self.answer_title) == self.Simplify(solution[1]):
				return solution[0]


	# Return 3 random solutions in list of solution to display them
	def Give_Solution_Examples(self):
		solutions = []
		if len(self.solutions) <= 3:
			for solution in self.solutions:
				solutions_singers.append(solution[0])
				solutions_titles.append(solution[1])
		else:
			already_used_index = []
			for i in range(3):
				DoAgain = True
				while DoAgain:
					index = random.randint(0, len(self.solutions)-1)
					if index not in already_used_index:
						already_used_index.append(index)
						DoAgain = False
				solutions.append((self.solutions[index][0], self.solutions[index][1]))
		return solutions


	def Set_Singer_Solution_Text(self):
		self.solution_singer_texts = []
		self.solution_singer_texts.append(Text(self.master, 870, 330, "L'interprète de la chanson", size=20, font="ARIALBD", center=False, center_in_rect=True, x1_rect=870, x2_rect=1200))
		self.solution_singer_texts.append(Text(self.master, 910, 365, self.answer_title, size=20, font="ARIALCEItalic", center=False, center_in_rect=True, x1_rect=870, x2_rect=1200))
		self.solution_singer_texts.append(Text(self.master, 970, 400, "est en fait", size=20, font="ARIALBD", center=False, center_in_rect=True, x1_rect=870, x2_rect=1200))
		self.solution_singer_texts.append(Text(self.master, 910, 435, self.solution_singer, size=20, font="ARIALCEItalic", center=False, center_in_rect=True, x1_rect=870, x2_rect=1200))	
	

	def Set_Solution_Examples_Text(self):
		self.solution_examples_texts = []
		solutions = self.Give_Solution_Examples()
		self.solution_examples_texts.append(Text(self.master, 0, 480, "Exemples de solutions possibles :", size=20, font="ARIALBD", center=False, center_in_rect=True, x1_rect=0, x2_rect=380))
		self.solution_examples_texts.append(Text(self.master, 0, 520, f"{solutions[0][1]} de {solutions[0][0]}", size=15, font="ARIALCEItalic", center=False, center_in_rect=True, x1_rect=0, x2_rect=380))
		self.solution_examples_texts.append(Text(self.master, 0, 550, f"{solutions[1][1]} de {solutions[1][0]}", size=15, font="ARIALCEItalic", center=False, center_in_rect=True, x1_rect=0, x2_rect=380))
		self.solution_examples_texts.append(Text(self.master, 0, 580, f"{solutions[2][1]} de {solutions[2][0]}", size=15, font="ARIALCEItalic", center=False, center_in_rect=True, x1_rect=0, x2_rect=380))


	def Set_End_Screen_Score_Text(self):
		self.end_screen_score_text = Text(self.master, 0, 300, str(self.score), size=80, font="ARIALBD", center=True)


	def Display_Texts(self):
		self.word_text.draw()
		self.round_text.draw()
		self.score_text.draw()

		if self.display_singer_solution:
			for text in self.solution_singer_texts:
				text.draw()

		if self.display_solution_examples and self.master.give_examples:
			for text in self.solution_examples_texts:
				text.draw()