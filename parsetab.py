
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTUADOR ARTICULO ASIG ATRIBUTO COMA ENTONCES LEER MIENTRAS MODIFICAR MUESTRA NUMERO OC OL PUNTO P_ACCION SI SI_NOprograma : plantaplanta : ejecucionplanta : condicionalplanta : iterativoplanta : entradaplanta : salidaplanta : lecturalectura : LEER ARTICULO ATRIBUTO PUNTO plantaplanta : emptyejecucion : P_ACCION ACTUADOR PUNTO plantaiterativo : MIENTRAS ARTICULO ATRIBUTO OC NUMERO COMA ENTONCES plantacondicional : SI ARTICULO ATRIBUTO OL NUMERO COMA ENTONCES planta SI_NO COMA ENTONCES plantacondicional : SI ARTICULO ATRIBUTO OL NUMERO COMA ENTONCES plantaentrada : asignacionentrada : edicionsalida : monitoreoasignacion : ARTICULO ATRIBUTO ASIG NUMERO PUNTO plantaedicion : MODIFICAR ARTICULO ATRIBUTO ASIG NUMERO PUNTO plantamonitoreo : MUESTRA ARTICULO ATRIBUTO recrec : COMA ARTICULO ATRIBUTO recrec : OL ARTICULO ATRIBUTO PUNTO plantaempty :'
    
