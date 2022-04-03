import pygame 
import time
from Modules.master import Master
from Modules.game import Game



pygame.init()
screen = pygame.display.set_mode((1200, 650))
pygame.display.set_caption("Melomaniac")

master = Master(screen)
game = Game(master)


running = True

pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))

while running:

	screen.fill((0, 0, 0))


	if master.is_running:
		master.display_in_game()
		game.Display_Texts()

		# Change cursor depending on what it is aiming
		for elt in master.in_game_clickables:
			if elt.collidepoint(pygame.mouse.get_pos()):
				pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
				break
			else:
				pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

	elif master.home_menu:
		master.display_home_menu()
		
		# Change cursor depending on what cursor it is aiming and displays message if aiming
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

	# If the user has been on the end screen for more than 6 sec, go back to home menu
	elif master.end_screen:
		if (time.time() - game.time_end_screen) > 6:
			master.logo_img_rect.y = 140
			master.end_screen = False
			master.home_menu = True
		game.end_screen_score_text.draw()
		for text in master.end_screen_texts:
			text.draw()

	# Actualise pygame window
	pygame.display.flip()


	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			# Close Window
			running = False
			pygame.quit()

		elif event.type == pygame.MOUSEBUTTONDOWN:

			if master.home_menu:

				# If click on one of the radio button in menu
				for btn in master.btn_group.buttons:
					if pygame.Rect(btn.x, btn.y, 20, 20).collidepoint(event.pos):
						btn.select()

				# If click on settings menu button, display/hide menu
				if master.settings_btn_rect.collidepoint(event.pos):
					if master.display_settings_menu : master.display_settings_menu = False 
					else: master.display_settings_menu = True

				# If click on advice checkbox
				if pygame.Rect(master.checkbox.x, master.checkbox.y, 20, 20).collidepoint(event.pos):
					if master.checkbox.checked : master.checkbox.checked = False
					else: master.checkbox.checked = True

				# If click on play button, start game
				if master.play_btn_rect.collidepoint(event.pos):
					if game.round == 6:
						game.Reset_Game()
					master.start_game()
					if game.round == 0:
						game.Launch_Round()

				master.update_checkboxes()

			elif master.is_running:

				# Click on return arrow
				if master.back_arrow_rect.collidepoint(event.pos):
					master.stop_game()

				# Click on validation button
				if master.check_rect.collidepoint(event.pos):
					game.Validate_Answer()
					game.Launch_Round()

		elif event.type == pygame.KEYDOWN:

			if master.is_running:

				# Validate if clicked enter
				if event.key == pygame.K_RETURN:
					game.Validate_Answer()
					game.Launch_Round()

			elif master.home_menu:

				# Start game if user clicked enter
				if event.key == pygame.K_RETURN:
					if game.round == 6:
						game.Reset_Game()
					master.start_game()
					if game.round == 0:
						game.Launch_Round()

		if master.is_running:
			for box in master.input_boxes:
				box.handle_event(event)

