# импорты библиотек
import main
from graphlern import Pixel, Message


# объявление переменных(констант)
GRID_WIDTH = 10
GRID_HEIGHT = 10
PIXEL_SIZE = 50
BACKGROUND_COLOR = "#ffeba1"
SOUND = ""


# координаты x пикселей арбуза

x_coords_when_y_equals_3 = [3, 4, 5, 6, 7, 8]
x_coords_when_y_equals_4 = [2, 3, 4, 5, 6, 7, 8, 9]
x_coords_when_y_equals_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_coords_when_y_equals_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_coords_when_y_equals_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 

# отрисовка
def draw(window):
    # Здесь пиши свой код

    for x in x_coords_when_y_equals_3:
        Pixel(window, x=x, y=3, color="darkgreen", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_4:
        if x == 2:
            Pixel(window, x=x, y=4, color="darkgreen", size=PIXEL_SIZE)
        elif x == 3:
            Pixel(window, x=x, y=4, color="green", size=PIXEL_SIZE)
        elif x == 4:
            Pixel(window, x=x, y=4, color="green", size=PIXEL_SIZE)
        elif x == 5:
            Pixel(window, x=x, y=4, color="green", size=PIXEL_SIZE)
        elif x == 6:
            Pixel(window, x=x, y=4, color="green", size=PIXEL_SIZE)
        elif x == 7:
            Pixel(window, x=x, y=4, color="green", size=PIXEL_SIZE)
        elif x == 8:
            Pixel(window, x=x, y=4, color="green", size=PIXEL_SIZE)
        elif x == 9:
            Pixel(window, x=x, y=4, color="darkgreen", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_5:
        if x == 1:
            Pixel(window, x=x, y=5, color="darkgreen", size=PIXEL_SIZE)
        elif x == 2:
            Pixel(window, x=x, y=5, color="green", size=PIXEL_SIZE)
        elif x >= 3 and x <= 6:
            Pixel(window, x=x, y=5, color="red", size=PIXEL_SIZE)
        elif x == 7:
            Pixel(window, x=x, y=5, color="black", size=PIXEL_SIZE)
        elif x == 8:
            Pixel(window, x=x, y=5, color="red", size=PIXEL_SIZE)
        elif x == 9:
            Pixel(window, x=x, y=5, color="green", size=PIXEL_SIZE)
        elif x == 10:
            Pixel(window, x=x, y=5, color="darkgreen", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_6:
        if x == 1:
            Pixel(window, x=x, y=6, color="darkgreen", size=PIXEL_SIZE)
        elif x == 2:
            Pixel(window, x=x, y=6, color="green", size=PIXEL_SIZE)
        elif x == 3:
            Pixel(window, x=x, y=6, color="red", size=PIXEL_SIZE)
        elif x == 4:
            Pixel(window, x=x, y=6, color="black", size=PIXEL_SIZE)
        elif x >= 5 and x <= 8:
            Pixel(window, x=x, y=6, color="red", size=PIXEL_SIZE)
        elif x == 9:
            Pixel(window, x=x, y=6, color="green", size=PIXEL_SIZE)
        elif x == 10:
            Pixel(window, x=x, y=6, color="darkgreen", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_7:
        if x == 1:
            Pixel(window, x=x, y=7, color="darkgreen", size=PIXEL_SIZE)
        elif x == 2:
            Pixel(window, x=x, y=7, color="green", size=PIXEL_SIZE)
        elif x >= 3 and x <= 5:
            Pixel(window, x=x, y=7, color="red", size=PIXEL_SIZE)
        elif x == 6:
            Pixel(window, x=x, y=7, color="black", size=PIXEL_SIZE)
        elif x ==7:
            Pixel(window, x=x, y=7, color="red", size=PIXEL_SIZE)
        elif x == 8:
            Pixel(window, x=x, y=7, color="red", size=PIXEL_SIZE)
        elif x == 9:
            Pixel(window, x=x, y=7, color="green", size=PIXEL_SIZE)
        elif x == 10:
            Pixel(window, x=x, y=7, color="darkgreen", size=PIXEL_SIZE)
