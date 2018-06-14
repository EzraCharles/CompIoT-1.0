import ply.yacc as yacc
import os
import sys
import re
import codecs
import lexicalAnalyzer
from lexicalAnalyzer import tokens
from semanticAnalyzer import *
from sys import stdin

"""precedence = (
    ('right', 'NUMERO'),
    ('right', 'ARTICULO'),
    ('right','SI_NO'),
    ('right', 'SI'),
    ('right', 'MUESTRA'),
    ('right', 'MODIFICAR'),
    ('right', 'ENTONCES'),
    ('right', 'MIENTRAS')
)"""

def p_programa(p):
    'programa : planta'
    #print("programa")
    p[0] = programa(p[1], "programa")

def p_planta1(p):
    'planta : ejecucion'
    #print("planta1")
    p[0] = planta1(p[1], "planta1")

def p_planta2(p):
    'planta : condicional'
    #print("planta2")
    p[0] = planta2(p[1], "planta2")

def p_planta3(p):
    'planta : iterativo'
    #print("planta3")
    p[0] = planta3(p[1], "planta3")

def p_planta4(p):
    'planta : entrada'
    #print("planta4")
    p[0] = planta4(p[1], "planta4")

def p_planta5(p):
    'planta : salida'
    #print("planta5")
    p[0] = planta5(p[1], "planta5")

def p_planta6(p):
    'planta : lectura'
    #print("planta5")
    p[0] = planta5(p[1], "planta6")

def p_lectura(p):
    'lectura : LEER ARTICULO ATRIBUTO PUNTO planta'
    p[0] = lectura(LEER(p[1]), ARTICULO(p[2]), ATRIBUTO(p[3]), PUNTO(p[4]), "planta6")

def p_plantaEmpty(p):
    'planta : empty'
    #print("planta6")
    p[0] = Null()

def p_ejecucion(p):
    'ejecucion : P_ACCION ACTUADOR PUNTO planta'
    #print("ejecucion")
    p[0] = ejecucion(P_ACCION(p[1]), ACTUADOR(p[2]), PUNTO(p[3]), p[4], "ejecucion")

def p_iterativo(p):
    'iterativo : MIENTRAS ARTICULO ATRIBUTO OC NUMERO COMA ENTONCES planta'
    #print("iterativo")
    p[0] = iterativo(MIENTRAS(p[1]), ARTICULO(p[2]), ATRIBUTO(p[3]), OC(p[4]), NUMERO(p[5]), COMA(p[6]), ENTONCES(p[7]), p[8], "iterativo")

def p_condicional1(p):
    'condicional : SI ARTICULO ATRIBUTO OL NUMERO COMA ENTONCES planta SI_NO COMA ENTONCES planta'
    #print("condicional1")
    p[0] = condicional1(SI(p[1]), ARTICULO(p[2]), ATRIBUTO(p[3]), OL(p[4]), NUMERO(p[5]), COMA(p[6]), ENTONCES(p[7]),
                        p[8], SI_NO(p[9]), COMA(p[10]), ENTONCES(p[11]), p[12], "condicional1")

def p_condicional2(p):
    'condicional : SI ARTICULO ATRIBUTO OL NUMERO COMA ENTONCES planta'
    #print("condicional2")
    p[0] = condicional1(SI(p[1]), ARTICULO(p[2]), ATRIBUTO(p[3]), OL(p[4]), NUMERO(p[5]), COMA(p[6]), ENTONCES(p[7]), p[8], "condicional2")

def p_entrada1(p):
    'entrada : asignacion'
    #print("entrada1")
    p[0] = entrada1(p[1], "entrada1")

def p_entrada2(p):
    'entrada : edicion'
    #print("entrada2")
    p[0] = entrada2(p[1], "entrada2")

def p_salida(p):
    'salida : monitoreo'
    #print("salida")
    p[0] = salida(p[1], "salida")

def p_asignacion(p):
    'asignacion : ARTICULO ATRIBUTO ASIG NUMERO PUNTO planta'
    #print("asignacion")
    p[0] = asignacion(ARTICULO(p[1]), ATRIBUTO(p[2]), ASIG(p[3]), NUMERO(p[4]), PUNTO(p[5]), p[6], "asignacion")

def p_edicion(p):
    'edicion : MODIFICAR ARTICULO ATRIBUTO ASIG NUMERO PUNTO planta'
    #print("edicion")
    p[0] = edicion(MODIFICAR(p[1]), ARTICULO(p[2]), ATRIBUTO(p[3]), ASIG(p[4]), NUMERO(p[5]), PUNTO(p[6]), p[7], "edicion")

#verificar con la gramatica
def p_monitoreo(p):
    'monitoreo : MUESTRA ARTICULO ATRIBUTO rec'
    #print("monitoreo")
    p[0] = monitoreo(MUESTRA(p[1]), ARTICULO(p[2]), ATRIBUTO(p[3]), p[4], "monitoreo")

def p_rec1(p):
    'rec : COMA ARTICULO ATRIBUTO rec'
    #print("rec1")
    p[0] = rec1(COMA(p[1]), ARTICULO(p[2]), ATRIBUTO(p[3]), p[4], "rec1")

def p_rec2(p):
    'rec : OL ARTICULO ATRIBUTO PUNTO planta'
    #print("rec2")
    p[0] = rec2(OL(p[1]), ARTICULO(p[2]), ATRIBUTO(p[3]), PUNTO(p[4]), "rec2")

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Error de sintaxis. " + str(errorType(p)) + " en la linea " + str(p.lineno) + ".")

def traducir(result):
    graphFile = open('graphviztree.gv','w')
    graphFile.write(result.traducir())
    graphFile.close()

    import semanticAnalyzer
    asm = open('asmcode.asm', 'w')
    asm.write(semanticAnalyzer.asm)
    print("\n El programa traducido se guardo en \"graphviztree.vz\" \n y el ASM en asmcode.asm.")

#Definicion de los errores.
def errorType(p):
    p = lexicalAnalyzer.impresionToken(p)
    raise SintaxlError("Error de Sintaxis: no se esperaba el Token.", p)
    #return "No se esperaba el " + str(p)

class Error(Exception):
    """Clase base para excepciones en el módulo."""
    pass

class SintaxlError(Error):
    """Excepción lanzada por errores en las entradas.

    Atributos:
        expresion -- expresión de entrada en la que ocurre el error
        mensaje -- explicación del error
    """

    def __init__(self, expresion, mensaje):
        self.expresion = expresion
        self.mensaje = mensaje


#TEST--------------------------------------------------------------------------------------------------------------
def test(file):
    source = codecs.open(file, "r", "utf-8")
    cadena = source.read()
    source.close()

    yacc.yacc()
    result = yacc.parse(cadena, debug=1)

    #traducir(result)
    result.imprimir(" ")

    traducir(result)
        #result.traducir()
"""
#parser = yacc.yacc('SLR')
#result = parser.parse(cadena, debug=1)

#yacc.yacc()
result = yacc.parse(cadena, debug=1)

traducir(result)
result.imprimir(" ")
#print(result.traducir())

#print(result)
"""
#yacc.yacc()