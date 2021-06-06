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
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización de la estructura

def createCatalog():
    structure = model.initStructure()
    catalog_plusinfo = loadInfo(structure)
    return catalog_plusinfo

# Funciones para la carga de datos

def loadInfo(structure):
    
    countries_count = 0
    last_country = None
    countriesFile = cf.data_dir + 'countries.csv'
    countriesData = csv.DictReader(open(countriesFile, encoding="utf-8"),
                                delimiter=",")
    for country in countriesData:
        structure = model.addCountry(country, structure)
        countries_count += 1
        if countries_count == 238:
            last_country = country
    countries_info = {'last': last_country, 'count': countries_count}

    lpoints_count = 0
    first_lpoint = None
    lpointsFile = cf.data_dir + 'landing_points.csv'
    lpointsData = csv.DictReader(open(lpointsFile, encoding="utf-8"),
                                delimiter=",")
    for lpoint in lpointsData:
        structure = model.addLpoint(lpoint, structure)
        lpoints_count += 1
        if lpoints_count == 1:
            first_lpoint = lpoint

    lpoints_info = {'first': first_lpoint, 'count': lpoints_count}

    connections_count = 0    
    connectionsFile = cf.data_dir + 'connections.csv'
    connectionsData = csv.DictReader(open(connectionsFile, encoding="utf-8-sig"),
                                delimiter=",")
    for connection in connectionsData:
        structure = model.addConnection(connection, structure)
        connections_count += 1
    connections_info = connections_count

    return [structure, [countries_info, lpoints_info, connections_info]]

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo


