import json
generos =[]
def cargarGeneros(generos):
    try:
        with open('generos', 'r') as archivo:
         return json.load(archivo)
    except FileNotFoundError:
        generos = []
        return generos
    finally:
        return ("no se encontro ningun archivo")


def crearGeneros(generos):
    id_genero = int(input("ingrese el id del genero"))
    new_genero = input("ingrese nombre del genero")
    nuevoGenero =  {'id' : id_genero,'genero' : new_genero}
    generos.append(nuevoGenero)
   
    with open('generos.json', 'w') as archivo:
            json.dump(generos, archivo, indent=4)

def listar_generos (generos):
   print("los generos son")
   for f, x in enumerate(generos):
      print(f)
      print(x)

