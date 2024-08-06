# импорты библиотек
import main
from graphlern import Pixel, Message


# объявление переменных(констант)
GRID_WIDTH = 10
GRID_HEIGHT = 10
PIXEL_SIZE = 50
BACKGROUND_COLOR = "#ffeba1"
SOUND = ""


# координаты x пикселей апельсина

x_coords_when_y_equals_1 = [4, 5, 6, 7]
x_coords_when_y_equals_2 = [3, 4, 5, 6, 7, 8]
x_coords_when_y_equals_3 = [2, 3, 4, 5, 6, 7, 8, 9]
x_coords_when_y_equals_4 = [2, 3, 4, 5, 6, 7, 8, 9]
x_coords_when_y_equals_5 = [2, 3, 4, 5, 6, 7, 8, 9]
x_coords_when_y_equals_6 = [2, 3, 4, 5, 6, 7, 8, 9]
x_coords_when_y_equals_7 = [3, 4, 5, 6, 7, 8]
x_coords_when_y_equals_8 = [4, 5, 6, 7]




# отрисовка
def draw(window):
    # Здесь пиши свой код

    # вкладываем, цикл перебирает, выполняет, повторят, переменная цикла # давить на эти слова

    for x in x_coords_when_y_equals_1:
        Pixel(window, x=x, y=1, color="orange", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_2:
        Pixel(window, x=x, y=2, color="orange", size=PIXEL_SIZE)    
        
    for x in x_coords_when_y_equals_3:
        Pixel(window, x=x, y=3, color="orange", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_4:
        if x == 8:
            Pixel(window, x=x, y=4, color="yellow", size=PIXEL_SIZE)
        else:
            Pixel(window, x=x, y=4, color="orange", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_5:
        if x == 8:
            Pixel(window, x=x, y=5, color="yellow", size=PIXEL_SIZE)
        else:
            Pixel(window, x=x, y=5, color="orange", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_6:
        if x == 6:
            Pixel(window, x=x, y=6, color="green", size=PIXEL_SIZE)
        else:
            Pixel(window, x=x, y=6, color="orange", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_7:
        if x == 5 or x == 6 or x == 7:
            Pixel(window, x=x, y=7, color="green", size=PIXEL_SIZE)
        else:
            Pixel(window, x=x, y=7, color="orange", size=PIXEL_SIZE)

    for x in x_coords_when_y_equals_8:
        if x == 6:
            Pixel(window, x=x, y=8, color="green", size=PIXEL_SIZE)
        else:
            Pixel(window, x=x, y=8, color="orange", size=PIXEL_SIZE)