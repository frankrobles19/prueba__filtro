import json
peliculas =[]
def cargarpeliculas(peliculas):
    try:
        with open('peliculas', 'r') as archivo:
         return json.load(archivo)
    except FileNotFoundError:
        peliculas = []
        return peliculas
    finally:
        return ("no se encontro ningun archivo")


def crearpeliculas(peliculas):
    try:     
        id_pelicula = int(input("ingrese el id del pelicula"))
        duracion = int(input("ingrese duracion de la pelicula"))
    except ValueError:
        print("ingrese nuemros enteros")
    else:        
        nombre = input("ingrese nombre de la pelicula")
        sinopsis = input("ingrese sinopsis de la pelicula")

        nuevapelicula =  {'id' : id_pelicula,'nombre' : nombre, 'sinopsis' : sinopsis, 'duracion' : duracion}
        peliculas.append(nuevapelicula)
    
        with open('peliculas.json', 'w') as archivo:
                json.dump(peliculas, archivo, indent=4)

def listar_generos (peliculas):
   print("los generos son")
   for f, x in enumerate(peliculas):
      print(f)
      print(x)