_lr_action_items = {'P_ACCION':([0,27,38,44,53,56,57,60,66,],[10,10,10,10,10,10,10,10,10,]),'SI':([0,27,38,44,53,56,57,60,66,],[11,11,11,11,11,11,11,11,11,]),'MIENTRAS':([0,27,38,44,53,56,57,60,66,],[13,13,13,13,13,13,13,13,13,]),'LEER':([0,27,38,44,53,56,57,60,66,],[17,17,17,17,17,17,17,17,17,]),'$end':([0,1,2,3,4,5,6,7,8,9,14,15,16,27,34,38,40,44,46,51,53,56,57,58,59,60,61,62,63,66,67,],[-22,0,-1,-2,-3,-4,-5,-6,-7,-9,-14,-15,-16,-22,-10,-22,-19,-22,-8,-17,-22,-22,-22,-18,-20,-22,-13,-11,-21,-22,-12,]),'ARTICULO':([0,11,13,17,18,19,27,38,41,42,44,53,56,57,60,66,],[12,21,23,24,25,26,12,12,48,49,12,12,12,12,12,12,]),'MODIFICAR':([0,27,38,44,53,56,57,60,66,],[18,18,18,18,18,18,18,18,18,]),'MUESTRA':([0,27,38,44,53,56,57,60,66,],[19,19,19,19,19,19,19,19,19,]),'SI_NO':([3,4,5,6,7,8,9,14,15,16,27,34,38,40,44,46,51,53,56,57,58,59,60,61,62,63,66,67,],[-2,-3,-4,-5,-6,-7,-9,-14,-15,-16,-22,-10,-22,-19,-22,-8,-17,-22,-22,-22,-18,-20,-22,64,-11,-21,-22,-12,]),'ACTUADOR':([10,],[20,]),'ATRIBUTO':([12,21,23,24,25,26,48,49,],[22,28,30,31,32,33,54,55,]),'PUNTO':([20,31,36,47,55,],[27,38,44,53,60,]),'ASIG':([22,32,],[29,39,]),'OL':([28,33,54,],[35,42,42,]),'NUMERO':([29,35,37,39,],[36,43,45,47,]),'OC':([30,],[37,]),'COMA':([33,43,45,54,64,],[41,50,52,41,65,]),'ENTONCES':([50,52,65,],[56,57,66,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'planta':([0,27,38,44,53,56,57,60,66,],[2,34,46,51,58,61,62,63,67,]),'ejecucion':([0,27,38,44,53,56,57,60,66,],[3,3,3,3,3,3,3,3,3,]),'condicional':([0,27,38,44,53,56,57,60,66,],[4,4,4,4,4,4,4,4,4,]),'iterativo':([0,27,38,44,53,56,57,60,66,],[5,5,5,5,5,5,5,5,5,]),'entrada':([0,27,38,44,53,56,57,60,66,],[6,6,6,6,6,6,6,6,6,]),'salida':([0,27,38,44,53,56,57,60,66,],[7,7,7,7,7,7,7,7,7,]),'lectura':([0,27,38,44,53,56,57,60,66,],[8,8,8,8,8,8,8,8,8,]),'empty':([0,27,38,44,53,56,57,60,66,],[9,9,9,9,9,9,9,9,9,]),'asignacion':([0,27,38,44,53,56,57,60,66,],[14,14,14,14,14,14,14,14,14,]),'edicion':([0,27,38,44,53,56,57,60,66,],[15,15,15,15,15,15,15,15,15,]),'monitoreo':([0,27,38,44,53,56,57,60,66,],[16,16,16,16,16,16,16,16,16,]),'rec':([33,54,],[40,59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> planta','programa',1,'p_programa','sintacticAnalyzer.py',23),
  ('planta -> ejecucion','planta',1,'p_planta1','sintacticAnalyzer.py',28),
  ('planta -> condicional','planta',1,'p_planta2','sintacticAnalyzer.py',33),
  ('planta -> iterativo','planta',1,'p_planta3','sintacticAnalyzer.py',38),
  ('planta -> entrada','planta',1,'p_planta4','sintacticAnalyzer.py',43),
  ('planta -> salida','planta',1,'p_planta5','sintacticAnalyzer.py',48),
  ('planta -> lectura','planta',1,'p_planta6','sintacticAnalyzer.py',53),
  ('lectura -> LEER ARTICULO ATRIBUTO PUNTO planta','lectura',5,'p_lectura','sintacticAnalyzer.py',58),
  ('planta -> empty','planta',1,'p_plantaEmpty','sintacticAnalyzer.py',62),
  ('ejecucion -> P_ACCION ACTUADOR PUNTO planta','ejecucion',4,'p_ejecucion','sintacticAnalyzer.py',67),
  ('iterativo -> MIENTRAS ARTICULO ATRIBUTO OC NUMERO COMA ENTONCES planta','iterativo',8,'p_iterativo','sintacticAnalyzer.py',72),
  ('condicional -> SI ARTICULO ATRIBUTO OL NUMERO COMA ENTONCES planta SI_NO COMA ENTONCES planta','condicional',12,'p_condicional1','sintacticAnalyzer.py',77),
  ('condicional -> SI ARTICULO ATRIBUTO OL NUMERO COMA ENTONCES planta','condicional',8,'p_condicional2','sintacticAnalyzer.py',83),
  ('entrada -> asignacion','entrada',1,'p_entrada1','sintacticAnalyzer.py',88),
  ('entrada -> edicion','entrada',1,'p_entrada2','sintacticAnalyzer.py',93),
  ('salida -> monitoreo','salida',1,'p_salida','sintacticAnalyzer.py',98),
  ('asignacion -> ARTICULO ATRIBUTO ASIG NUMERO PUNTO planta','asignacion',6,'p_asignacion','sintacticAnalyzer.py',103),
  ('edicion -> MODIFICAR ARTICULO ATRIBUTO ASIG NUMERO PUNTO planta','edicion',7,'p_edicion','sintacticAnalyzer.py',108),
  ('monitoreo -> MUESTRA ARTICULO ATRIBUTO rec','monitoreo',4,'p_monitoreo','sintacticAnalyzer.py',114),
  ('rec -> COMA ARTICULO ATRIBUTO rec','rec',4,'p_rec1','sintacticAnalyzer.py',119),
  ('rec -> OL ARTICULO ATRIBUTO PUNTO planta','rec',5,'p_rec2','sintacticAnalyzer.py',124),
  ('empty -> <empty>','empty',0,'p_empty','sintacticAnalyzer.py',129),
]
