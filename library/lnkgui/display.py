import pygame as pg
from .base import *

class Surface(ScreenGui):
    def __init__(self, dimensions, *flags):
        GuiObject.__init__(self)
        self._screen = pg.Surface(dimensions, *flags)
    
    def get(self):
        return self._screen

    def draw(self, screen_gui: ScreenGui):
        self.get().fill(self.background_color)
        position = self.topleft.copy()
        if self.parent:
            position += self.parent.topleft

        screen_gui.get().blit(self.get(), position)
        self.draw_children(screen_gui)