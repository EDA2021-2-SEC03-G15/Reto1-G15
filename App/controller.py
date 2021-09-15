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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de artistas

def initCatalog(tipo):

    catalog = model.newCatalog(tipo)
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)

def loadArtists(catalog):
    """
    Carga los artistas del archivo.
    """
    artistsfiles = cf.data_dir + "Artists-utf8-large.csv"
    input_file = csv.DictReader(open(artistsfiles, encoding="utf-8"))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga las obras del archivo.
    """
    artworksfiles = cf.data_dir + "Artworks-utf8-large.csv"
    input_file = csv.DictReader(open(artworksfiles, encoding="utf-8"))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

##crea una lista de artistas nacidos entre dos fechas dadas por parametro

def listarArtistas(catalog, inicio, fin):

    rango_artistas = lt.newList(datastructure="ARRAY_LIST")

    i = 0
    while i<=lt.size(catalog["artists"]):

        artista = lt.getElement(catalog["artists"], i)
        fechaInicial = int(lt.getElement(catalog["artists"], i)["BeginDate"] )
        if fechaInicial != 0:
            if (fechaInicial>= inicio) and (fechaInicial <= fin):
                lt.addLast(rango_artistas, artista)
        i+=1

    lista = []

    for i in range (0, lt.size(rango_artistas)):
        lista.append(lt.getElement(rango_artistas, i))

    return lista
        

# Funciones de ordenamiento

def ordenarArtistas(catalog, inicio, fin):

    return model.ordenarArtistas(listarArtistas(catalog, inicio, fin))

def sortArtworksByDateAcquired(catalog, size, alg):

    return model.sortByDate(catalog, size, alg)

# Funciones de consulta sobre el catálogo