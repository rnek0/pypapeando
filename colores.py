#!/usr/bin/env python


class Estilo:
    """Estilo de texto, bold, italic..."""
    bold = '1m'
    italic= '3m'
    underline= '3m'
    strike= '3m'
    reset = '0m'

class Color:
    """Algunos colores"""
    fg = 7          # white
    verde = 46      #"\x1b[38;25;46m"
    azul = 25       #"\x1b[38;25;25m"
    rojo = 9        #"\x1b[38;25;9m"
    naranja = 166   #"\x1b[38;25;166m"
    gris = 235      #"\x1b[38;25;235m"
    reset = 0       #'\x1b[0m'
    colors = [fg,verde, azul, rojo,reset]



class TUI:

    @classmethod
    def all_colors(cls):
        for i in range(1,255):
            print(f"\x1b[38;5;{i}m{i}", end= " ")

    def color(self, u_char):
        """Return ASCII color code from int between 0-255"""
        return f"\x1b[38;5;{u_char}m"

    def __init__(self, element="", color=0):
        self._element = element
        if color:
            self._color = color
        else:
            self._color = Color.fg # ascii reset color code (here int 0)
            
        self.escribe(element,self._color)
    
    @classmethod
    def reset(cls):
        return Color.reset

    @classmethod
    def colorea(cls, str, color):
        return f"\x1b[38;5;{color}m{str}\x1b[0m"

    def con_color(funcion):
        # escribe tiene un parámetro opcional, se debe especificar aquí también.
        def envoltura(self,texto, _color=Color.fg):  
            # print('\nEntrando en la envoltura\n')
            str_color =  self.color(_color)       #f"\x1b[38;5;{_color}m"
            str_reset =  self.color(Color.reset)  #f"\x1b[{Color.reset}m"
           
            funcion(self, str_color + texto + str_reset, str_color)
            # print('\nSaliendo de la envoltura\n')
        return envoltura

    @con_color
    def escribe(self,texto,color=Color.fg):
        """TUI.escribe() Escribe una string con el color pasado en parametro"""
        self._color = color
        print(f"{texto}\x1b[0m", end= " ")

        