import pygame as pg 

pg.init()

ARIAL = pg.font.Font("Visuals/ARIAL.ttf", 25)
ARIAL_ITLC = pg.font.Font("Visuals/ARIALCEItalic.ttf", 25)


class Text:
	def __init__(self, master, x, y, text="", size=30, font="ARIAL", color=(255, 255, 255), center=True):
		self.master = master
		self.text_rect = pg.font.Font(f"Visuals/{font}.ttf", size).render(text, True, color)
		self.x = x
		self.y = y
		if center:
			self.x = (self.master.screen.get_width() / 2) - (self.text_rect.get_width() / 2)

	def draw(self):
		self.master.screen.blit(self.text_rect, (self.x, self.y))