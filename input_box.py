import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = (255, 255, 255)
COLOR_ACTIVE = (255, 120, 120)
ARIAL = pg.font.Font("Visuals/ARIAL.ttf", 25)


class InputBox:

    def __init__(self, master, x, y, w, h, text='', font_color=(255, 255, 255)):
        self.master = master
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = ARIAL.render(text, True, self.color)
        self.active = False
        self.fc = font_color
        self.update()

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            self.update()
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def update(self):
        # Resize the box if the text is too long.
        width = max(400, self.txt_surface.get_width()+25)
        self.rect.w = width
        self.rect.x = (self.master.screen.get_width() / 2) - (self.rect.w / 2)
    def draw(self, screen):
        # Blit the text inside the input box
        self.txt_surface = ARIAL.render(self.text, True, self.color)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y))
        # Blit the rect
        pg.draw.rect(screen, self.color, self.rect, 2)

