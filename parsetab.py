
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSAND CATGIRL CHAN COMMA DEQ DESU DIVIDE EQ EQOP GEQ GT HAREM ID ISTUDIED KUN LBRACE LBRACK LEQ LPAREN LT MEQ MINUS MULTID NANI NEQ NOT NOU NUMBER OR OWO PEQ PERIOD PLUS RBRACE RBRACK REAL RPAREN SAN SEMICOL SHI SQUIGGLY TEQ TIMES UWU WAIFU WHILEU YOKAImultiState : statement\n                    | multiState statementstatement : numExpr SEMICOL\n                 | boolExpr SEMICOL\n                 | declare SEMICOL\n                 | print SEMICOL\n                 | reassign SEMICOL\n     reassign : ID EQ numExpr\n                 | ID EQ boolExpr\n     declare : declaration\n                | declaration EQ numExpr \n                | declaration EQ boolExpr    \n     declaration : type ID \n                    | arrays ID \n                    | REAL declaration\n     arrays : type HAREM \n     type : WAIFU\n             | CATGIRL\n     boolExpr : boolExpr NEQ boolExpr\n                 | numExpr NEQ numExpr\n                 | numExpr LEQ numExpr\n                 | numExpr GEQ numExpr\n                 | numExpr LT numExpr\n                 | numExpr GT numExpr\n                 | numExpr EQOP numExpr\n                 | boolExpr EQOP boolExpr\n                 | boolExpr AND boolExpr\n                 | boolExpr OR boolExpr\n    boolExpr : NOT boolExpr\n    boolExpr : LPAREN boolExpr RPAREN boolExpr : OWO\n             | UWU\n    numExpr : numExpr PLUS numExpr\n                  | numExpr MINUS numExpr\n                  | numExpr TIMES numExpr\n                  | numExpr DIVIDE numExprnumExpr : ID PEQ numExpr\n                | ID MEQ numExpr\n                | ID DEQ numExpr\n                | ID TEQ numExpr\n    numExpr : MINUS numExpr %prec UMINUSnumExpr : LPAREN numExpr RPARENnumExpr : NUMBERprint : ID'
    
