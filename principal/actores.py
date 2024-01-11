import json
actores = []
def cargarActores(actores):
    try:
        with open('actores', 'r') as archivo:
         return json.load(archivo)
    except FileNotFoundError:
        actores = []
        return actores
    finally:
        return ("no se encontro ningun archivo")

def crearActores(actores):
    id_actor = int(input("ingrese el id del actor"))
    new_actor = input("ingrese nombre del actor")
    nuevoActor =  {'id' : id_actor,'actor' : new_actor}
    actores.append(nuevoActor)
   
    with open('actores.json', 'w') as archivo:
            json.dump(actores, archivo, indent=4)

def listar_Actores (actores):
   print("los actores son")
   for f, x in enumerate(actores):
      print(f)
      print(x)


