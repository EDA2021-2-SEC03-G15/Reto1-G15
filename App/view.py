"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""



def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente artistas")
    print("3- Listar cronológicamente artworks")
    print("4- Clasificar obras de un artista por técnica")
    print("5- Clasificar obras de un artista por nacionalidad")
    print("6- Transportar obras")
    print("7- Proponer exposicion")

catalog = None

def initCatalog():

    return controller.initCatalog()

def loadArtists(catalog):

     return controller.loadArtists(catalog)

def loadArtworks(catalog):

    return controller.loadArtworks(catalog)
"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()

        loadArtists(catalog)
        loadArtworks(catalog)
         
        print("Artistas Cargados " + str(lt.size(catalog["artists"])))
        print("Artworks cargados " + str(lt.size(catalog["artworks"])))
        
        print("Últimos 3 Artistas")
        i = 2
        while i >= 0:
            print (str(lt.getElement((catalog["artists"]), lt.size(catalog["artists"])-i)))
            i-=1
        
        print("Ultimos 3 Artworks")
        j = 2
        while j >= 0:
            print (str(lt.getElement((catalog["artworks"]),lt.size(catalog["artworks"])-j)))
            j-=1
  

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
