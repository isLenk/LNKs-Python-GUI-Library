
class Drawable:
    __z_index: int = 0

    @__z_index.setter
    def z_index(self, val):
        self.__z_index = val
    
    @__z_index.getter
    def z_index(self):
        return self.__z_index


# Import screen library
from lnkgui.surface import screen, surface
