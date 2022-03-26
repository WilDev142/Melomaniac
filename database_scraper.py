#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import codecs


t_songs = []

# Iterate through the 9 html pages containing tables to get the list of all songs
for i in range(9):

	file = "karaoke19_html_pages/page" + str(i+1) + ".txt"


	with codecs.open(file, "r", encoding="utf-8") as f:
		soup = BeautifulSoup(f.read(), features="html.parser")

	# Get all the table lines
	lines = soup.find_all("tr")

	# Remove the lines that are not songs
	for line in lines:

		if line.find_all("td") == []:
			lines.remove(line)
		elif len(line.find_all("td")) < 3:
			lines.remove(line)

	# Create a list of songs made up of tuples (title, singer)
	file_songs = [(lines[i].find_all("td")[0].text, lines[i].find_all("td")[1].text) for i in range(len(lines))]
	#file_songs = [lines[i].text for i in range(len(lines))]
	t_songs += file_songs


# Create the definitive list of songs
songs = []

# Remove the duplicate songs
for song in t_songs:
	if song not in songs:
		songs.append(song)


with codecs.open("song_singer_database.txt", "w", encoding="utf-8") as file:
	for song in songs:
		file.write(f"{song[0]} | {song[1]}\n")