_lr_action_items = {'ID':([0,1,2,8,10,12,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,47,48,53,54,56,],[9,9,-1,42,42,42,55,57,-17,-18,-2,-3,42,42,42,42,42,42,42,42,42,42,-4,42,42,42,42,-5,-6,-7,42,42,42,42,42,42,42,42,-16,]),'MINUS':([0,1,2,3,8,10,11,12,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,52,53,54,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,80,82,83,],[8,8,-1,24,8,8,-43,8,-2,-3,8,8,8,8,8,8,8,8,8,8,-4,8,8,8,8,-5,-6,-7,-41,8,8,8,8,8,8,24,24,8,8,-33,-34,-35,-36,24,24,24,24,24,24,24,24,24,24,24,24,-42,24,24,]),'LPAREN':([0,1,2,8,10,12,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,47,48,53,54,],[10,10,-1,43,10,53,-2,-3,43,43,43,43,43,43,43,43,43,43,-4,53,53,53,53,-5,-6,-7,43,43,43,43,43,10,53,10,]),'NUMBER':([0,1,2,8,10,12,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,47,48,53,54,],[11,11,-1,11,11,11,-2,-3,11,11,11,11,11,11,11,11,11,11,-4,11,11,11,11,-5,-6,-7,11,11,11,11,11,11,11,11,]),'NOT':([0,1,2,10,12,21,22,33,34,35,36,37,38,39,40,48,53,54,],[12,12,-1,12,12,-2,-3,-4,12,12,12,12,-5,-6,-7,12,12,12,]),'OWO':([0,1,2,10,12,21,22,33,34,35,36,37,38,39,40,48,53,54,],[13,13,-1,13,13,-2,-3,-4,13,13,13,13,-5,-6,-7,13,13,13,]),'UWU':([0,1,2,10,12,21,22,33,34,35,36,37,38,39,40,48,53,54,],[14,14,-1,14,14,-2,-3,-4,14,14,14,14,-5,-6,-7,14,14,14,]),'REAL':([0,1,2,18,21,22,33,38,39,40,],[18,18,-1,18,-2,-3,-4,-5,-6,-7,]),'WAIFU':([0,1,2,18,21,22,33,38,39,40,],[19,19,-1,19,-2,-3,-4,-5,-6,-7,]),'CATGIRL':([0,1,2,18,21,22,33,38,39,40,],[20,20,-1,20,-2,-3,-4,-5,-6,-7,]),'$end':([1,2,21,22,33,38,39,40,],[0,-1,-2,-3,-4,-5,-6,-7,]),'SEMICOL':([3,4,5,6,7,9,11,13,14,15,41,51,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,83,84,],[22,33,38,39,40,-44,-43,-31,-32,-10,-41,-29,-13,-14,-15,-33,-34,-35,-36,-20,-21,-22,-23,-24,-25,-19,-26,-27,-28,-37,-38,-39,-40,-8,-9,-42,-30,-11,-12,]),'PLUS':([3,11,41,49,52,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,80,82,83,],[23,-43,-41,23,23,-33,-34,-35,-36,23,23,23,23,23,23,23,23,23,23,23,23,-42,23,23,]),'TIMES':([3,11,41,49,52,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,80,82,83,],[25,-43,-41,25,25,25,25,-35,-36,25,25,25,25,25,25,25,25,25,25,25,25,-42,25,25,]),'DIVIDE':([3,11,41,49,52,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,80,82,83,],[26,-43,-41,26,26,26,26,-35,-36,26,26,26,26,26,26,26,26,26,26,26,26,-42,26,26,]),'NEQ':([3,4,11,13,14,41,49,50,51,52,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,],[27,34,-43,-31,-32,-41,27,34,34,27,-33,-34,-35,-36,-20,-21,-22,-23,-24,-25,34,34,34,34,-37,-38,-39,-40,27,34,-42,-30,27,27,34,]),'LEQ':([3,11,41,49,52,59,60,61,62,74,75,76,77,78,80,82,83,],[28,-43,-41,28,28,-33,-34,-35,-36,-37,-38,-39,-40,28,-42,28,28,]),'GEQ':([3,11,41,49,52,59,60,61,62,74,75,76,77,78,80,82,83,],[29,-43,-41,29,29,-33,-34,-35,-36,-37,-38,-39,-40,29,-42,29,29,]),'LT':([3,11,41,49,52,59,60,61,62,74,75,76,77,78,80,82,83,],[30,-43,-41,30,30,-33,-34,-35,-36,-37,-38,-39,-40,30,-42,30,30,]),'GT':([3,11,41,49,52,59,60,61,62,74,75,76,77,78,80,82,83,],[31,-43,-41,31,31,-33,-34,-35,-36,-37,-38,-39,-40,31,-42,31,31,]),'EQOP':([3,4,11,13,14,41,49,50,51,52,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,],[32,35,-43,-31,-32,-41,32,35,35,32,-33,-34,-35,-36,-20,-21,-22,-23,-24,-25,35,35,35,35,-37,-38,-39,-40,32,35,-42,-30,32,32,35,]),'AND':([4,11,13,14,41,50,51,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,76,77,79,80,81,84,],[36,-43,-31,-32,-41,36,36,-33,-34,-35,-36,-20,-21,-22,-23,-24,-25,36,36,36,36,-37,-38,-39,-40,36,-42,-30,36,]),'OR':([4,11,13,14,41,50,51,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,76,77,79,80,81,84,],[37,-43,-31,-32,-41,37,37,-33,-34,-35,-36,-20,-21,-22,-23,-24,-25,37,37,37,37,-37,-38,-39,-40,37,-42,-30,37,]),'PEQ':([9,42,],[44,44,]),'MEQ':([9,42,],[45,45,]),'DEQ':([9,42,],[46,46,]),'TEQ':([9,42,],[47,47,]),'EQ':([9,15,55,57,58,],[48,54,-13,-14,-15,]),'RPAREN':([11,13,14,41,49,50,51,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,],[-43,-31,-32,-41,80,81,-29,-33,-34,-35,-36,-20,-21,-22,-23,-24,-25,-19,-26,-27,-28,80,-37,-38,-39,-40,-42,-30,80,]),'HAREM':([16,19,20,],[56,-17,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'multiState':([0,],[1,]),'statement':([0,1,],[2,21,]),'numExpr':([0,1,8,10,12,23,24,25,26,27,28,29,30,31,32,34,35,36,37,43,44,45,46,47,48,53,54,],[3,3,41,49,52,59,60,61,62,63,64,65,66,67,68,52,52,52,52,73,74,75,76,77,78,82,83,]),'boolExpr':([0,1,10,12,34,35,36,37,48,53,54,],[4,4,50,51,69,70,71,72,79,50,84,]),'declare':([0,1,],[5,5,]),'print':([0,1,],[6,6,]),'reassign':([0,1,],[7,7,]),'declaration':([0,1,18,],[15,15,58,]),'type':([0,1,18,],[16,16,16,]),'arrays':([0,1,18,],[17,17,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> multiState","S'",1,None,None,None),
  ('multiState -> statement','multiState',1,'p_multiStatements_expr','parser.py',17),
  ('multiState -> multiState statement','multiState',2,'p_multiStatements_expr','parser.py',18),
  ('statement -> numExpr SEMICOL','statement',2,'p_statement_expr','parser.py',23),
  ('statement -> boolExpr SEMICOL','statement',2,'p_statement_expr','parser.py',24),
  ('statement -> declare SEMICOL','statement',2,'p_statement_expr','parser.py',25),
  ('statement -> print SEMICOL','statement',2,'p_statement_expr','parser.py',26),
  ('statement -> reassign SEMICOL','statement',2,'p_statement_expr','parser.py',27),
  ('reassign -> ID EQ numExpr','reassign',3,'p_statement_reassign','parser.py',32),
  ('reassign -> ID EQ boolExpr','reassign',3,'p_statement_reassign','parser.py',33),
  ('declare -> declaration','declare',1,'p_statement_declare_or_assign','parser.py',40),
  ('declare -> declaration EQ numExpr','declare',3,'p_statement_declare_or_assign','parser.py',41),
  ('declare -> declaration EQ boolExpr','declare',3,'p_statement_declare_or_assign','parser.py',42),
  ('declaration -> type ID','declaration',2,'p_statement_declaration','parser.py',49),
  ('declaration -> arrays ID','declaration',2,'p_statement_declaration','parser.py',50),
  ('declaration -> REAL declaration','declaration',2,'p_statement_declaration','parser.py',51),
  ('arrays -> type HAREM','arrays',2,'p_arrays','parser.py',61),
  ('type -> WAIFU','type',1,'p_types','parser.py',66),
  ('type -> CATGIRL','type',1,'p_types','parser.py',67),
  ('boolExpr -> boolExpr NEQ boolExpr','boolExpr',3,'p_boolExpr_op','parser.py',72),
  ('boolExpr -> numExpr NEQ numExpr','boolExpr',3,'p_boolExpr_op','parser.py',73),
  ('boolExpr -> numExpr LEQ numExpr','boolExpr',3,'p_boolExpr_op','parser.py',74),
  ('boolExpr -> numExpr GEQ numExpr','boolExpr',3,'p_boolExpr_op','parser.py',75),
  ('boolExpr -> numExpr LT numExpr','boolExpr',3,'p_boolExpr_op','parser.py',76),
  ('boolExpr -> numExpr GT numExpr','boolExpr',3,'p_boolExpr_op','parser.py',77),
  ('boolExpr -> numExpr EQOP numExpr','boolExpr',3,'p_boolExpr_op','parser.py',78),
  ('boolExpr -> boolExpr EQOP boolExpr','boolExpr',3,'p_boolExpr_op','parser.py',79),
  ('boolExpr -> boolExpr AND boolExpr','boolExpr',3,'p_boolExpr_op','parser.py',80),
  ('boolExpr -> boolExpr OR boolExpr','boolExpr',3,'p_boolExpr_op','parser.py',81),
  ('boolExpr -> NOT boolExpr','boolExpr',2,'p_boolExpr_not','parser.py',95),
  ('boolExpr -> LPAREN boolExpr RPAREN','boolExpr',3,'p_boolExpr_group','parser.py',100),
  ('boolExpr -> OWO','boolExpr',1,'p_bool','parser.py',104),
  ('boolExpr -> UWU','boolExpr',1,'p_bool','parser.py',105),
  ('numExpr -> numExpr PLUS numExpr','numExpr',3,'p_numExpr_binop','parser.py',111),
  ('numExpr -> numExpr MINUS numExpr','numExpr',3,'p_numExpr_binop','parser.py',112),
  ('numExpr -> numExpr TIMES numExpr','numExpr',3,'p_numExpr_binop','parser.py',113),
  ('numExpr -> numExpr DIVIDE numExpr','numExpr',3,'p_numExpr_binop','parser.py',114),
  ('numExpr -> ID PEQ numExpr','numExpr',3,'p_numExpr_shortBinOp','parser.py',126),
  ('numExpr -> ID MEQ numExpr','numExpr',3,'p_numExpr_shortBinOp','parser.py',127),
  ('numExpr -> ID DEQ numExpr','numExpr',3,'p_numExpr_shortBinOp','parser.py',128),
  ('numExpr -> ID TEQ numExpr','numExpr',3,'p_numExpr_shortBinOp','parser.py',129),
  ('numExpr -> MINUS numExpr','numExpr',2,'p_numExpr_uminus','parser.py',146),
  ('numExpr -> LPAREN numExpr RPAREN','numExpr',3,'p_numExpr_group','parser.py',151),
  ('numExpr -> NUMBER','numExpr',1,'p_numExpr_number','parser.py',156),
  ('print -> ID','print',1,'p_print_var','parser.py',161),
]
