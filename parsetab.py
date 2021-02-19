
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSAND CATGIRL CHAN COMMA DEQ DESU DIVIDE EQ EQOP GEQ GT HAREM ID ISTUDIED KUN LBRACE LBRACK LEQ LPAREN LT MEQ MINUS MULTID NANI NEQ NOT NOU NUMBER OR OWO PEQ PERIOD PLUS RBRACE RBRACK REAL RPAREN SAN SEMICOL SHI SQUIGGLY TEQ TIMES UWU WAIFU WHILEU YOKAIstatement : numExpr SEMICOL\n                 | boolExpr SEMICOL\n                 | declare SEMICOL\n     declare : declaration\n                | declaration EQ numExpr \n                | declaration EQ boolExpr    \n     declaration : type ID \n                    | arrays ID \n                    | REAL declaration\n     arrays : type HAREM \n     type : WAIFU\n             | CATGIRL\n     boolExpr : boolExpr NEQ boolExpr\n                 | numExpr NEQ numExpr\n                 | numExpr LEQ numExpr\n                 | numExpr GEQ numExpr\n                 | numExpr LT numExpr\n                 | numExpr GT numExpr\n                 | numExpr EQOP numExpr\n                 | boolExpr EQOP boolExpr\n                 | boolExpr AND boolExpr\n                 | boolExpr OR boolExpr\n    boolExpr : NOT boolExpr\n    boolExpr : LPAREN boolExpr RPAREN boolExpr : OWO\n             | UWU\n    numExpr : numExpr PLUS numExpr\n                  | numExpr MINUS numExpr\n                  | numExpr TIMES numExpr\n                  | numExpr DIVIDE numExprnumExpr : MINUS numExpr %prec UMINUSnumExpr : LPAREN numExpr RPARENnumExpr : NUMBER'
    
