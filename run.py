import pygame as pg
import library.lnkgui as lgui


WIDTH = 1080
HEIGHT = 720
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pg.init()

root = lgui.Manager()
screen = lgui.ScreenGui((WIDTH, HEIGHT))
root.screen = screen
screen.background_color = WHITE

test_surface = lgui.Surface((200, 200))
test_surface.position = pg.Vector2(250, 50)
test_surface.background_color = BLACK
root.add(test_surface)

test_surface2 = lgui.Surface((60, 60))
test_surface2.position = pg.Vector2(30, 30)
test_surface2.background_color = pg.Color(150, 0, 0)
test_surface.add_child(test_surface2)


pg.display.set_caption("LNK Gui Library Sandbox")
clock = pg.time.Clock()

test_surface.on_mouse_up(5)
## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    root.process_events(events)

    #3 Draw/render
    root.update()

    root.render()
    ## Done after drawing everything to the screen
    pg.display.flip()       

pg.quit()
