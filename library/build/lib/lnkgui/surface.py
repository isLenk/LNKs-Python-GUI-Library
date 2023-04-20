import pygame as pg

class screen:
    def __init__(self, dimensions):
        """Returns a pygame screen."""
        self.__screen = pg.display.set_mode(dimensions)
    
    def get(self):
        return self.__screen

class surface:
    def __init__(self, dimensions, *flags):
        self._surface = pg.Surface(dimensions, *flags)
    
    def get(self):
        return self._surface