_lr_action_items = {'MINUS':([0,2,5,6,7,8,18,19,20,21,22,23,24,25,26,27,29,30,31,32,34,35,36,39,40,41,46,47,48,49,50,51,52,53,54,55,60,61,63,64,],[5,19,5,5,-33,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-31,5,19,19,5,5,-27,-28,-29,-30,19,19,19,19,19,19,19,-32,19,19,]),'LPAREN':([0,5,6,8,18,19,20,21,22,23,24,25,26,27,29,30,31,32,35,40,41,],[6,35,6,40,35,35,35,35,35,35,35,35,35,35,40,40,40,40,35,40,6,]),'NUMBER':([0,5,6,8,18,19,20,21,22,23,24,25,26,27,29,30,31,32,35,40,41,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'NOT':([0,6,8,29,30,31,32,40,41,],[8,8,8,8,8,8,8,8,8,]),'OWO':([0,6,8,29,30,31,32,40,41,],[9,9,9,9,9,9,9,9,9,]),'UWU':([0,6,8,29,30,31,32,40,41,],[10,10,10,10,10,10,10,10,10,]),'REAL':([0,14,],[14,14,]),'WAIFU':([0,14,],[15,15,]),'CATGIRL':([0,14,],[16,16,]),'$end':([1,17,28,33,],[0,-1,-2,-3,]),'SEMICOL':([2,3,4,7,9,10,11,34,38,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,64,65,],[17,28,33,-33,-25,-26,-4,-31,-23,-7,-8,-9,-27,-28,-29,-30,-14,-15,-16,-17,-18,-19,-13,-20,-21,-22,-32,-24,-5,-6,]),'PLUS':([2,7,34,36,39,46,47,48,49,50,51,52,53,54,55,60,61,63,64,],[18,-33,-31,18,18,-27,-28,-29,-30,18,18,18,18,18,18,18,-32,18,18,]),'TIMES':([2,7,34,36,39,46,47,48,49,50,51,52,53,54,55,60,61,63,64,],[20,-33,-31,20,20,20,20,-29,-30,20,20,20,20,20,20,20,-32,20,20,]),'DIVIDE':([2,7,34,36,39,46,47,48,49,50,51,52,53,54,55,60,61,63,64,],[21,-33,-31,21,21,21,21,-29,-30,21,21,21,21,21,21,21,-32,21,21,]),'NEQ':([2,3,7,9,10,34,36,37,38,39,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,],[22,29,-33,-25,-26,-31,22,29,29,22,-27,-28,-29,-30,-14,-15,-16,-17,-18,-19,29,29,29,29,-32,-24,22,22,29,]),'LEQ':([2,7,34,36,39,46,47,48,49,61,63,64,],[23,-33,-31,23,23,-27,-28,-29,-30,-32,23,23,]),'GEQ':([2,7,34,36,39,46,47,48,49,61,63,64,],[24,-33,-31,24,24,-27,-28,-29,-30,-32,24,24,]),'LT':([2,7,34,36,39,46,47,48,49,61,63,64,],[25,-33,-31,25,25,-27,-28,-29,-30,-32,25,25,]),'GT':([2,7,34,36,39,46,47,48,49,61,63,64,],[26,-33,-31,26,26,-27,-28,-29,-30,-32,26,26,]),'EQOP':([2,3,7,9,10,34,36,37,38,39,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,],[27,30,-33,-25,-26,-31,27,30,30,27,-27,-28,-29,-30,-14,-15,-16,-17,-18,-19,30,30,30,30,-32,-24,27,27,30,]),'AND':([3,7,9,10,34,37,38,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,65,],[31,-33,-25,-26,-31,31,31,-27,-28,-29,-30,-14,-15,-16,-17,-18,-19,31,31,31,31,-32,-24,31,]),'OR':([3,7,9,10,34,37,38,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,65,],[32,-33,-25,-26,-31,32,32,-27,-28,-29,-30,-14,-15,-16,-17,-18,-19,32,32,32,32,-32,-24,32,]),'RPAREN':([7,9,10,34,36,37,38,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[-33,-25,-26,-31,61,62,-23,-27,-28,-29,-30,-14,-15,-16,-17,-18,-19,-13,-20,-21,-22,61,-32,-24,61,]),'EQ':([11,42,44,45,],[41,-7,-8,-9,]),'ID':([12,13,15,16,43,],[42,44,-11,-12,-10,]),'HAREM':([12,15,16,],[43,-11,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'numExpr':([0,5,6,8,18,19,20,21,22,23,24,25,26,27,29,30,31,32,35,40,41,],[2,34,36,39,46,47,48,49,50,51,52,53,54,55,39,39,39,39,60,63,64,]),'boolExpr':([0,6,8,29,30,31,32,40,41,],[3,37,38,56,57,58,59,37,65,]),'declare':([0,],[4,]),'declaration':([0,14,],[11,45,]),'type':([0,14,],[12,12,]),'arrays':([0,14,],[13,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> numExpr SEMICOL','statement',2,'p_statement_expr','parser.py',15),
  ('statement -> boolExpr SEMICOL','statement',2,'p_statement_expr','parser.py',16),
  ('statement -> declare SEMICOL','statement',2,'p_statement_expr','parser.py',17),
  ('declare -> declaration','declare',1,'p_statement_declare','parser.py',23),
  ('declare -> declaration EQ numExpr','declare',3,'p_statement_declare','parser.py',24),
  ('declare -> declaration EQ boolExpr','declare',3,'p_statement_declare','parser.py',25),
  ('declaration -> type ID','declaration',2,'p_statement_declaration_or_assign_h','parser.py',32),
  ('declaration -> arrays ID','declaration',2,'p_statement_declaration_or_assign_h','parser.py',33),
  ('declaration -> REAL declaration','declaration',2,'p_statement_declaration_or_assign_h','parser.py',34),
  ('arrays -> type HAREM','arrays',2,'p_arrays','parser.py',44),
  ('type -> WAIFU','type',1,'p_types','parser.py',49),
  ('type -> CATGIRL','type',1,'p_types','parser.py',50),
  ('boolExpr -> boolExpr NEQ boolExpr','boolExpr',3,'p_boolExpr_op','parser.py',55),
  ('boolExpr -> numExpr NEQ numExpr','boolExpr',3,'p_boolExpr_op','parser.py',56),
  ('boolExpr -> numExpr LEQ numExpr','boolExpr',3,'p_boolExpr_op','parser.py',57),
  ('boolExpr -> numExpr GEQ numExpr','boolExpr',3,'p_boolExpr_op','parser.py',58),
  ('boolExpr -> numExpr LT numExpr','boolExpr',3,'p_boolExpr_op','parser.py',59),
  ('boolExpr -> numExpr GT numExpr','boolExpr',3,'p_boolExpr_op','parser.py',60),
  ('boolExpr -> numExpr EQOP numExpr','boolExpr',3,'p_boolExpr_op','parser.py',61),
  ('boolExpr -> boolExpr EQOP boolExpr','boolExpr',3,'p_boolExpr_op','parser.py',62),
  ('boolExpr -> boolExpr AND boolExpr','boolExpr',3,'p_boolExpr_op','parser.py',63),
  ('boolExpr -> boolExpr OR boolExpr','boolExpr',3,'p_boolExpr_op','parser.py',64),
  ('boolExpr -> NOT boolExpr','boolExpr',2,'p_boolExpr_not','parser.py',78),
  ('boolExpr -> LPAREN boolExpr RPAREN','boolExpr',3,'p_boolExpr_group','parser.py',83),
  ('boolExpr -> OWO','boolExpr',1,'p_bool','parser.py',87),
  ('boolExpr -> UWU','boolExpr',1,'p_bool','parser.py',88),
  ('numExpr -> numExpr PLUS numExpr','numExpr',3,'p_numExpr_binop','parser.py',94),
  ('numExpr -> numExpr MINUS numExpr','numExpr',3,'p_numExpr_binop','parser.py',95),
  ('numExpr -> numExpr TIMES numExpr','numExpr',3,'p_numExpr_binop','parser.py',96),
  ('numExpr -> numExpr DIVIDE numExpr','numExpr',3,'p_numExpr_binop','parser.py',97),
  ('numExpr -> MINUS numExpr','numExpr',2,'p_numExpr_uminus','parser.py',109),
  ('numExpr -> LPAREN numExpr RPAREN','numExpr',3,'p_numExpr_group','parser.py',114),
  ('numExpr -> NUMBER','numExpr',1,'p_numExpr_number','parser.py',119),
]
