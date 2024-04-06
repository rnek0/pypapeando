#!/usr/bin/env python3
# Ejercicios de entrenamiento en el curso de Python Ofensivo hack4u.io
# 06-04-2024 / rnek0

from colores import *
import time

class Stock:
    """Class Stock. Stock de productos en venta"""
    _stock = {}

    def __init__(self, producto=None,cantidad=0):
        self._stock = {"Perrier":[2,"bebidas",1.55], "Jamon Serrano":[3,"tapitas",8.80], "Reina":[2,"pizza",14.00], "Café":[10,"bebidas",5.90], "Cocacola":[8,"bebidas",2.80]}
        self.venta = TUI.colorea(f"[-]", Color.gris)
        if producto:
            self.producto = producto
            self.cantidad = cantidad
            self.poner_en_stock(producto,cantidad)
    
    @property
    def stock(self):
        """Retorna un diccionario de productos en stock"""
        return dict(self._stock)

    @stock.setter
    def stock(self):
        pass

    def __str__(self):
        return f" Stock de productos: {type(self)}\n {self.stock}"

    def poner_en_stock(self,producto, cantidad=1):
        """Añadir un producto al stock"""
        if en_stock(producto):
            self._stock[producto] = self._stock[producto].value + cantidad # update available number of products
        else:
            self._stock[producto] = cantidad # add new product


    def vender(self, producto,cantidad):
        """Stock.vender() : Venta de un producto por cantidad.\nRetourne le produit vendu."""
        venta = False;
        print(f"\t [-] vendiendo : {producto} / {cantidad}")
        for k,v in self.stock.items():
            if k == producto and v[0] - cantidad >= 0 :
                self._stock[producto][0] = v[0] - cantidad # update available quantity of products
                conseguido = TUI.colorea(f"[+]",Color.verde)
                print(f"\t {conseguido} Producto {producto} vendido. " f" ([{self._stock[producto][0]}] en stock)", sep="/")

                if self._stock[producto][0] == 0:
                    sacando = TUI.colorea(f"\t >>> Sacando {producto} del stock.", Color.gris)
                    print(f"{sacando}")
                    p = self._stock.pop(producto)
                    
                venta = True;

        if venta:
            return producto
        else:
            return ""

    
    def en_stock(self,producto,cantidad):
        """Stock.en_stock() : Saber si hay un producto disponible (True)"""
        disponible = False
        for k, v in self._stock.items():
            if k == producto and cantidad <= v[0]:
                return True
                #disponible = True
                #break
                
        return disponible


