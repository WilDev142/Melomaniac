import string
import pickle


class Song:

	def __init__(self, name, lyrics):
		self.title =  self.Get_Title(name)
		self.singer =  self.Get_Singer(name)
		self.lyrics = self.Get_Lyrics(lyrics)

		self.Save_In_File()


	def Get_Title(self, name):
		return_name = name.split("|")[1].strip().capitalize()
		for punctuation in string.punctuation:
			return_name = return_name.replace(punctuation, " ")
		return_name = return_name.replace("’", " ").replace("  ", " ").replace("  ", " ")

		return return_name

	def Get_Singer(self, name):
		return_singer = name.split("|")[0].strip().capitalize()
		for punctuation in string.punctuation:
			return_singer = return_singer.replace(punctuation, " ")
		return_singer = return_singer.replace("’", " ").replace("  ", " ").replace("  ", " ")

		return return_singer

	def Get_Lyrics(self, lyrics):
		cleared_lyrics = lyrics
		to_remove = string.punctuation + "↑…»«’—–°º"
		for punctuation in to_remove:
			cleared_lyrics = cleared_lyrics.replace(punctuation, " ")
		cleared_lyrics = cleared_lyrics.replace("’", " ")
		cleared_lyrics = cleared_lyrics.split()

		lyrics_words = []
		for word in cleared_lyrics:
			if word.lower() not in lyrics_words:
				lyrics_words.append(word.lower())

		return lyrics_words


	def Save_In_File(self):

		try:
			with open("Songs", "rb") as file: #Try to open the file in read mode, to see if it exists
				pass
		except Exception: 
			with open("Songs", "wb") as file: #The file doesn't exists, I create it
				pass

		"""Save the Song in 'Songs', our song database"""
		with open("Songs","rb") as file:
			unpickler = pickle.Unpickler(file)
			try:
				songs_list = unpickler.load()
			except EOFError:
				songs_list = []
			Do_Saving = True
			for elt in songs_list:
				if self.singer == elt.singer:
					if self.title == elt.title:
						print(elt.singer, elt.title, "ERROR!!!")
						Do_Saving = False

		if Do_Saving:
			with open("Songs","wb") as file:
				songs_list.append(self)
				print(len(songs_list))
				pickler = pickle.Pickler(file)
				pickler.dump(songs_list)