
from generos import*
from actores import*
from agregarPelicula import*



def menu():
 print("1. sistema gestor de blockboster")
 print("2. sistema gestor de peliculas")
 print("3. salir")

def MenuGestorblockB():
 print("1. administrador de generos")
 print("2. administrador de actores")
 print("3. administrador de formatos")
 print("4. gestor de informes")
 print("5. gestor de peliculas")
 print("6. volver al menu principal")

def submenuGenemros():
  print("1. crear generos")
  print("2. listar generos")
  print("3. volver al menu")

def submenuActores():
  print("1. crear actores")
  print("2. listar actores")
  print("3. volver al menu")

def MenuPeliculas():
 print("1 .agregar pelicula")
 print("2. editar pelicula")
 print("3. eliminar actor")
 print("4. buscar pelicula")
 print("5. listar todas pelicula")
 print("6. eliminar pelicula")
 print("7. menu principal")



def opmenu():
 while True:
    try:
        menu()
        opmenu = int(input("ingrese una opcion de menu"))
    except ValueError:
      print("solo puede ingresar numeros enteros")
    else:
        if opmenu ==1:
            MenuGestorblockB()
            try:
                opmenu2 = int(input("ingrese una opcion de menu"))
            except ValueError:   
                print("solo puede ingresar numeros enteros")
            else: 
                if opmenu2 ==1:
                    submenuGenemros()
                    try:
                        opmenu3 = int(input("ingrese una opcion de menu"))
                    except ValueError:   
                        print("solo puede ingresar numeros enteros")
                       
                    if opmenu3 ==1:
                        crearGeneros(generos)
                    elif opmenu3 ==2:
                        listar_generos(generos)
                elif opmenu2 ==2:
                    submenuActores()
                    opmenu4 = int(input("ingrese una opcion de menu"))
                    if opmenu4 == 1:
                        crearActores(actores)
                    elif opmenu4 ==2:
                        listar_Actores(actores)
                elif opmenu == 2:
                    MenuPeliculas()
                    opmenu5 = int(input("ingrese una opcion del menu"))
                if opmenu5 ==1:
                    crearpeliculas(peliculas)

            
    
            


          

if __name__=="__main__":
    cargarpeliculas(peliculas)
    cargarActores(actores)
    cargarGeneros(generos)
    
    opmenu()