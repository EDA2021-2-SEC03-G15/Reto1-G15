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

from DISClib.ADT.queue import newQueue
from DISClib.ADT.indexminpq import size
from decimal import Rounded
from DISClib.DataStructures.arraylist import newList, subList
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
from DISClib.ADT import queue as q
assert cf
import math
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
def FindIDArtist(catalog, nombre):
    
    artistas = catalog["artists"]
    c = False
    while c == False:
        for i in range(lt.size(artistas)):
            x = lt.getElement(artistas, i)
            if x['DisplayName'] == nombre:
                IDArtista = x['ConstituentID']
                c = True
    
    return IDArtista

def contar_tecnicas(obrasArtista):

    tecnicas = lt.newList(datastructure="ARRAY_LIST")
    for i in range(lt.size(obrasArtista)):
        artwork = lt.getElement(obrasArtista, i)
        if lt.isPresent(tecnicas, artwork["Medium"]) == 0:
            lt.addLast(tecnicas, artwork["Medium"])
    tecnicas = lt.size(tecnicas)

    return tecnicas

def tecnica_mas_usada(obrasArtista):

    tecnica_mas_usada = lt.newList(datastructure="ARRAY_LIST")
    obras = obrasArtista["elements"]
    dic = {}
    x = ""
    for obra in range(len(obras)):
        iguales = 0
        #(obras[obra]["Medium"])
        for obra1 in range(len(obras)):
            if obras[obra]["Medium"] == obras[obra1]["Medium"]:
                iguales += 1   
        dic[obras[obra]["Medium"]] = iguales
    mayor = 0 
    obramayor = ""    
    for llave in dic:
        if dic[llave] > mayor:
           mayor = dic[llave]
           obramayor = llave
    letra = {obramayor:mayor} 

    return obramayor
     
def obras_tecnicaUsada(obrasArtista, obramayor):
    obrasA = obrasArtista["elements"]
    obras = lt.newList(datastructure='ARRAY_LIST')

    for i in range(len(obrasA)):
        if obrasA[i]["Medium"] == obramayor:
            lt.addLast(obras, obrasA[i])
    obrasTecnica = obras["elements"]
    return obrasTecnica


# Funciones utilizadas para comparar elementos dentro de una lista
def compareBeginDate(artist1, artist2):
    
    return (int(artist1["BeginDate"])<int(artist2["BeginDate"]))

def compareAlphabetically(artwork1, artwork2):

    return (str(artwork1["Title"])<str(artwork2["Title"]))

def comparebyConsID(art1, art2):

    return (str(art1["ConstituentID"])<str(art2["CostituentID"]))

def compareByCosts(art1,art2):

    return (int(art1["Cost"])>int(art2["Cost"]))


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

def sortByDate(catalog, alg):

    sub_list = lt.subList(catalog["artworks"], 1, (lt.size(catalog["artworks"])))
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


    return sorted

def sortByNacionality(catalog):
    #"ConstituentID"
    artworks = lt.newList(datastructure="ARRAY_LIST")
    aux_dict = dict()
    contadora = 0
    i = 1
    artistas_sort=mg.sort(catalog["artists"],sortByNacionality)
    while i<=lt.size(catalog["artworks"]):
        j = 1

        while j<=lt.size(catalog["artists"]):
            
            a = lt.getElement(catalog["artworks"], i)['ConstituentID'][1:-1]
            if ',' in a:
                for id in range(len(a.split(','))):
                    if id == 0: 
                        if a.split(',')[id] == lt.getElement(catalog["artists"], j)['ConstituentID']:
                            contadora+=1
                            aux_dict[lt.getElement(catalog["artists"], j)['Nationality']] = aux_dict.get(lt.getElement(catalog["artists"], j)['Nationality'],0) + 1
                            if str(lt.getElement(catalog["artists"],j)["Nationality"]).lower()=="american":
                                lt.addLast(artworks,lt.getElement(catalog["artworks"], i))
                    else:
                        if a.split(',')[id][1:] == lt.getElement(catalog["artists"], j)['ConstituentID']:
                            contadora+=1
                            aux_dict[lt.getElement(catalog["artists"], j)['Nationality']] = aux_dict.get(lt.getElement(catalog["artists"], j)['Nationality'],0) + 1
                            if str(lt.getElement(catalog["artists"],j)["Nationality"]).lower()=="american":
                                lt.addLast(artworks,lt.getElement(catalog["artworks"], i))
            else:
                if lt.getElement(catalog["artworks"], i)['ConstituentID'][1:-1] == lt.getElement(catalog["artists"], j)['ConstituentID']:
                    contadora+=1
                    aux_dict[lt.getElement(catalog["artists"], j)['Nationality']] = aux_dict.get(lt.getElement(catalog["artists"], j)['Nationality'],0) + 1
                    if str(lt.getElement(catalog["artists"],j)["Nationality"]).lower()=="american":
                         lt.addLast(artworks,lt.getElement(catalog["artworks"], i))

            
            j+=1

        i+=1
    sorted = mg.sort(artworks, compareAlphabetically)
    print (lt.size(sorted))
    z = 0

    for nationality in aux_dict:
        if z<=9:
            print ("%-20s %4.1f" % (nationality, aux_dict[nationality]))
        z+=1
    return sorted


def transportRules(catalog, department):

    listawCosts = lt.newList("ARRAY_LIST")
    aw = catalog["artworks"]
    i = 1
    total_obras =  0
    costo_total = 0
    while i <= lt.size(aw):
        awactual = lt.getElement(aw, i)
        if awactual["Department"]==department :
            costo = 48
            total_obras += 1
            if awactual["Diameter (cm)"]!="":
                r = float(awactual["Diameter (cm)"])/200
                area = (math.pi)*(r)**2
                costo = area*72
            
            if awactual["Height (cm)"]!="" and awactual["Width (cm)"]!="":
                if awactual["Height (cm)"]!="0" and awactual["Width (cm)"]!="0":

                    h = float(awactual["Height (cm)"])/100
                    w = float(awactual["Width (cm)"])/100
                    area = h*w
                    costo = area*72

            if awactual["Depth (cm)"] !="" and awactual["Depth (cm)"] !="0":
                if i == 47:
                        print("")
                d = (float(awactual["Depth (cm)"]))/100
                h = (float(awactual["Height (cm)"]))/100
                w = (float(awactual["Width (cm)"]))/100
                if h == 0:
                    area = d * w
                    costo = area*72
                if w == 0:
                    area = d * h
                    costo = area*72
                vol = d*w*h
                costov = vol*72
                if costov > costo:
                    costo = costov

            if awactual["Weight (kg)"]!="":

                we = float(awactual["Weight (kg)"])
                costop = we * 72
                if costop > costo:
                    costo = costop
                if costop > costov:
                    costo = costop
                elif costov > costop:
                    costo = costov
            
            awactual["Cost"] = round(costo,2)

            if awactual["Cost"] == "0":
                awactual["Cost"] == 48
            
            costo_total += costo
            
            lt.addLast(listawCosts, awactual)
        i+=1

    sorted = mg.sort(listawCosts, compareByCosts)
    mensaje = "Se transportarán ", total_obras, "obras por un costo de ", costo_total, "USD"
    print (mensaje)
    for i in range(1, lt.size(sorted)):
        if i < 4:
            print("--------------------------------------------------------")
            print (lt.getElement(sorted, i))
    return sorted
    