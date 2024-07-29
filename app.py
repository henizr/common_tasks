# импорты библиотек
import main
from graphlern import Pixel, Message


# объявление переменных(констант)
GRID_WIDTH = 10
GRID_HEIGHT = 10
PIXEL_SIZE = 50
BACKGROUND_COLOR = "#ffeba1"
SOUND = ""


# Цвет смайла:  #030418

# координаты x пикселей смайла

x_coords_when_y_equals_2 = [5, 6]
x_coords_when_y_equals_3 = [4, 7]
x_coords_when_y_equals_7 = [1, 4, 7, 10]
x_coords_when_y_equals_8 = [2, 3, 8, 9]


# отрисовка
def draw(window):
    # Здесь пиши свой код

    # рисует пиксели по горизонтали, когда y = 2
    for x in x_coords_when_y_equals_2:
       Pixel(window, x=x, y=2, color="#030418", size=PIXEL_SIZE)
    
    for x in x_coords_when_y_equals_3:
       Pixel(window, x=x, y=3, color="#030418", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_7:
       Pixel(window, x=x, y=7, color="#030418", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_8:
       Pixel(window, x=x, y=8, color="#030418", size=PIXEL_SIZE)