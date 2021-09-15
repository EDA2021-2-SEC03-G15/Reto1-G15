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
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
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
    print("0- Salir")

def menuTAD():
    print("Seleccione el tipo de TAD sobre el que quiere cargar los archivos")
    print("1. Arraylist")
    print("2. Single Linked List")

def menuOrd():
    print("Seleccione el algoritmo de ordenamiento que desea usar:")
    print("1. Insertion")
    print("2. Mergesort")
    print("3. Quicksort")
    print("4. Shellsort")

catalog = None

def initCatalog(tipo):

    return controller.initCatalog(tipo)

def loadArtists(catalog):

     return controller.loadArtists(catalog)

def loadArtworks(catalog):

    return controller.loadArtworks(catalog)

def listarArtistas(catalog, inicio, fin):
    
    return controller.listarArtistas(catalog, inicio, fin)

def ordenarArtistas(catalog, inicio, fin):

    return controller.ordenarArtistas(catalog, inicio, fin)

def sortArtworksByDateAcquired(catalog, size, alg):

    return controller.sortArtworksByDateAcquired(catalog, size, alg)
"""
Menu principal
"""


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:

        menuTAD()
        inputATD = input("Seleccione: \n")

        print("Cargando información de los archivos ....")
        if int(inputATD[0]) == 1:

            catalog = initCatalog("ARRAY_LIST")
        
        else:

            catalog = initCatalog("SINGLE_LINKED")


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

        print("Digite las fechas inciales y finales a consultar")
        date1 = int(input("Año inicial: " ))
        date2 = int(input("Año final: " ))
        lista = listarArtistas(catalog, date1, date2)

        print("Hay ", lt.size(lista), "artistas en el rango de ", date1, "y ", date2)
        print("================================================================")
        print("Los primeros 3 y ultimos 3 artistas del rango son:")
        for i in range(1, lt.size(lista)):
            if i < 4:
                print("--------------------------------------------------------")
                print (lt.getElement(lista, i))
        for i in range (lt.size(lista)-3, lt.size(lista)):
            if i <= lt.size(lista):
                print("--------------------------------------------------------")
                print(lt.getElement(lista, i))

    elif int(inputs[0]) == 3:

        size = int(input("Seleccione el tamaño de la muestra: \n"))
        menuOrd()
        inputOrd = int(input("Seleccione el algoritmo: \n"))
        lista_ordenada = sortArtworksByDateAcquired(catalog, size, inputOrd)
        x,y = lista_ordenada
        print(x)
        
    else:
        sys.exit(0)
sys.exit(0)
