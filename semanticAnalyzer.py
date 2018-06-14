#import sintacticAnalyzer
#import lexicalAnalyzer

txt = " "
cont = 0
asm = " "

def incremetarContador():
    global cont
    cont += 1
    return "%d" % cont


class Nodo():
    pass


class Null(Nodo):
    def __init__(self):
        self.type = 'void'

    def imprimir(self, ident):
        global asm
        asm += ident + "NODO NULO\n"

        print(ident + "NODO NULO")

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= " + "nodo_nulo" + "]" + "\n\t"
        return id


class programa(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Programa: " + self.name)

        global asm
        asm += ident + "Programa: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return "digraph G { \n\t" + txt + "}"


class planta1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Planta1: " + self.name)

        global asm
        asm += ident + "Planta1: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id


class planta2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Planta2: " + self.name)

        global asm
        asm += ident + "Planta2: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id


class planta3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Planta3: " + self.name)

        global asm
        asm += ident + "Planta3: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id


class planta4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Planta4: " + self.name)

        global asm
        asm += ident + "Planta4: " + self.name + "\n"

    def traducir(self):
        global txt

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id


class planta5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Planta5: " + self.name)

        global asm
        asm += ident + "Planta5: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id


class planta6(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Planta6: " + self.name)

        global asm
        asm += ident + "Planta6: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id


class lectura(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        print(ident + "Lectura: " + self.name)

        global asm
        asm += ident + "Lectura: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"

        return id


class plantaEmpty(Nodo):
    def __init__(self, name):
        pass


class ejecucion(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        print(ident + "Ejecucion: " + self.name)

        global asm
        asm += ident + "Ejecucion: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"

        return id


class iterativo(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        self.son5.imprimir(" " + ident)
        self.son6.imprimir(" " + ident)
        self.son7.imprimir(" " + ident)
        self.son8.imprimir(" " + ident)
        print(ident + "Iterativo: " + self.name)

        global asm
        asm += ident + "Iterativo: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()
        son6 = self.son6.traducir()
        son7 = self.son7.traducir()

        if type(self.son8) == type(tuple()):
            son8 = self.son8[0].traducir()
        else:
            son8 = self.son8.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"
        txt += id + "->" + son6 + "\n\t"
        txt += id + "->" + son7 + "\n\t"
        txt += id + "->" + son8 + "\n\t"
        return id


class condicional1(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, son9, son10, son11, son12, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9
        self.son10 = son10
        self.son11 = son11
        self.son12 = son12

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        self.son5.imprimir(" " + ident)
        self.son6.imprimir(" " + ident)
        self.son7.imprimir(" " + ident)
        self.son8.imprimir(" " + ident)
        self.son9.imprimir(" " + ident)
        self.son10.imprimir(" " + ident)
        self.son11.imprimir(" " + ident)
        self.son12.imprimir(" " + ident)
        print(ident + "Condicional: " + self.name)

        global asm
        asm += ident + "Condicional: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()
        son6 = self.son6.traducir()
        son7 = self.son7.traducir()

        if type(self.son8) == type(tuple()):
            son8 = self.son8[0].traducir()
        else:
            son8 = self.son8.traducir()

        son9 = self.son9.traducir()
        son10 = self.son10.traducir()
        son11 = self.son11.traducir()

        if type(self.son12) == type(tuple()):
            son12 = self.son12[0].traducir()
        else:
            son12 = self.son12.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"
        txt += id + "->" + son6 + "\n\t"
        txt += id + "->" + son7 + "\n\t"
        txt += id + "->" + son8 + "\n\t"
        txt += id + "->" + son9 + "\n\t"
        txt += id + "->" + son10 + "\n\t"
        txt += id + "->" + son11 + "\n\t"
        txt += id + "->" + son12 + "\n\t"
        return id


class condicional2(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        self.son5.imprimir(" " + ident)
        self.son6.imprimir(" " + ident)
        self.son7.imprimir(" " + ident)
        self.son8.imprimir(" " + ident)
        print(ident + "Condicional2: " + self.name)

        global asm
        asm += ident + "Condicional2: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()
        son6 = self.son6.traducir()
        son7 = self.son7.traducir()

        if type(self.son8) == type(tuple()):
            son8 = self.son8[0].traducir()
        else:
            son8 = self.son8.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"
        txt += id + "->" + son6 + "\n\t"
        txt += id + "->" + son7 + "\n\t"
        txt += id + "->" + son8 + "\n\t"
        return id


class entrada1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Entrada1: " + self.name)

        global asm
        asm += ident + "Entrada1: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id


class entrada2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Entrada2: " + self.name)

        global asm
        asm += ident + "Entrada2: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id


class salida(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Salida: " + self.name)

        global asm
        asm += ident + "Salida: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        return id


class asignacion(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        self.son5.imprimir(" " + ident)
        self.son6.imprimir(" " + ident)
        print(ident + "Asignacion: " + self.name)

        global asm
        asm += ident + "Asignacion: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        if type(self.son6) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"
        txt += id + "->" + son6 + "\n\t"
        return id


class edicion(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        self.son5.imprimir(" " + ident)
        self.son6.imprimir(" " + ident)
        self.son7.imprimir(" " + ident)
        print(ident + "Edicion: " + self.name)

        global asm
        asm += ident + "Edicion: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()
        son6 = self.son6.traducir()

        if type(self.son7) == type(tuple()):
            son7 = self.son7[0].traducir()
        else:
            son7 = self.son7.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        txt += id + "->" + son5 + "\n\t"
        txt += id + "->" + son6 + "\n\t"
        txt += id + "->" + son7 + "\n\t"
        return id


# verificar con la gramatica
class monitoreo(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        print(ident + "Monitoreo: " + self.name)

        global asm
        asm += ident + "Monitoreo: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        return id


class rec1(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        print(ident + "Rec1: " + self.name)

        global asm
        asm += ident + "Rec1: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        return id


class rec2(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        print(ident + "Rec2: " + self.name)

        global asm
        asm += ident + "Rec2: " + self.name + "\n"


    def traducir(self):
        global txt
        id = incremetarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"
        return id


"""class empty(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incremetarContador()

		return id

class error(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incremetarContador()

		return id"""


# Tokens and keywords----------------------------------------------------------------------------------------------------

class MIENTRAS(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Mientras: " + str(self.name))

        global asm
        asm += ident + "Mientras: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class SI(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Si: " + str(self.name))

        global asm
        asm += ident + "Si: " + self.name + "\n"


    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class SI_NO(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Si_no: " + str(self.name))

        global asm
        asm += ident + "Si_no: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class ENTONCES(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Entonces: " + str(self.name))

        global asm
        asm += ident + "Entonces: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class MODIFICAR(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Modificar: " + str(self.name))

        global asm
        asm += ident + "Modificar: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class MUESTRA(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Muestra: " + str(self.name))

        global asm
        asm += ident + "Muestras: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class COMA(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Coma: " + str(self.name))

        global asm
        asm += ident + "Coma: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class PUNTO(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Punto: " + str(self.name))

        global asm
        asm += ident + "Punto: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class NUMERO(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Numero: " + str(self.name))

        global asm
        asm += ident + "Numero: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class ASIG(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Asig: " + str(self.name))

        global asm
        asm += ident + "Asig: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class LEER(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Leer: " + str(self.name))

        global asm
        asm += ident + "Leer: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class P_ACCION(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "P_accion: " + str(self.name))

        global asm
        asm += ident + "P_accion: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class ATRIBUTO(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Atributo: " + str(self.name))

        global asm
        asm += ident + "Atributo: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class ARTICULO(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Articulo: " + str(self.name))

        global asm
        asm += ident + "Articulo: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class ACTUADOR(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Actuador: " + str(self.name))

        global asm
        asm += ident + "Actuador: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class OL(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "OL: " + str(self.name))

        global asm
        asm += ident + "OL: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id


class OC(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "OC: " + str(self.name))

        global asm
        asm += ident + "OC: " + self.name + "\n"

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"
        return id
