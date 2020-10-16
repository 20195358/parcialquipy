import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
def multiplicar(num1, num2, num3):
    resultado = num1 * num2 * num3
    return resultado


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    result = 0

    for x in range(1000,2001):
        if x % 5 == 0 and x % 3 == 0:
            result = result + x
    
    return result 


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro(longitud, latitud,altura):
    thisdict = {"area": 0, "volumen": 0}
    thisdict["area"] = 2 * (longitud * latitud + longitud * altura + latitud * altura)
    thisdict["volumen"] = longitud * latitud * altura
    result = thisdict
    return result
    
    


def obtenerArea(longitud, latitud, altura):
    result = 2 * (longitud * latitud + longitud * altura + latitud * altura)
    return result


def obtenerVolumen(longitud,latitud, altura):
    result = longitud * latitud * altura
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def __init__(self, longitud, latitud, altura):
        self.__longitud = longitud
        self.__latitud = latitud
        self.__altura = altura

    def definicionOrtoedro(self):
        thisdict = {"area": 0, "volumen": 0}
        thisdict["area"] = 2 * (self.__longitud * self.__latitud + self.__longitud * self.__altura + self.__latitud * self.__altura)
        thisdict["volumen"] = self.__longitud * self.__latitud * self.__altura
        result = thisdict
        return result
    


"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def __init__(self):
        self.compuList = []
        
        

    def orden(self):
        Computadora = {"procesador": 0, "memoria": 0, "grafica": 0, "ram": 0, "precio": 0, "boolean": 0, "desc": 0}
        self.compuList.append(Computadora)

    def totalProcesadorIntel(self):
        
        for pc in self.compuList:
            if pc["procesador"] == "intel":
                result = result + pc[precio]
                return result

    def totalRam16ConDescuento(self):
        for pc2 in self.compuList:
            if pc2["ram"] == "16" and pc2[descuento] == True:
                result = result + pc2[precio]
                return result


class Computadora:
    pass 


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/20195358/parcialquipy.git"
