#!/usr/bin/env python3
# Ejercicios de entrenamiento en el curso de Python Ofensivo hack4u.io
# 14-03-2024 / rnek0

class Producto:
    """Compra.\n- nombre\n- categoria\n -precio"""

    """Lista de productos adquiridos"""
    compras = []
    """tamaño máximo del separador nombre/precio"""
    max_string_lenght = 2


    @classmethod
    def talla_str_nombre(cls,str_lenght):
        if str_lenght > Producto.max_string_lenght:
            cls.max_string_lenght = str_lenght


    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.compras.append(self)
        Producto.talla_str_nombre(len(self.nombre))


    @classmethod
    def display_compra(cls,compras):
        for i, producto in enumerate(compras):
            print(f" + {i + 1} : {producto}")
        

    @classmethod
    def total(cls):
        return sum(list(map( lambda x: x.precio , cls.compras)))


    def __str__(self):
        sep = (Producto.max_string_lenght - len(self.nombre))*' '
        return f"[P] {self.nombre} {sep} Precio : {self.precio:>5.2f} €"

class Banner:
    """Display banner app"""
    title = """\t  __      __________  __  _______  ____  ___   _____    __  
\t / /     / ____/ __ \/  |/  / __ \/ __ \/   | / ___/    \ \ 
\t/ /     / /   / / / / /|_/ / /_/ / /_/ / /| | \__ \      \ \\
\t\ \    / /___/ /_/ / /  / / ____/ _, _/ ___ |___/ /      / /
\t \_\   \____/\____/_/  /_/_/   /_/ |_/_/  |_/____/      /_/ """
    
    @classmethod
    def display_banner(cls):
        return f"\n{cls.title}\n"

if __name__ == "__main__":
    print(Banner.display_banner())
    
    # Initialize buying products / Inicializar la compra de productos
    agua = Producto("Perrier", "bebidas", 1.55)
    jamon = Producto("Jamon Serrano", "tapitas", 8.80)
    pizza = Producto("Margarita","comida", 14.50)
    café = Producto("Café", "bebidas", 5.90)

    # Shows purchases / Muestra compras
    Producto.display_compra(Producto.compras)

    print(f"\n Total : {Producto.total()} €\n")