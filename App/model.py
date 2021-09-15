"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from decimal import Rounded
from DISClib.DataStructures.arraylist import subList
import config as cf
import controller
import time
from datetime import date
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qc
from DISClib.Algorithms.Sorting import shellsort as sh
from DISClib.ADT import stack as sdt
assert cf
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):

    catalog = {"artists":None, 
               "artworks": None,
               }
    
    catalog["artists"] = lt.newList(tipo)

    catalog["artworks"] = lt.newList(tipo)

    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog["artists"], artist)

def addArtwork(catalog, artwork):

    lt.addLast(catalog["artworks"], artwork)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareBeginDate(artist1, artist2):
    
    return (int(artist1["BeginDate"])<int(artist2["BeginDate"]))


def cmpArtWorkByDateAcquired(artwork1, artwork2):

    
    fecha1 = artwork1['DateAcquired']
    fecha2 = artwork2['DateAcquired']

    if fecha1 == "":
        fecha1 = '1700-01-01'
    if fecha2 == "": 
        fecha2 = '1700-01-01'

    dt1 = date.fromisoformat(fecha1)
    dt2 = date.fromisoformat(fecha2)

    return (dt1<dt2)
# Funciones de ordenamiento

##Ordena los artistas por el metodo quicksort
def ordenarArtistas(lista):

    return mg.sort(lista, compareBeginDate)

def sortByDate(catalog, size, alg):

    sub_list = lt.subList(catalog["artworks"], 1, size)
    sub_list = sub_list.copy()
    elapsedtime = 0

    if alg == 1:
        start_time = time.process_time()
        sorted = ins.sort(sub_list, cmpArtWorkByDateAcquired)
        stop_time = time.process_time()
        elapsedtime += (stop_time - start_time)*1000
    
    elif alg == 2:
        start_time = time.process_time()
        sorted = mg.sort(sub_list, cmpArtWorkByDateAcquired)
        stop_time = time.process_time()
        elapsedtime += (stop_time - start_time)*1000

    elif alg == 3:
        start_time = time.process_time()
        sorted = qc.sort(sub_list, cmpArtWorkByDateAcquired)
        stop_time = time.process_time()
        elapsedtime += (stop_time - start_time)*1000

    elif alg == 4:        
        start_time = time.process_time()
        sorted = sh.sort(sub_list, cmpArtWorkByDateAcquired)
        stop_time = time.process_time()
        elapsedtime += (stop_time - start_time)*1000

    return round(elapsedtime, 2), sorted

