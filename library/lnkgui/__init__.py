
class Drawable:
    @property
    def z_index(self):
        return self.__z_index
    
    @z_index.setter
    def z_index(self, val):
        self.__z_index = val

from .utils import *
from .manager import *
from .display import *