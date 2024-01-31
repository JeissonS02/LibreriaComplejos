import math

"""
Funcion que hace la suma entre dos numeros complejos
"""
def sumacplx(c1,c2):
    parteA = c1[0] + c2 [0]
    parteB = c1[1] + c2 [1]

    return parteA,parteB


"""
Funcion que hace la multiplicacion o producto entre dos numeros complejos
"""

def multcplx(c1, c2):
    parteA = c1[0] * c2[0]
    parteB = c1[1] * c2[1]
    parteC = c1[0] * c2[1]
    parteD = c1[1] * c2[0]
    parteI = parteA - parteB
    parteD = parteC + parteD

    return parteI, parteD



"""
Funcion que hace la resta entre dos numeros complejos
"""

def restcplx(c1,c2):
    parteA = c1[0] - c2[0]
    parteB = c1[1] - c2[1]

    return parteA,parteB

"""
Funcion que hace la division entre dos numeros complejos
"""

def divcplx(c1,c2):

    parteA = (c1[0] * c2[0]) + (c1[1] * c2[1])
    parteB = (c2[0] ** 2) + (c2[1] ** 2)
    parteC = (c2[0] * c1[1]) - (c1[0]*c2[1])

    parteI = parteA / parteB
    parteD = parteC / parteB

    return parteI,parteD

"""
Funcion que haya el modulo de un numero complejo
"""
def modul_cplx(c1):
    parteA = c1[0]**2
    parteB = c1[1]**2
    parteC = parteA + parteB
    parteD = parteC**0.5

    return parteD

"""
Funcion que haya el conjugado de un numero complejo
"""
def conjugado(numero_complejo):
    a, b = numero_complejo
    conjugado_a = a
    conjugado_b = -b
    return conjugado_a,conjugado_b
"""
Funcion que convierte un numero complejo de polar a cartesiano
"""
def polar_cplx(c1):
    parteA = modul_cplx(c1)
    parteB = fase_cplx(c1)
    parteC = parteA * math.cos(parteB) + parteA * math.sin(parteB)
    return parteC
"""
Funcion que haya la fase de un numero complejo
"""

def fase_cplx(c1):
    parteA = c1[1] / c1[0]
    parteB = math.atan(parteA)
    return parteB

