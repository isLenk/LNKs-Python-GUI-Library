"""
This module contains all the base classes of the LNK UI
"""
import pygame as pg
from .utils import *
from pygame import Color

class Drawable:
    def draw(self, *args): pass
    def update(self, *args): pass

class Events:
    def on_mouse_motion(self, e): pass
    def on_mouse_down(self, e): pass
    def on_mouse_up(self, e): pass
    def on_keyup(self, e): pass
    def on_keydown(self, e): pass

class GuiObject(Drawable, Events):
    """The top-level class of all objects that are part of the LNK_UI"""

    def __init__(self):
        self._background_color = Color(255, 255, 255)
        self._text_color = Color(0, 0, 0)
        self._visible = True
        self._parent = None
        self._contents = list()
        self._size = (1, 1)
        self._position = (1, 1)
    
    def focused(self) -> bool:
        """Returns true if the mouse is hovering over
        this element
        """
        return pg.Rect(self.position, self.size).collidepoint(pg.mouse.get_pos()) 
    
    @property
    def abs_position(self) -> pg.Vector2:
        return self._position or pg.Vector2(0, 0) + \
                self.parent.position if self.parent else (0, 0)
    
    @property
    def position(self) -> pg.Vector2:
        return self._position or pg.Vector2(0, 0)
    
    @position.setter
    def position(self, val) -> None:
        self._position = val

    @property
    def topleft(self) -> pg.Vector2:
        return self._position
    
    @property
    def size(self) -> Size:
        return self._size()
    
    @size.setter
    def size(self, val) -> None:
        self._size = val

    @property
    def background_color(self) -> Color:
        return self._background_color

    @background_color.setter
    def background_color(self, color) -> None:
        self._background_color = color
    
    @property
    def text_color(self) -> Color:
        return self._text_color
    
    @text_color.setter
    def text_color(self, color) -> None:
        self._text_color = color
    
    @property
    def visible(self) -> bool:
        return self._visible
    
    @visible.setter
    def visible(self, val) -> None:
        self._visible = val

    @property
    def parent(self) -> "GuiObject" or None:
        return self._parent
    
    @parent.setter
    def parent(self, val: "GuiObject") -> None:
        val.add_child(self)
        
    @property
    def contents(self) -> list["GuiObject"]:
        return self._contents
    
    @contents.setter
    def contents(self, val) -> None:
        raise Exception("Contents is not settable")
    
    def add_child(self, child: "GuiObject") -> None:
        if child is self:
            raise Exception("Attempt to add itself as a child of itself")
        self.contents.append(child)
        child._parent = self

    def draw(self, screen_gui: "ScreenGui"):
        rect = pg.Rect(self.parent.position + self.position, self.size)
        pg.draw.rect(screen_gui.get(), self.background_color, rect)
        self.draw_children(screen_gui.get())
    
    def draw_children(self, surface: pg.Surface):
        for gui in self.contents:
            gui.draw(surface)

    #__getitem__, __setitem__ https://docs.python.org/3/reference/datamodel.html#object.__getitem__
        
class ScreenGui(GuiObject):
    def __init__(self, dimensions):
        """Returns a pygame screen."""
        GuiObject.__init__(self)
        self.size = Size(*dimensions)
        self._screen = pg.display.set_mode(dimensions)
    
    def get(self):
        return self._screen
    
    def draw(self, *args):
        self._screen.fill(self.background_color)
        return self._screen
    
    def update(self, *args): pass