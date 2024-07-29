import pygame
import sys
from pygame.locals import *
from typing import (
    Union
)
from pathlib import Path

PATH = Path(__file__).parent
IMG = PATH / "img"
SOUND_FOLDER = PATH / "sound"




class Rectangle:
    def __init__(
            self, 
            surface: pygame.Surface, 
            width: int = 100, 
            height:int = 100, 
            x: int = 10, 
            y: int = 10, 
            color: tuple=(0,0,0), 
            border_radius: int=0,
            thickness: int=0
    ) -> None:
        """initialize this rect"""
        self.surface = surface
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y
        self.__color = color
        self.__border_radius = border_radius
        self.__thickness = thickness


    def draw(self, thickness=0):
        """draw a rect"""

        if thickness:
            self.__thickness = thickness
            self.__color = "#dc90a9"
        
        pygame.draw.rect(
            surface=self.surface,
            color=self.__color,
            rect=(self.__x, self.__y, self.width, self.height),
            border_radius=self.__border_radius,
            width=self.__thickness
        )
        

    def set_coord(self, x, y):
        """sets the coordinates of this rect"""
        self.__x = x
        self.__y = y

        
class Square:
    def __init__(
            self, 
            surface: pygame.Surface, 
            side: int = 100, 
            x: int = 10, 
            y: int = 10, 
            color: tuple=(0,0,0), 
            border_radius: int=0,
            thickness: int=0
    ) -> None:
        pygame.draw.rect(
        surface=surface,
        color=color,
        rect=(x, y, side, side),
        border_radius=border_radius,
        width=0
    )
        
class Circle:
    def __init__(
            self,
            surface: pygame.Surface,
            color: Union[tuple, str] = (255,255,0),
            center_x: Union[int,float] = 0,
            center_y: Union[int,float] = 0,
            radius: Union[int,float] = 50,
            thickness: Union[int,float] = 0
    ):
        pygame.draw.circle(
            surface=surface,
            color=color,
            center=(center_x, center_y),
            radius=radius,
            width=thickness
        )

class Ellipse:
    def __init__(
            self, 
            surface: pygame.Surface, 
            width: int = 100, 
            height:int = 50, 
            x: int = 100, 
            y: int = 100, 
            color: tuple=(255,0,255), 
            border_radius: int=0,
            thickness: int=0
    ) -> None:
        pygame.draw.ellipse(
            surface=surface,
            color=color,
            rect=(x, y, width, height),
            width=thickness
        )

class Picture:
    def __init__(self) -> None:
        pass


class Bms(Picture):
    def __init__(
            self,
            window: pygame.Surface,
            image: Path = IMG / "bms.png",
            x: int=100,
            y: int=100,
            width: int=80,
            height: int=100
    ) -> None:
        super().__init__()
        bms = pygame.image.load(image)
        bms = pygame.transform.scale(bms, (width, height))
        window.blit(bms, (x, y))



class Capybara(Picture):
    def __init__(
            self,
            window: pygame.Surface,
            image: Path = IMG / "capybara.png",
            x: float=100,
            y: float=100,
            width: int=80,
            height: int=100
    ) -> None:
        super().__init__()
        capy = pygame.image.load(image)
        capy = pygame.transform.scale(capy, (width, height))
        window.blit(capy, (x, y))


class Seal(Picture):
    def __init__(
            self,
            window: pygame.Surface,
            image: Path = IMG / "seal.png",
            x: float=100,
            y: float=100,
            width: int=80,
            height: int=100
    ) -> None:
        super().__init__()
        seal = pygame.image.load(image)
        seal = pygame.transform.scale(seal, (width, height))
        window.blit(seal, (x, y))


class Pixel():
    def __init__(
            self,
            sunface: pygame.Surface,
            x: int,
            y: int,
            size: int=50,
            thickness: int=0,
            color: Union[str, tuple]="#ed553b",
    ) -> None:
        self.__surface = sunface
        self.__width = size
        self.__height = size

        self.__center_x = x * self.__width
        self.__center_y = y
        self.__center_y = self.__surface.get_rect().height-self.__center_y*self.__height-self.__height
        
        
        self.__thickness = thickness
        self.__color = color


        pygame.draw.rect(
            surface=self.__surface,
            color=self.__color,
            rect=(self.__center_x, self.__center_y, self.__width, self.__height),
            border_radius=0,
            width=self.__thickness
        )
        pygame.draw.rect(
            surface=self.__surface,
            color="#FFFFFF",
            rect=(self.__center_x, self.__center_y, self.__width, self.__height),
            border_radius=0,
            width=1
        )



class Text():
    def __init__(
            self,
            sunface: pygame.Surface,
            text: Union[str, pygame.Surface],
            center_x: int,
            center_y: int,
    ) -> None:
        self.__text = text
        self.__surface = sunface
        self.__text = text
        self.__center_x = center_x
        self.__center_y = center_y

        font = pygame.font.Font(None, 35)
        self.__text = font.render(self.__text, True, "darkblue")
        self.__surface.blit(self.__text, self.__text.get_rect(center=(self.__center_x, self.__center_y)))

class Message(Rectangle):
    def __init__(
            self, 
            surface: pygame.Surface, 
            width: int = 380, 
            height: int = 250, 
            x: int = 10, 
            y: int = 10, 
            color: tuple = "#ffe8d5", 
            border_radius: int = 0, 
            thickness: int = 0,
            centered: bool=True
    ) -> None:
        super().__init__(surface, width, height, x, y, color, border_radius, thickness)
        self.__centered = centered

    
        if self.__centered: self.center()
        self.draw()
        self.draw(thickness=5)

    def center(self):
        self.set_coord(
            self.surface.get_width()//2 - self.width//2, 
            self.surface.get_height()//2 - self.height//2)