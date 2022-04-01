import string
import pickle
import codecs



class Song:
	"""A Song in the Database"""
	def __init__(self, singer, title, file):
		"""Create arguments title, singer and lyrics which is the list of all the words in the song"""
		self.title = title
		self.singer = singer
		with codecs.open(file, "r", encoding = "utf-8") as song_file:
			base_lyrics = song_file.read()
		if not base_lyrics:
			raise FileError
		for punctuation in string.punctuation:
			base_lyrics = base_lyrics.replace(punctuation, " ")
		base_lyrics = base_lyrics.replace("’", " ")
		base_lyrics = base_lyrics.split()
		self.lyrics = []
		for word in base_lyrics:
			if word.lower() not in self.lyrics:
				self.lyrics.append(word.lower())
		self.Save_In_File()


	def Save_In_File(self):
		"""Save the Song in 'Songs', our song database"""
		with open("Songs","rb") as file:
			unpickler = pickle.Unpickler(file)
			try:
				songs_list = unpickler.load()
			except EOFError:
				songs_list = []
			for elt in songs_list:
				if self.singer == elt.singer:
					if self.title == elt.title:
						raise SongError

		with open("Songs","wb") as file:
			songs_list.append(self)
			pickler = pickle.Pickler(file)
			pickler.dump(songs_list)