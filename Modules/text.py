import pygame as pg 

pg.init()



class Text:


	def __init__(self, master, x, y, text="", size=30, font="ARIAL", color=(255, 255, 255), center=True, center_in_rect=False, x1_rect=0, x2_rect=0):
		self.master = master
		self.text_rect = pg.font.Font(f"Visuals/{font}.ttf", size).render(text, True, color)
		self.x = x
		self.y = y
		if center:
			self.x = (self.master.screen.get_width() / 2) - (self.text_rect.get_width() / 2)
		if center_in_rect:
			self.x = ((x2_rect - x1_rect) / 2) - (self.text_rect.get_width() / 2) + x1_rect


	def draw(self):
		self.master.screen.blit(self.text_rect, (self.x, self.y))