class Producto:
    """Compra.\n- nombre\n- categoria\n -precio\n -cantidad"""

    """Lista de productos adquiridos"""
    compras = []
    """tamaño máximo del separador nombre/precio"""
    max_string_lenght = 2

    @classmethod
    def talla_str_nombre(cls,str_lenght):
        if str_lenght > Producto.max_string_lenght:
            cls.max_string_lenght = str_lenght

    # Ctor. -----------------------------------------------------
    def __init__(self, stock, nombre, categoria, precio,cantidad,tui):

        self.stock = stock
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        self.tui = tui
        

        # Mejor poner esto en variables de clase y no de instancia.
        self.alert = TUI.colorea(f"[!]",Color.rojo) 
        self.pregunta = TUI.colorea(f"[?]",Color.naranja)
        self.conseguido = TUI.colorea(f"[+]",Color.verde)
        self.si = TUI.colorea(f"si", Color.verde)
        self.no = TUI.colorea(f"no", Color.rojo)
        self.venta = TUI.colorea(f"[-]", Color.gris)

        Banner.title_section(nombre)

        if self.stock.en_stock(nombre,cantidad):
            self.adquirir(self.nombre,self.cantidad)
            self.compras.append(self)
        else:
            p = TUI.colorea(f"{self.nombre}",Color.rojo) 
            print(f"\t {self.alert} El producto {p} no esta disponible.")
            if input(f"\t {self.pregunta} Comprar algo parecido: {self.si} / {self.no} ?  ") == 'si':

                for k,v in self.stock.stock.items():
                    if v[1] == self.categoria:
                        menu = TUI.colorea(f" Menu : {v[1]} !!!",Color.naranja)
                        tenemos = TUI.colorea(f" [{v[0]}] {k}",Color.verde)
                        print(f"\t {self.pregunta}{menu}\n\t Tenemos : {tenemos} ; Precio unidad : {v[2]} €")        
                        if input(f"\t Comprar {k}: {self.si} / {self.no} ?  ") == 'si':
                            cuantos_productos = int(input("\t Cantidad deseada : "))
                            if cuantos_productos <= v[0]:
                                print(f"\t {self.conseguido} Pedido de {cuantos_productos} {k}...")
                                time.sleep(1)
                                print(f"\t {self.conseguido} Efectuado.")
                                time.sleep(2)
                                if self.stock.en_stock(k,cuantos_productos):
                                    Banner.title_section(k)
                                    
                                    if self.adquirir(k,cuantos_productos):
                                        self.nombre = k
                                        self.categoria = v[1]
                                        self.precio = v[2]
                                        self.cantidad = cuantos_productos
                                        self.compras.append(self)
                                        
                                    else:
                                        break    
                            else:
                                print(f"\t {self.alert} Solo podemos vender {v[0]} {k}.\n\tCancelando la compra de {k}.")
                                time.sleep(2)

        Producto.talla_str_nombre(len(self.nombre))
        print()

    def adquirir(self, nombre,cantidad):
        """Producto.adquirir() Proceso de adquisición de la cantidad de productos deseados"""

        result = False
        print(f"\t {self.venta} {cantidad} {nombre} en venta...")
        if self.stock.vender(nombre, cantidad) != "":
            tui.escribe(f"\t .......{self.conseguido} {cantidad} {nombre} en el carrito 🛒", Color.verde)
            result = True

        return result
        
        
    @classmethod
    def display_compra(cls):
        """Saca la nota de productos adquiridos"""
        #tui.escribe(f"\n\t --- COMPRAS : ---\n", Color.azul)
        Banner.title_section("COMPRAS :")
        i = 0
        for p in list(enumerate(cls.compras)):
            #print(f"\t + {i + 1} : {producto}")
            i += 1
            total = p[1].cantidad * p[1].precio
            print(f"\t + {i} : {p[1].nombre:<15} / {p[1].cantidad} * {round(p[1].precio,2):>0.2f} = {total:>5.2f} €")
        
        Banner.title_section("TOTAL :")
        total_compras = cls.total()
        total_compras = TUI.colorea(f"{total_compras}",Color.rojo)
        print(f"\t Total : {total_compras} €\n")

    @classmethod
    def total(cls):
        """Calcula el total de la nota"""
        return sum(list(map( lambda x: x.precio * x.cantidad , cls.compras)))


    def __str__(self):
        sep = (Producto.max_string_lenght - len(self.nombre))*' '
        return f"[P] {self.nombre} {sep} Precio : {self.precio:>5.2f} €"

class Banner:
    """Display banner app"""
    title = """
\t  __      __________  __  _______  ____  ___   _____    __  
\t / /     / ____/ __ \/  |/  / __ \/ __ \/   | / ___/    \ \ 
\t/ /     / /   / / / / /|_/ / /_/ / /_/ / /| | \__ \      \ \\
\t\ \    / /___/ /_/ / /  / / ____/ _, _/ ___ |___/ /      / /
\t \_\   \____/\____/_/  /_/_/   /_/ |_/_/  |_/____/      /_/ \n"""
    
    @classmethod
    def display_banner(cls):
        return f"{cls.title}\n"

    @classmethod
    def title_section(cls,title):
        tui.escribe(f"\n\t *** {title}", Color.azul)
        line = '*'*58
        tui.escribe(f"\n\t {line} \n", Color.azul)


if __name__ == "__main__":
    #TUI.all_colors() # Para buscar colores.
    tui = TUI()
    tui.escribe(Banner.display_banner(), Color.azul)
    
    stock = Stock()
    #tui.escribe(f"{stock}\n") # Para ver el mock

    # Initialize buying products / Inicializar la compra de productos
    agua = Producto(stock,"Perrier", "bebidas", 1.55, 2,tui)
    cocacola = Producto(stock,"Cocacola", "bebidas", 2.80, 4,tui)
    jamon = Producto(stock,"Jamon Serrano", "tapitas", 8.80, 2,tui)
    pizza = Producto(stock,"Margarita","pizza", 14.50, 1,tui)
    café = Producto(stock,"Café", "bebidas", 5.90, 2,tui)


    # Shows purchases / Muestra compras
    Producto.display_compra()