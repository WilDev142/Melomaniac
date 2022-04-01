import pygame 



class Checkbox:


	def __init__(self, master, x, y):
		self.master = master
		self.x = x
		self.y = y
		self.check_image = pygame.image.load("Visuals/check_black.PNG")
		self.check_image = pygame.transform.scale(self.check_image, (16, 16))
		self.check_image_rect = self.check_image.get_rect()
		self.check_image_rect.x = self.x + 2
		self.check_image_rect.y = self.y + 2
		self.checked = True



	def render_checkbox(self):
		if self.checked:
			pygame.draw.rect(self.master.screen, (230, 230, 230), pygame.Rect(self.x, self.y, 20, 20))
			pygame.draw.rect(self.master.screen, (0, 0, 0), pygame.Rect(self.x, self.y, 20, 20), 1)
			self.master.screen.blit(self.check_image, self.check_image_rect)

		else:
			pygame.draw.rect(self.master.screen, (230, 230, 230), pygame.Rect(self.x, self.y, 20, 20))
			pygame.draw.rect(self.master.screen, (0, 0, 0), pygame.Rect(self.x, self.y, 20, 20), 1)


# Class used to link all radio buttons
class ButtonGroup():
	def __init__(self):
		self.buttons = []



class RadioButton():
	def __init__(self, master, parent, x, y, default_status=False):
		self.master = master
		self.parent = parent
		self.selected = default_status
		self.x = x
		self.y = y


	# When clicked, select self and unselect other radio buttons
	def select(self):
		for x in self.parent.buttons: x.selected = False
		self.selected = True


	def render_button(self, master):
		if self.selected:
			pygame.draw.rect(master.screen, (230, 230, 230), pygame.Rect(self.x, self.y, 20, 20))
			pygame.draw.rect(master.screen, (0, 0, 0), pygame.Rect(self.x, self.y, 20, 20), 1)
			pygame.draw.circle(master.screen, (0, 0, 0), (self.x + 10, self.y + 10), 7)

		else:
			pygame.draw.rect(master.screen, (230, 230, 230), pygame.Rect(self.x, self.y, 20, 20))
			pygame.draw.rect(master.screen, (0, 0, 0), pygame.Rect(self.x, self.y, 20, 20), 1)