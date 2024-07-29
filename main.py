import pygame
import app
import sys
from pathlib import Path

from graphlern import *

from app import (
    BACKGROUND_COLOR,
    SOUND,
    PIXEL_SIZE,
    GRID_WIDTH,
    GRID_HEIGHT
)

PATH = Path(__file__).parent
IMG = PATH / "img"
SOUND_FOLDER = PATH / "sound"
FRAMES_PER_SECOND = 30
WINDOW_WIDTH = GRID_WIDTH*PIXEL_SIZE+PIXEL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT*PIXEL_SIZE+PIXEL_SIZE


border_x_bottom = [ 
    (x, 0) 
    for x in  range(0, GRID_WIDTH+1) 
    ]

border_y_left = [
    (0, y) 
    for y in  range(0, GRID_HEIGHT+1)
    ]

borders = [*border_x_bottom, *border_y_left]
 

# (220, 219, 248)
def draw_borders(window, x, y, color="#C6D8FF", thickness=0):

    if (x,y) in borders:
        Pixel(
                sunface=window, 
                x=x, 
                y=y, 
                size=PIXEL_SIZE, 
                thickness=thickness, 
                color=color
                )
        
def draw_cell(window, x, y, color = "grey"):
    
    thickness = 1
    Pixel(
        sunface=window, 
        x=x, 
        y=y, 
        size=PIXEL_SIZE, 
        thickness=thickness, 
        color=color
        )

def draw_grid(window):
    color = "grey"
    thickness = 0

    for x in range(0, GRID_WIDTH+1):
        for y in range(0, GRID_HEIGHT+1):
            draw_cell(window=window, x=x, y=y, color= "#ffffff")
            draw_borders(window=window, x=x, y=y, color="#C6D8FF")
            draw_borders(window=window, x=x, y=y, color="white", thickness=1)

    draw_nums()


def draw_nums():
    for i, x in enumerate(range(0, WINDOW_WIDTH-PIXEL_SIZE+1, PIXEL_SIZE)):
        Text(
            sunface=window,
            text=str(i),
            center_x=x+PIXEL_SIZE//2,
            center_y=WINDOW_WIDTH-PIXEL_SIZE+PIXEL_SIZE//2
        )

    for i, y in zip(
        range((WINDOW_HEIGHT-10)//PIXEL_SIZE, 0, -1),
        range(0, WINDOW_HEIGHT-PIXEL_SIZE+1, PIXEL_SIZE)   
    ):
        Text(
            sunface=window,
            text=str(i),
            center_x=PIXEL_SIZE//2,
            center_y=y+PIXEL_SIZE//2
        )




# Начальные настройки
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pixel art drawing")
clock = pygame.time.Clock()

if SOUND:
    pygame.mixer.music.load(PATH / SOUND_FOLDER / SOUND)
    pygame.mixer.music.play(-1, 0.0)


class Game():
    def __init__(self) -> None:

        self.main_loop()

    def main_loop(self):
        # Main gameloop
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            window.fill(BACKGROUND_COLOR)

            draw_grid(window=window)
            app.draw(window=window)


            pygame.display.update()
            clock.tick(FRAMES_PER_SECOND)



Game()

    