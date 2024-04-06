#!/usr/bin/env python

class Python:                 # Clase : es un 'molde o plantilla' que describe 
                              # los atributos y métodos del objeto que se puede crear a partir de ella.
    """POO Python."""
    def __init__(self, lang): # Constructor : metodo que permite la instanciación del objeto de clase.
        self.lang = lang      # self : palabra reservada que hace referencia al objeto en si mismo.
    
    def __str__(self):        # Retorna la descripción del objeto (metodo decorador).
        return f"{self.lang} : {type(self)}" 
        
if __name__ == "__main__":
    python = Python("Python")
    print(python)
    