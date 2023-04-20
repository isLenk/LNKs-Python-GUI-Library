"""
This class handles the entire loop process
"""
from .base import *
import pygame as pg


class Manager:
    Collection: list[GuiObject]

    def __init__(self, screen = None):
        self.Collection = list[GuiObject]()
        self._screen = screen

    @property
    def screen(self) -> ScreenGui:
        return self._screen

    @screen.setter
    def screen(self, screen: ScreenGui) -> None:
        self._screen = screen

    def add(self, obj: GuiObject) -> None:
        self.Collection.append(obj)
    
    def remove(self, obj: GuiObject) -> None:
        """Removes the object from the collection"""
        self.Collection.remove(obj)

    def process_events(self, events: list[pg.event.Event]) -> None:
        """Receives a collection of events and handles it."""
        pass

    def update(self):
        for gui in self.Collection:
            gui.update()

    def render(self):
        self._screen.draw()
        for gui in self.Collection:
            gui.draw(self._screen)