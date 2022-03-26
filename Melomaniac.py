import pygame 
from input_box import InputBox
from text import Text
from buttons import Checkbox, ButtonGroup, RadioButton



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


		self.home_clickables = [self.play_btn_rect, self.settings_btn_rect, self.question_btn_rect,
						self.contact_btn_rect]

		self.input_boxes = []
		self.input_boxes.append(InputBox(self, 0, 480, 400, 30))
		self.input_boxes.append(InputBox(self, 0, 580, 400, 30))

		self.rules_text = Text(self, 0, 230, "Trouvez une chanson dont les paroles contiennent le mot :")
		self.title_text = Text(self, 0, 430, "Titre de la chanson :")
		self.singer_text = Text(self, 0, 530, "Interprète :")

		self.word_text = Text(self, 0, 300, "Camion", size=60, font="ARIALBD")

		self.in_game_clickables = [self.input_boxes[0].rect, self.input_boxes[1].rect, self.back_arrow_rect]

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
		self.word_text.draw()
		self.screen.blit(self.logo_img, self.logo_img_rect)
		self.screen.blit(self.back_arrow, self.back_arrow_rect)

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


pygame.init()
screen = pygame.display.set_mode((1200, 650))
pygame.display.set_caption("Melomaniac")

master = Master(screen)


running = True

pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))

while running:

	screen.fill((0, 0, 0))


	if master.is_running:
		master.display_in_game()

		for elt in master.in_game_clickables:
			if elt.collidepoint(pygame.mouse.get_pos()):
				pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
				break
			else:
				pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

	elif master.home_menu:
		master.display_home_menu()
		
		for elt in master.home_clickables:
			if elt.collidepoint(pygame.mouse.get_pos()):
				pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
				if elt == master.contact_btn_rect:
					master.display_contact_msg = True
				elif elt == master.question_btn_rect:
					master.display_tutorial_msg = True
				break
			else:
				pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
				master.display_contact_msg = False
				master.display_tutorial_msg = False

		if master.display_settings_menu:
			for btn in master.btn_group.buttons:
				btn.render_button(master)

			master.checkbox.render_checkbox()


	pygame.display.flip()

	for event in pygame.event.get():

		# Click on settings : settings menu shows up right under settings btn


		if event.type == pygame.QUIT:
			# Close Window
			running = False
			pygame.quit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			for btn in master.btn_group.buttons:
				if pygame.Rect(btn.x, btn.y, 20, 20).collidepoint(event.pos) and master.home_menu:
					btn.select()

			if master.settings_btn_rect.collidepoint(event.pos):
				if master.display_settings_menu : master.display_settings_menu = False 
				else: master.display_settings_menu = True

			if pygame.Rect(master.checkbox.x, master.checkbox.y, 20, 20).collidepoint(event.pos) and master.home_menu:
				if master.checkbox.checked : master.checkbox.checked = False
				else: master.checkbox.checked = True

			if master.play_btn_rect.collidepoint(event.pos) and master.home_menu:
				master.home_menu = False
				master.is_running = True
				master.start_game()

			master.update_checkboxes()


		if master.is_running:
			for box in master.input_boxes:
				box.handle_event(event)


"""        # If event type is pressed key
        elif event.type == pygame.KEYDOWN:
            # Set event.key to True
            game.pressed[event.key] = True

            if game.home_settings_menu:
                if event.key == pygame.K_RETURN:
                    game.visuals.update_checkboxes()
                    game.visuals.update_input_boxes()


        elif event.type == pygame.KEYUP:
            # Set event.key to False
            game.pressed[event.key] = False

        """
