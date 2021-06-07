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
    print("2- Identificar clústeres de comunicación")
    print("3- Identificar puntos de conexión críticos de la red")
    print("4- Identificar ruta de menor distancia")
    print("5- Identificar infraestructura crítica de la red")
    print("6- Análisis de fallas")
    print("7- Identificar los mejores canañes para transmitir")
    print("8- Identificar la mejor ruta para comunicarse")
    print("0- Salir")

def printInfoCountries(info_countries):
    print("El total de países cargados es de " + str(info_countries['count']))
    print("El último país cargado es " + str(info_countries['last']['CountryName']) + 
          " con población de " + str(info_countries['last']['Population']) + " y " + 
          str(info_countries['last']['Internet users']) + " usuarios de internet")

def printInfoLpoints(info_lpoints):
    print("El total de landing points cargados es de " + str(info_lpoints['count']))
    print("El primer landing point cargado tiene id: " + str(info_lpoints['first']['landing_point_id']) + 
          ", nombre: " + str(info_lpoints['first']['name']) + ", latitud: " + 
          str(info_lpoints['first']['latitude']) + ", longitud: " + str(info_lpoints['first']['longitude']))

def printInfoConnections(info_connections):
    print("La cantidad de conexiones cargadas es de " + str(info_connections))

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        process = controller.createCatalog()
        catalog = process[0]
        info = process[1]
        printInfoCountries(info[0])
        printInfoLpoints(info[1])
        printInfoConnections(info[2])
        
    elif int(inputs[0]) == 2:
        print(" ======================= REQUERIMIENTO 1 ======================= ")
        pass

    elif int(inputs[0]) == 3:
        print(" ======================= REQUERIMIENTO 2 ======================= ")
        points_list = controller.req2(catalog)
        for lpoint in lt.iterator(points_list):
            print(" > " + "Nombre: " + lpoint['name'] + " || País:" + lpoint['country'] + " || ID: " + lpoint['id'] + " || Cables: " +  str(lpoint['amount']))
            
    elif int(inputs[0]) == 4:
        print(" ======================= REQUERIMIENTO 3 ======================= ")
        countryA = input("Ingrese el país A: ")
        countryB = input("Ingrese el país B: ")
        result = controller.req3(catalog, countryA, countryB)
        if result[0] == None:
            print("No hay comunicación entre ambos países")
        else:
            print("La ruta obtenida (por tramos) ha sido:")
            for element in lt.iterator(result[0]):
                print(" > " + element['vertexA'] + " a " + element['vertexB'] + " con una distancia de " + str(element['weight']) + "km")
            print("La distancia total entre ambos países es de " + str(round(result[1], 2)) + "km" )
    elif int(inputs[0]) == 5:
        print(" ======================= REQUERIMIENTO 4 ======================= ")
        pass

    elif int(inputs[0]) == 6:
        print(" ======================= REQUERIMIENTO 5 ======================= ")
        lpointname = input("Ingrese el nombre del landing point: ")
        result = controller.req5(catalog, lpointname)
        print("La cantidad de países afectados sería: " + str(lt.size(result)))
        for point in lt.iterator(result):
            print(" > " + point[0] + " a " + point[1] + " de distancia")
        
    else:
        sys.exit(0)
sys.exit(0)
