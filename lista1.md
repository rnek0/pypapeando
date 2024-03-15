# Sobre lista de compras

> [Utilidad](main.py) que encapsula la creación y gestión de una lista de objetos de tipo Producto.  

Ejercicio personal que trata de poner en practica las nociones de POO impartidas en [hack4u.io](https://hack4u.io/cursos/python-ofensivo)

Podemos apreciar que no se trata de un "modulo de biblioteca" con el ```if __name__ == '__main__':``` en la linea [55](https://github.com/rnek0/pypapeando/blob/6e047405f940653ad7dc8149f33a9a35f907c170/main.py#L55)  
Un **modulo de biblioteca** es un fichero *.py exterior al fichero main.py (en este caso) que es el punto inicial del programa y situado en el mismo directorio. El modulo de biblioteca puede ser importado para aportar funcionalidad extra pero no sera el punto de partida de la aplicación.  
Un **package** est un grupo de módulos que están agrupados en una sola entidad (dentro de un directorio)

## Clases

Dos clases

- [Producto](https://github.com/rnek0/pypapeando/blob/6e047405f940653ad7dc8149f33a9a35f907c170/main.py#L5)
- [Banner](https://github.com/rnek0/pypapeando/blob/6e047405f940653ad7dc8149f33a9a35f907c170/main.py#L43)

#### Producto 

* Un constructor [```__init__```](https://github.com/rnek0/pypapeando/blob/6e047405f940653ad7dc8149f33a9a35f907c170/main.py#L20) :
  1. inicializa el objeto Producto on nombre categoría y precio. **self** hace referencia al objeto en si mismo. Ver recomendación en [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/#function-and-method-arguments)
  2. añade el objeto a la lista de compras **compras**
  3. llama a la **@classmethod** [talla_str_nombre](https://github.com/rnek0/pypapeando/blob/6e047405f940653ad7dc8149f33a9a35f907c170/main.py#L15) pasándole la longitud de la variable nombre del objeto para calcular la tabulación disponible en una variable de clase **variable sep** que sera utilizada en el método ```__self__``` el cual se encarga de dar un aspecto visual al objeto de tipo Producto.

* Un **@classmethod** (método de clase) llamado [total](https://github.com/rnek0/pypapeando/blob/6e047405f940653ad7dc8149f33a9a35f907c170/main.py#L35) que calcula la adicion de los precios con una [funcion lambda](https://github.com/rnek0/pypapeando/blob/6e047405f940653ad7dc8149f33a9a35f907c170/main.py#L36).

* El metodo de clase [**display_compra**](https://github.com/rnek0/pypapeando/blob/6e047405f940653ad7dc8149f33a9a35f907c170/main.py#L29) se encarga de la salida por pantalla de la lista de productos.
---

 #### Banner 

 Una clase estatica (sin constructor __init__) para mostrar un banner

 - una variable
 - un metodo de clase
