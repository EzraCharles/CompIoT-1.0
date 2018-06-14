import os
import sys
import re
import codecs
import ply.lex as lex

reserved = [ 'MIENTRAS','SI','SI_NO','ENTONCES','MODIFICAR','MUESTRA','LEER']

tokens = reserved + ['COMA', 'PUNTO', 'NUMERO','ASIG',
            'P_ACCION',
            #"ENCENDER","APAGAR",
            'ATRIBUTO',
            #"PH","HUMEDAD_RELATIVA","LUMINOSIDAD","AGUA","TEMPERATURA","MINERAL",
            'ARTICULO',
            #"EL","LA",
            'ACTUADOR',
            #"LUZ","ASPERSOR", "FLUJO", "CALOR", "VENTILADOR", "LLAVE", "TANQUE",
            #'CONTROL',
            #"DEPOSITA",
            'OL',
            #"Y", "O",
            'OC'
            #"ES_MENOR_QUE", "ES_MAYOR_QUE", "ES_IGUAL_QUE", "ES_DIFERENTE_QUE"
         ]

#t_CONTROL = r'deposita-mineral\d+'
t_ignore = '\t'
t_COMA = r','
t_PUNTO = r'\.'

def t_ASIG(t):
    r'\bigual_a\b'
    return t

"""def t_NUMERO(t):
    r'\d+\,'
    r = str(t.value)
    r = r.replace(',', '')
    t.value = int(r)
    return t
"""
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

"""def t_CONTROL(t):
    r'deposita'
    return t"""

def t_MIENTRAS(t):
    r'\bmientras\b'
    return t

def t_LEER(t):
    r'\bleer\b'
    return t

def t_SI_NO(t):
    r'\bsi_no\b'
    return t

def t_SI(t):
    r'\bsi\b'
    return t

def t_ENTONCES(t):
    r'\bentonces\b'
    return t

def t_MODIFICAR(t):
    r'\bmodificar\b'
    return t

def t_MUESTRA(t):
    r'\bmuestra\b'
    return t

def t_P_ACCION(t):
    r'\bencender\b|\bapagar\b'
    return t

def t_ATRIBUTO(t):
    r'\bhumedad_relativa\b|\bluminosidad\b|\bagua\b|\btemperatura\b|\bmineral\b|\bPH\b'
    return t

def t_ARTICULO(t):
    r'\bla\b|\bel\b'
    return t

def t_ACTUADOR(t):
    r'\bluz\b|\baspersor\b|\bflujo\b|\bcalor\b|\bventilador\b|\bllave\b|\btanque\b|\bcontrol\b|\bbomba\b|\bfocos\b'
    return t

def t_OL(t):
    r'\by\b'
    return t

def t_OC(t):
    r'\bes_menor_que\b|\bes_mayor_que\b|\bes_diferente_que\b|\bes_igual_que\b'
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_whitespace(t):
    r'\s+'
    pass

def t_error(t):
    #print ("Caracter ilegal" %t.value[0])
    r = str(t)
    r = r.split("'")
    r = r[1]
    r = r.split(' ')
    r = r[0]

    if r.find('\\'):
        r = r.split('\\')

    raise LexicalError("Token no valido.", r[0])
    #print('Error lexico, Token ilegal: "' + str(r[0]) + '" en la linea ' + str(t.lineno) + ".")
    t.lexer.skip(int(len(r[0])))
    #t.lexer.skkip(int(len(r)))

class Error(Exception):
    """Clase base para excepciones en el módulo."""
    pass

class LexicalError(Error):
    """Excepción lanzada por errores en las entradas.

    Atributos:
        expresion -- expresión de entrada en la que ocurre el error
        mensaje -- explicación del error
    """

    def __init__(self, expresion, mensaje):
        self.expresion = expresion
        self.mensaje = mensaje

#Visualizacion de los tokens por separado.
def impresionToken(t):
    r = str(t)
    r = r.split(",")
    r = r[1]

    if r.__contains__("'"):
        r = r.replace("'", '')

    if r.__len__() == 0:
        r = ','

    #print("Token: " + str(r))
    return 'Token: "' + str(r) + '"'

# Token para guardar en archivo.
def saveToken(t):
    r = str(t)
    r = r.split("(")
    r = r[1]
    r = r.split(")")
    r = str(r[0])

    return r

#TEST---------------------------------------------------------------------------------------------------------------

def test(file):
    source = codecs.open(file, "r", "utf-8")
    cadena = source.read()
    source.close()

    analizador = lex.lex()

    analizador.input(cadena)

    tempT = ["Tipo", "Token", "No. linea", "No. caracter"]

    while True:
        tok = analizador.token()
        if not tok: break
        #print(impresionToken(tok))  # Imprime solamente el token
        temp = saveToken(tok).split(',')
        if temp.__len__() == 5:
            temp.remove("'")
            temp[1] = "','"
        tempT.append(temp[0])
        tempT.append(temp[1])
        tempT.append(temp[2])
        tempT.append(temp[3])

        #print(saveToken(tok))      # Imprime los datos separados
        #print(tok)                  # Imprime la cadena de Lex

    return tempT

analizador = lex.lex()
#file = "test1.txt"
#print(test(file))