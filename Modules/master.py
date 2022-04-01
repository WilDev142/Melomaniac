import pygame 
from Modules.input_box import InputBox
from Modules.text import Text
from Modules.buttons import Checkbox, ButtonGroup, RadioButton



class Master():


	def __init__(self, screen):
		self.screen = screen
		self.is_running = False
		self.home_menu = True

		self.game_level = 1
		self.give_examples = True

		# Radio buttons to choose game level
		self.btn_group = ButtonGroup()
		self.btn_group.buttons.append(RadioButton(self, self.btn_group, 1080, 252, True))
		self.btn_group.buttons.append(RadioButton(self, self.btn_group, 1080, 280))
		self.btn_group.buttons.append(RadioButton(self, self.btn_group, 1080, 307))
		self.display_contact_msg = False
		self.display_tutorial_msg = False
		self.display_settings_menu = False

		self.checkbox = Checkbox(self, 1050, 435)

		self.logo_img = pygame.image.load("Visuals/Melomaniac_logo_BW.PNG")
		self.logo_img = pygame.transform.scale(self.logo_img, (577, 69))
		self.logo_img_rect = self.logo_img.get_rect()
		self.logo_img_rect.x = self.screen.get_width() / 2 - 288
		self.logo_img_rect.y = 140

		self.play_btn = pygame.image.load("Visuals/Jouer_btn_BW.PNG")
		self.play_btn = pygame.transform.scale(self.play_btn, (295, 105))
		self.play_btn_rect = self.logo_img.get_rect()
		self.play_btn_rect.x = self.screen.get_width() / 2 - 148
		self.play_btn_rect.y = 400

		self.settings_btn = pygame.image.load("Visuals/Settings.PNG")
		self.settings_btn = pygame.transform.scale(self.settings_btn, (60, 60))
		self.settings_btn_rect = self.logo_img.get_rect()
		self.settings_btn_rect.x = self.screen.get_width() - 80
		self.settings_btn_rect.y = 20

		self.question_btn = pygame.image.load("Visuals/Question.PNG")
		self.question_btn = pygame.transform.scale(self.question_btn, (34, 60))
		self.question_btn_rect = self.logo_img.get_rect()
		self.question_btn_rect.x = 20
		self.question_btn_rect.y = 20

		self.contact_btn = pygame.image.load("Visuals/Mail_BW.PNG")
		self.contact_btn = pygame.transform.scale(self.contact_btn, (60, 60))
		self.contact_btn_rect = self.logo_img.get_rect()
		self.contact_btn_rect.x = self.screen.get_width() - 80
		self.contact_btn_rect.y = self.screen.get_height() - 80

		self.contact_msg = pygame.image.load("Visuals/Contact_Message_BW.PNG")
		self.contact_msg = pygame.transform.scale(self.contact_msg, (885, 85))
		self.contact_msg_rect = self.logo_img.get_rect()
		self.contact_msg_rect.x = self.screen.get_width() / 2 - 442
		self.contact_msg_rect.y = 530

		self.tutorial_msg = pygame.image.load("Visuals/Tutorial_Message_BW.PNG")
		self.tutorial_msg = pygame.transform.scale(self.tutorial_msg, (868, 45))
		self.tutorial_msg_rect = self.logo_img.get_rect()
		self.tutorial_msg_rect.x = self.screen.get_width() / 2 - 434
		self.tutorial_msg_rect.y = 40

		self.settings_menu = pygame.image.load("Visuals/Settings_Menu_BW.PNG")
		self.settings_menu = pygame.transform.scale(self.settings_menu, (221, 364))
		self.settings_menu_rect = self.logo_img.get_rect()
		self.settings_menu_rect.x = self.screen.get_width() - 250
		self.settings_menu_rect.y = 130

		self.back_arrow = pygame.image.load("Visuals/back-arrow.PNG")
		self.back_arrow = pygame.transform.scale(self.back_arrow, (60, 60))
		self.back_arrow_rect = self.logo_img.get_rect()
		self.back_arrow_rect.x = 20
		self.back_arrow_rect.y = 20

		self.check = pygame.image.load("Visuals/check.PNG")
		self.check = pygame.transform.scale(self.check, (80, 80))
		self.check_rect = self.logo_img.get_rect()
		self.check_rect.x = 880
		self.check_rect.y = 500


		self.home_clickables = [self.play_btn_rect, self.settings_btn_rect, self.question_btn_rect,
						self.contact_btn_rect]

		self.input_boxes = []
		self.input_boxes.append(InputBox(self, 0, 480, 400, 30))
		self.input_boxes.append(InputBox(self, 0, 580, 400, 30))

		self.rules_text = Text(self, 0, 230, "Trouvez une chanson dont les paroles contiennent le mot :")
		self.title_text = Text(self, 0, 430, "Titre de la chanson :")
		self.singer_text = Text(self, 0, 530, "Interprète :")

		self.in_game_clickables = [self.input_boxes[0].rect, self.input_boxes[1].rect, self.back_arrow_rect, self.check_rect]

		self.end_screen_texts = []
		self.end_screen_texts.append(Text(self, 0, 100, "Partie terminée !", size=50))
		self.end_screen_texts.append(Text(self, 0, 210, "Vous avez obtenu un score de :", size=50))
		self.end_screen_texts.append(Text(self, 0, 480, "Félicitations !", size=50))


	def display_home_menu(self):
		self.screen.blit(self.logo_img, self.logo_img_rect)
		self.screen.blit(self.play_btn, self.play_btn_rect)
		self.screen.blit(self.settings_btn, self.settings_btn_rect)
		self.screen.blit(self.question_btn, self.question_btn_rect)
		self.screen.blit(self.contact_btn, self.contact_btn_rect)
		if self.display_contact_msg:
			self.screen.blit(self.contact_msg, self.contact_msg_rect)
		elif self.display_tutorial_msg:
			self.screen.blit(self.tutorial_msg, self.tutorial_msg_rect)
		if self.display_settings_menu:
			self.screen.blit(self.settings_menu, self.settings_menu_rect)


	def display_in_game(self):
		for input_box in self.input_boxes:
			input_box.draw(self.screen)
		self.title_text.draw()
		self.singer_text.draw()
		self.rules_text.draw()
		self.screen.blit(self.logo_img, self.logo_img_rect)
		self.screen.blit(self.back_arrow, self.back_arrow_rect)
		self.screen.blit(self.check, self.check_rect)


	def update_checkboxes(self):
		if self.checkbox.checked:
			self.give_examples = True
		else:
			self.give_examples = False

		for index, btn in enumerate(self.btn_group.buttons):
			if btn.selected:
				self.game_level = index + 1


	def start_game(self):
		self.logo_img_rect.y = 60
		self.is_running = True
		self.home_menu = False
		self.end_screen = False


	def stop_game(self):
		self.logo_img_rect.y = 140
		self.is_running = False
		self.home_menu = True