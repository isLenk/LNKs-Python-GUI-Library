import pygame as pg

class Size:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def __iter__(self):
        yield self.width
        yield self.height

    def __call__(self):
        return pg.Vector2(self.width, self.height)