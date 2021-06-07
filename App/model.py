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
from DISClib.Algorithms.Graphs import bellmanford as bmf
from DISClib.Algorithms.Graphs import dijsktra as djk
assert cf
import sys
sys.path.append('d:/apps/anaconda/anaconda_install/lib/site-packages')
import haversine
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
    
    originp = mp.get(structure['landing_points'], origin)
    originll = (float(originp['value']['latitude']), float(originp['value']['longitude']))
    destinationp = mp.get(structure['landing_points'], destination)
    destinationll = (float(destinationp['value']['latitude']), float(destinationp['value']['longitude']))
    length = round(haversine.haversine(originll, destinationll), 2)

    edge = gr.getEdge(structure['connections'], origin, destination)
    if edge is None:
        gr.addEdge(structure['connections'], origin, destination, length)
    
    return structure
        


# Funciones para creacion de datos

# Funciones de consulta

def req1(catalog):
    pass


def req2(catalog):
    points = mp.valueSet(catalog['landing_points'])
    points_list = lt.newList()
    for point in lt.iterator(points):
        amount = gr.degree(catalog['connections'], point['landing_point_id'])
        if len(point['name'].split(",")) > 1:
            element = {'name': str(point['name']), 'country': str((point['name'].split(",")[1])), 'id': point['landing_point_id'], 'amount': amount}
        else:
            element = {'name': str(point['name']), 'country': str(point['name']), 'id': point['landing_point_id'], 'amount': amount}
        lt.addLast(points_list, element)
    return points_list


def req3(catalog, pointA, pointB):
    execution = djk.Dijkstra(catalog['connections'], pointA)
    distance = djk.distTo(execution, pointB)
    path = djk.pathTo(execution, pointB)
    return (path, distance)
    

def req5(catalog, lpoint):
    points = gr.adjacents(catalog['connections'], lpoint)
    points_list = lt.newList()
    for adjacent in lt.iterator(points):
        distance = (gr.getEdge(catalog['connections'], lpoint, adjacent))['weight']
        name = ((mp.get(catalog['landing_points'], adjacent))['value']['name'].split(","))[1]
        if not lt.isPresent(points_list, [name, distance]):
            lt.addLast(points_list, [name, distance])
    sorted_points = sa.sort(points_list, cmpPointslist)
    return sorted_points


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

def cmpPointslist(p1, p2):
    if (p1[1] == p2[1]):
        return 0
    elif (p1[1] < p2[1]):
        return 1
    else:
        return -1
