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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT.graph import gr
assert cf
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initStructure():
    catalog = {'contries': None, 'landing_points': None, 'connections': None}
    catalog['countries'] = mp.newMap(numelements=250)
    catalog['landing_points'] = mp.newMap(numelements=1300)
    catalog['lpoints_list'] = lt.newList()
    catalog['connections'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=3300,
                                              comparefunction=cmpConnections)
    return catalog

# Funciones para agregar informacion al catalogo

def addCountry(country, structure):
    name = country['CountryName']
    mp.put(structure['countries'], name, country)
    return structure

def addLpoint(lpoint, structure):
    lpoint_id = lpoint['landing_point_id']
    lpoint_name = lpoint['name']
    mp.put(structure['landing_points'], lpoint_id, lpoint)
    lp = str(lpoint_id) + ";" + str(lpoint_name)
    lt.addLast(structure['lpoints_list'], lp)
    return structure

def addConnection(connection, structure):

    origin = connection['origin']
    if not gr.containsVertex(structure['connections'], origin):
            gr.insertVertex(structure['connections'], origin)

    destination = connection['destination']
    if not gr.containsVertex(structure['connections'], destination):
            gr.insertVertex(structure['connections'], destination)
    
    length = connection['cable_length']
    edge = gr.getEdge(structure['connections'], origin, destination)
    if edge is None:
        gr.addEdge(structure['connections'], origin, destination, length)
    
    return structure
        


# Funciones para creacion de datos

# Funciones de consulta



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

# Funciones de comparación

def cmpConnections(con1, con2in):
    """
    Compara dos estaciones
    """
    con2 = con2in['key']
    if (con1 == con2):
        return 0
    elif (con1 > con2):
        return 1
    else:
        return -1
