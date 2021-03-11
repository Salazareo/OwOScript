
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftQMARKCOLleftANDORleftNEQLEQGEQLTGTEQOPleftPLUSMINUSleftTIMESDIVIDEMODleftPOWrightUMINUSNOTleftLPARENRPARENAND BAKA CATGIRL CHAN COL COMMA DEQ DESU DIVIDE EQ EQOP GEQ GT HAREM ID ISTUDIED KUN LBRACE LBRACK LEQ LPAREN LT MEQ MINUS MM MOD MULTID NANI NEQ NOT NOU NUMBER OR OWO PEQ PERIOD PLUS POW PP QMARK RBRACE RBRACK REAL RPAREN SAMA SAN SEMICOL SHI SQUIGGLY TEQ TIMES UWU WAIFU WHILEU YOKAI program : stmts_or_empty stmts_or_empty : statements\n                       | empty\n     statements : statements singleStatement\n                   | singleStatement\n     singleStatement : expr SEMICOL\n                        | assignment SEMICOL\n                        | declaration SEMICOL\n                        | functionDeclaration\n                        | whileLoop\n                        | forLoop\n                        | conditional\n                        | returnStatement SEMICOL\n     expr : literal\n             | arrayLiteral\n             | reference\n             | functionCall\n             | ternaryOp\n\n     expr : LPAREN expr RPAREN\n     expr : expr PLUS expr\n             | expr MINUS expr\n             | expr TIMES expr\n             | expr DIVIDE expr\n             | expr MOD expr\n             | expr POW expr\n             | expr NEQ expr\n             | expr LEQ expr\n             | expr GEQ expr\n             | expr LT expr\n             | expr GT expr\n             | expr EQOP expr\n     expr : expr AND expr\n             | expr OR expr\n    expr : NOT exprexpr : MINUS expr %prec UMINUS ternaryOp : expr QMARK expr COL expr\n    assignment : reassign\n                  | initialize\n                  | arrayAssign\n                  | binOpAssign\n     conditional : if else\n                    | if\n     if : NANI LPAREN expr RPAREN newScope enclosure popScope\n           | NANI LPAREN expr RPAREN newScope singleStatement popScope\n     else : NOU newScope enclosure popScope\n             | NOU newScope singleStatement popScope\n     reassign : ID EQ expr\n     functionDeclaration : newFn newScope LPAREN argumentDeclaration RPAREN enclosure popScope\n     enclosure : LBRACE RBRACE\n                  | LBRACE statements RBRACE\n    newFn : fnType SQUIGGLY honorific IDnewScope :  returnStatement : expr DESU\n    popScope :  honorific : CHAN\n                  | KUN\n                  | SAN\n                  | SAMA\n     arrayAssign : ID LBRACK expr RBRACK EQ expr\n     functionCall : printCall\n                     | ID LPAREN exprLst RPAREN\n                     | ID LPAREN RPAREN\n     arrayLiteral : LBRACK RBRACK\n                     | LBRACK exprLst RBRACK\n     exprLst : expr\n                | expr COMMA exprLst\n     initialize : letInitialize\n                   | constInitialize\n     letInitialize : declaration EQ expr\n     constInitialize : constDeclaration EQ expr\n     declaration : arrayDeclaration\n                    | letDeclaration\n     binOpAssign : ID PEQ expr\n                    | ID MEQ expr\n                    | ID TEQ expr\n                    | ID DEQ expr\n                    | ID PP\n                    | ID MM\n    argumentDeclaration : declaration\n                           | declaration COMMA argumentDeclaration\n                           |\n    constDeclaration : REAL arrayDeclaration\n                        | REAL letDeclaration\n    arrayDeclaration : type HAREM IDletDeclaration : type IDwhileLoop : WHILEU LPAREN expr RPAREN ISTUDIED newScope enclosure popScope\n    forLoop : SHI newScope LPAREN forTrio RPAREN enclosure popScope\n               | SHI newScope LPAREN forElement RPAREN enclosure popScope\n     forTrio : forAssign SEMICOL expr SEMICOL forReassign\n     forAssign : reassign\n                  | letInitialize\n                  | arrayAssign\n                  | binOpAssign\n     forReassign : reassign\n                    | arrayAssign    \n                    | binOpAssign\n     forElement : declaration COL ID\n                   | constDeclaration COL ID\n    printCall : BAKA LPAREN exprLst RPARENreference : letReference\n                 | arrayReference\n    letReference : ID\n     arrayReference : ID LBRACK expr RBRACK literal : NUMBER literal : OWO\n                | UWU\n     fnType : YOKAI\n               | type\n    type : WAIFU\n            | CATGIRL\n    empty : '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,9,10,11,12,31,51,52,69,70,72,80,159,160,179,180,181,185,188,189,194,196,197,198,199,200,201,204,205,206,],[-111,0,-1,-2,-3,-5,-9,-10,-11,-12,-42,-4,-6,-7,-8,-13,-41,-54,-54,-45,-46,-49,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'LPAREN':([0,3,5,9,10,11,12,19,20,21,28,29,30,31,35,39,44,45,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,74,77,78,79,80,81,85,86,87,88,89,90,91,97,98,99,120,124,126,144,159,160,161,165,166,175,177,179,180,181,182,183,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[19,19,-5,-9,-10,-11,-12,19,19,19,-52,78,-52,-42,19,85,97,98,-4,-6,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-7,-8,19,-13,85,121,19,123,-41,-52,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-54,-54,19,-51,-52,19,19,-45,-46,-49,19,19,19,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'NOT':([0,3,5,9,10,11,12,19,20,21,31,35,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,78,80,81,85,86,87,88,89,90,91,97,98,99,120,124,126,144,159,160,161,166,175,177,179,180,181,182,183,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[21,21,-5,-9,-10,-11,-12,21,21,21,-42,21,-4,-6,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-7,-8,21,-13,21,-41,-52,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-54,-54,21,-52,21,21,-45,-46,-49,21,21,21,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'MINUS':([0,3,5,6,9,10,11,12,14,15,16,17,18,19,20,21,31,32,33,34,35,36,37,38,39,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,78,80,81,82,84,85,86,87,88,89,90,91,97,98,99,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,124,125,126,128,129,130,131,132,133,134,141,143,144,145,159,160,161,163,164,166,167,168,169,175,177,179,180,181,182,183,184,185,188,189,190,192,194,195,196,197,198,199,200,201,204,205,206,],[20,20,-5,54,-9,-10,-11,-12,-14,-15,-16,-17,-18,20,20,20,-42,-104,-105,-106,20,-100,-101,-60,-102,-4,-6,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-7,-8,20,-13,54,-102,-35,-34,20,-41,-52,-63,54,20,20,20,20,20,20,20,20,20,20,-20,-21,-22,-23,-24,-25,54,54,54,54,54,54,54,54,54,54,-19,20,54,20,-64,20,-62,54,54,54,54,54,54,54,54,20,54,-54,-54,20,-61,-103,-52,-99,54,-103,20,20,-45,-46,-49,20,20,20,-54,-54,-54,54,54,-50,54,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'WHILEU':([0,3,5,9,10,11,12,31,51,52,69,70,72,80,81,124,159,160,161,166,179,180,181,182,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[29,29,-5,-9,-10,-11,-12,-42,-4,-6,-7,-8,-13,-41,-52,29,-54,-54,29,-52,-45,-46,-49,29,29,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'SHI':([0,3,5,9,10,11,12,31,51,52,69,70,72,80,81,124,159,160,161,166,179,180,181,182,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[30,30,-5,-9,-10,-11,-12,-42,-4,-6,-7,-8,-13,-41,-52,30,-54,-54,30,-52,-45,-46,-49,30,30,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'NUMBER':([0,3,5,9,10,11,12,19,20,21,31,35,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,78,80,81,85,86,87,88,89,90,91,97,98,99,120,124,126,144,159,160,161,166,175,177,179,180,181,182,183,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[32,32,-5,-9,-10,-11,-12,32,32,32,-42,32,-4,-6,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-7,-8,32,-13,32,-41,-52,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-54,-54,32,-52,32,32,-45,-46,-49,32,32,32,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'OWO':([0,3,5,9,10,11,12,19,20,21,31,35,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,78,80,81,85,86,87,88,89,90,91,97,98,99,120,124,126,144,159,160,161,166,175,177,179,180,181,182,183,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[33,33,-5,-9,-10,-11,-12,33,33,33,-42,33,-4,-6,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-7,-8,33,-13,33,-41,-52,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-54,-54,33,-52,33,33,-45,-46,-49,33,33,33,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'UWU':([0,3,5,9,10,11,12,19,20,21,31,35,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,78,80,81,85,86,87,88,89,90,91,97,98,99,120,124,126,144,159,160,161,166,175,177,179,180,181,182,183,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[34,34,-5,-9,-10,-11,-12,34,34,34,-42,34,-4,-6,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-7,-8,34,-13,34,-41,-52,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-54,-54,34,-52,34,34,-45,-46,-49,34,34,34,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'LBRACK':([0,3,5,9,10,11,12,19,20,21,31,35,39,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,74,78,80,81,85,86,87,88,89,90,91,97,98,99,120,124,126,144,153,159,160,161,166,175,177,179,180,181,182,183,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[35,35,-5,-9,-10,-11,-12,35,35,35,-42,35,87,-4,-6,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-7,-8,35,-13,120,35,-41,-52,35,35,35,35,35,35,35,35,35,35,35,35,35,35,177,-54,-54,35,-52,35,35,-45,-46,-49,35,35,35,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'ID':([0,3,5,9,10,11,12,19,20,21,31,35,42,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,78,80,81,85,86,87,88,89,90,91,94,97,98,99,102,120,123,124,126,136,137,138,139,140,144,159,160,161,166,175,176,177,178,179,180,181,182,183,184,185,188,189,194,196,197,198,199,200,201,202,204,205,206,],[39,39,-5,-9,-10,-11,-12,74,74,74,-42,74,95,-109,-110,-4,-6,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,-7,-8,74,-13,74,-41,-52,74,74,74,74,74,74,74,135,74,74,74,95,74,153,39,74,165,-55,-56,-57,-58,74,-54,-54,39,-52,74,191,74,193,-45,-46,-49,39,74,39,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,153,-43,-44,-86,]),'NANI':([0,3,5,9,10,11,12,31,51,52,69,70,72,80,81,124,159,160,161,166,179,180,181,182,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[44,44,-5,-9,-10,-11,-12,-42,-4,-6,-7,-8,-13,-41,-52,44,-54,-54,44,-52,-45,-46,-49,44,44,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'BAKA':([0,3,5,9,10,11,12,19,20,21,31,35,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,78,80,81,85,86,87,88,89,90,91,97,98,99,120,124,126,144,159,160,161,166,175,177,179,180,181,182,183,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[45,45,-5,-9,-10,-11,-12,45,45,45,-42,45,-4,-6,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-7,-8,45,-13,45,-41,-52,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-54,-54,45,-52,45,45,-45,-46,-49,45,45,45,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'WAIFU':([0,3,5,9,10,11,12,31,50,51,52,69,70,72,80,81,121,123,124,159,160,161,166,171,179,180,181,182,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[47,47,-5,-9,-10,-11,-12,-42,47,-4,-6,-7,-8,-13,-41,-52,47,47,47,-54,-54,47,-52,47,-45,-46,-49,47,47,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'CATGIRL':([0,3,5,9,10,11,12,31,50,51,52,69,70,72,80,81,121,123,124,159,160,161,166,171,179,180,181,182,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[48,48,-5,-9,-10,-11,-12,-42,48,-4,-6,-7,-8,-13,-41,-52,48,48,48,-54,-54,48,-52,48,-45,-46,-49,48,48,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'YOKAI':([0,3,5,9,10,11,12,31,51,52,69,70,72,80,81,124,159,160,161,166,179,180,181,182,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[49,49,-5,-9,-10,-11,-12,-42,-4,-6,-7,-8,-13,-41,-52,49,-54,-54,49,-52,-45,-46,-49,49,49,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'REAL':([0,3,5,9,10,11,12,31,51,52,69,70,72,80,81,123,124,159,160,161,166,179,180,181,182,184,185,188,189,194,196,197,198,199,200,201,204,205,206,],[50,50,-5,-9,-10,-11,-12,-42,-4,-6,-7,-8,-13,-41,-52,50,50,-54,-54,50,-52,-45,-46,-49,50,50,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'RBRACE':([5,9,10,11,12,31,51,52,69,70,72,80,159,160,161,179,180,181,182,185,188,189,194,196,197,198,199,200,201,204,205,206,],[-5,-9,-10,-11,-12,-42,-4,-6,-7,-8,-13,-41,-54,-54,181,-45,-46,-49,194,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'SEMICOL':([6,7,8,13,14,15,16,17,18,22,23,24,25,26,27,32,33,34,36,37,38,39,40,41,67,74,75,76,82,92,93,95,103,104,105,106,107,108,109,110,111,112,113,114,115,116,118,119,125,128,129,131,132,133,134,135,143,151,155,156,157,158,163,164,167,168,169,190,195,],[52,69,70,72,-14,-15,-16,-17,-18,-37,-38,-39,-40,-71,-72,-104,-105,-106,-100,-101,-60,-102,-67,-68,-53,-102,-35,-34,-63,-77,-78,-85,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-69,-19,-64,-62,-47,-73,-74,-75,-76,-84,-70,175,-90,-91,-92,-93,-61,-103,-99,-36,-103,202,-59,]),'PLUS':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[53,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,53,-102,-35,-34,-63,53,-20,-21,-22,-23,-24,-25,53,53,53,53,53,53,53,53,53,53,-19,53,-64,-62,53,53,53,53,53,53,53,53,53,-61,-103,-99,53,-103,53,53,53,]),'TIMES':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[55,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,55,-102,-35,-34,-63,55,55,55,-22,-23,-24,-25,55,55,55,55,55,55,55,55,55,55,-19,55,-64,-62,55,55,55,55,55,55,55,55,55,-61,-103,-99,55,-103,55,55,55,]),'DIVIDE':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[56,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,56,-102,-35,-34,-63,56,56,56,-22,-23,-24,-25,56,56,56,56,56,56,56,56,56,56,-19,56,-64,-62,56,56,56,56,56,56,56,56,56,-61,-103,-99,56,-103,56,56,56,]),'MOD':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[57,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,57,-102,-35,-34,-63,57,57,57,-22,-23,-24,-25,57,57,57,57,57,57,57,57,57,57,-19,57,-64,-62,57,57,57,57,57,57,57,57,57,-61,-103,-99,57,-103,57,57,57,]),'POW':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[58,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,58,-102,-35,-34,-63,58,58,58,58,58,58,-25,58,58,58,58,58,58,58,58,58,58,-19,58,-64,-62,58,58,58,58,58,58,58,58,58,-61,-103,-99,58,-103,58,58,58,]),'NEQ':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[59,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,59,-102,-35,-34,-63,59,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,59,59,59,59,-19,59,-64,-62,59,59,59,59,59,59,59,59,59,-61,-103,-99,59,-103,59,59,59,]),'LEQ':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[60,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,60,-102,-35,-34,-63,60,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,60,60,60,60,-19,60,-64,-62,60,60,60,60,60,60,60,60,60,-61,-103,-99,60,-103,60,60,60,]),'GEQ':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[61,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,61,-102,-35,-34,-63,61,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,61,61,61,61,-19,61,-64,-62,61,61,61,61,61,61,61,61,61,-61,-103,-99,61,-103,61,61,61,]),'LT':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[62,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,62,-102,-35,-34,-63,62,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,62,62,62,62,-19,62,-64,-62,62,62,62,62,62,62,62,62,62,-61,-103,-99,62,-103,62,62,62,]),'GT':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[63,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,63,-102,-35,-34,-63,63,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,63,63,63,63,-19,63,-64,-62,63,63,63,63,63,63,63,63,63,-61,-103,-99,63,-103,63,63,63,]),'EQOP':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[64,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,64,-102,-35,-34,-63,64,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,64,64,64,64,-19,64,-64,-62,64,64,64,64,64,64,64,64,64,-61,-103,-99,64,-103,64,64,64,]),'AND':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[65,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,65,-102,-35,-34,-63,65,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,65,65,-19,65,-64,-62,65,65,65,65,65,65,65,65,65,-61,-103,-99,65,-103,65,65,65,]),'OR':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[66,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,66,-102,-35,-34,-63,66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,66,66,-19,66,-64,-62,66,66,66,66,66,66,66,66,66,-61,-103,-99,66,-103,66,66,66,]),'DESU':([6,14,15,16,17,18,32,33,34,36,37,38,39,74,75,76,82,103,104,105,106,107,108,109,110,111,112,113,114,115,116,119,125,128,163,164,167,168,169,],[67,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,-102,-35,-34,-63,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-19,-64,-62,-61,-103,-99,-36,-103,]),'QMARK':([6,14,15,16,17,18,32,33,34,36,37,38,39,73,74,75,76,82,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,125,128,129,130,131,132,133,134,141,143,145,163,164,167,168,169,190,192,195,],[68,-14,-15,-16,-17,-18,-104,-105,-106,-100,-101,-60,-102,68,-102,-35,-34,-63,68,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,68,68,-19,68,-64,-62,68,68,68,68,68,68,68,68,68,-61,-103,-99,-36,-103,68,68,68,]),'EQ':([8,26,27,39,46,95,100,101,135,152,153,164,203,],[71,-71,-72,86,99,-85,-82,-83,-84,71,86,183,183,]),'NOU':([9,10,11,12,31,52,69,70,72,80,159,160,179,180,181,185,188,189,194,196,197,198,199,200,201,204,205,206,],[-9,-10,-11,-12,81,-6,-7,-8,-13,-41,-54,-54,-45,-46,-49,-54,-54,-54,-50,-54,-54,-48,-54,-87,-88,-43,-44,-86,]),'RPAREN':([14,15,16,17,18,26,27,32,33,34,36,37,38,73,74,75,76,82,84,85,92,93,95,103,104,105,106,107,108,109,110,111,112,113,114,115,116,119,121,122,125,127,128,129,131,132,133,134,135,141,142,146,147,149,150,162,163,167,168,169,171,186,191,193,195,207,208,209,210,],[-14,-15,-16,-17,-18,-71,-72,-104,-105,-106,-100,-101,-60,119,-102,-35,-34,-63,-65,128,-77,-78,-85,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-19,-81,148,-64,163,-62,-47,-73,-74,-75,-76,-84,166,167,170,-79,173,174,-66,-61,-99,-36,-103,-81,-80,-97,-98,-59,-89,-94,-95,-96,]),'COMMA':([14,15,16,17,18,26,27,32,33,34,36,37,38,74,75,76,82,84,95,103,104,105,106,107,108,109,110,111,112,113,114,115,116,119,125,128,135,147,163,167,168,169,],[-14,-15,-16,-17,-18,-71,-72,-104,-105,-106,-100,-101,-60,-102,-35,-34,-63,126,-85,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-19,-64,-62,-84,171,-61,-99,-36,-103,]),'RBRACK':([14,15,16,17,18,32,33,34,35,36,37,38,74,75,76,82,83,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,119,125,128,130,145,162,163,167,168,169,192,],[-14,-15,-16,-17,-18,-104,-105,-106,82,-100,-101,-60,-102,-35,-34,-63,125,-65,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-19,-64,-62,164,169,-66,-61,-99,-36,-103,203,]),'COL':([14,15,16,17,18,26,27,32,33,34,36,37,38,74,75,76,82,95,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,125,128,135,152,154,163,167,168,169,],[-14,-15,-16,-17,-18,-71,-72,-104,-105,-106,-100,-101,-60,-102,-35,-34,-63,-85,-82,-83,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,144,-19,-64,-62,-84,176,178,-61,-99,-36,-103,]),'PEQ':([39,153,],[88,88,]),'MEQ':([39,153,],[89,89,]),'TEQ':([39,153,],[90,90,]),'DEQ':([39,153,],[91,91,]),'PP':([39,153,],[92,92,]),'MM':([39,153,],[93,93,]),'HAREM':([42,47,48,102,],[94,-109,-110,94,]),'SQUIGGLY':([42,43,47,48,49,],[-108,96,-109,-110,-107,]),'LBRACE':([81,124,166,170,172,173,174,184,187,],[-52,161,-52,161,-52,161,161,161,161,]),'CHAN':([96,],[137,]),'KUN':([96,],[138,]),'SAN':([96,],[139,]),'SAMA':([96,],[140,]),'ISTUDIED':([148,],[172,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmts_or_empty':([0,],[2,]),'statements':([0,161,],[3,182,]),'empty':([0,],[4,]),'singleStatement':([0,3,124,161,182,184,],[5,51,160,5,51,197,]),'expr':([0,3,19,20,21,35,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,78,85,86,87,88,89,90,91,97,98,99,120,124,126,144,161,175,177,182,183,184,],[6,6,73,75,76,84,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,84,129,130,131,132,133,134,141,84,143,145,6,84,168,6,190,192,6,195,6,]),'assignment':([0,3,124,161,182,184,],[7,7,7,7,7,7,]),'declaration':([0,3,121,123,124,161,171,182,184,],[8,8,147,152,8,8,147,8,8,]),'functionDeclaration':([0,3,124,161,182,184,],[9,9,9,9,9,9,]),'whileLoop':([0,3,124,161,182,184,],[10,10,10,10,10,10,]),'forLoop':([0,3,124,161,182,184,],[11,11,11,11,11,11,]),'conditional':([0,3,124,161,182,184,],[12,12,12,12,12,12,]),'returnStatement':([0,3,124,161,182,184,],[13,13,13,13,13,13,]),'literal':([0,3,19,20,21,35,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,78,85,86,87,88,89,90,91,97,98,99,120,124,126,144,161,175,177,182,183,184,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'arrayLiteral':([0,3,19,20,21,35,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,78,85,86,87,88,89,90,91,97,98,99,120,124,126,144,161,175,177,182,183,184,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'reference':([0,3,19,20,21,35,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,78,85,86,87,88,89,90,91,97,98,99,120,124,126,144,161,175,177,182,183,184,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'functionCall':([0,3,19,20,21,35,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,78,85,86,87,88,89,90,91,97,98,99,120,124,126,144,161,175,177,182,183,184,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'ternaryOp':([0,3,19,20,21,35,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,78,85,86,87,88,89,90,91,97,98,99,120,124,126,144,161,175,177,182,183,184,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'reassign':([0,3,123,124,161,182,184,202,],[22,22,155,22,22,22,22,208,]),'initialize':([0,3,124,161,182,184,],[23,23,23,23,23,23,]),'arrayAssign':([0,3,123,124,161,182,184,202,],[24,24,157,24,24,24,24,209,]),'binOpAssign':([0,3,123,124,161,182,184,202,],[25,25,158,25,25,25,25,210,]),'arrayDeclaration':([0,3,50,121,123,124,161,171,182,184,],[26,26,100,26,26,26,26,26,26,26,]),'letDeclaration':([0,3,50,121,123,124,161,171,182,184,],[27,27,101,27,27,27,27,27,27,27,]),'newFn':([0,3,124,161,182,184,],[28,28,28,28,28,28,]),'if':([0,3,124,161,182,184,],[31,31,31,31,31,31,]),'letReference':([0,3,19,20,21,35,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,78,85,86,87,88,89,90,91,97,98,99,120,124,126,144,161,175,177,182,183,184,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'arrayReference':([0,3,19,20,21,35,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,78,85,86,87,88,89,90,91,97,98,99,120,124,126,144,161,175,177,182,183,184,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'printCall':([0,3,19,20,21,35,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,71,78,85,86,87,88,89,90,91,97,98,99,120,124,126,144,161,175,177,182,183,184,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'letInitialize':([0,3,123,124,161,182,184,],[40,40,156,40,40,40,40,]),'constInitialize':([0,3,124,161,182,184,],[41,41,41,41,41,41,]),'type':([0,3,50,121,123,124,161,171,182,184,],[42,42,102,102,102,42,42,102,42,42,]),'fnType':([0,3,124,161,182,184,],[43,43,43,43,43,43,]),'constDeclaration':([0,3,123,124,161,182,184,],[46,46,154,46,46,46,46,]),'newScope':([28,30,81,166,172,],[77,79,124,184,187,]),'else':([31,],[80,]),'exprLst':([35,85,98,126,],[83,127,142,162,]),'honorific':([96,],[136,]),'argumentDeclaration':([121,171,],[146,186,]),'forTrio':([123,],[149,]),'forElement':([123,],[150,]),'forAssign':([123,],[151,]),'enclosure':([124,170,173,174,184,187,],[159,185,188,189,196,199,]),'popScope':([159,160,185,188,189,196,197,199,],[179,180,198,200,201,204,205,206,]),'forReassign':([202,],[207,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmts_or_empty','program',1,'p_program','parser.py',44),
  ('stmts_or_empty -> statements','stmts_or_empty',1,'p_statements_or_empty','parser.py',49),
  ('stmts_or_empty -> empty','stmts_or_empty',1,'p_statements_or_empty','parser.py',50),
  ('statements -> statements singleStatement','statements',2,'p_statements','parser.py',56),
  ('statements -> singleStatement','statements',1,'p_statements','parser.py',57),
  ('singleStatement -> expr SEMICOL','singleStatement',2,'p_singleStatement','parser.py',63),
  ('singleStatement -> assignment SEMICOL','singleStatement',2,'p_singleStatement','parser.py',64),
  ('singleStatement -> declaration SEMICOL','singleStatement',2,'p_singleStatement','parser.py',65),
  ('singleStatement -> functionDeclaration','singleStatement',1,'p_singleStatement','parser.py',66),
  ('singleStatement -> whileLoop','singleStatement',1,'p_singleStatement','parser.py',67),
  ('singleStatement -> forLoop','singleStatement',1,'p_singleStatement','parser.py',68),
  ('singleStatement -> conditional','singleStatement',1,'p_singleStatement','parser.py',69),
  ('singleStatement -> returnStatement SEMICOL','singleStatement',2,'p_singleStatement','parser.py',70),
  ('expr -> literal','expr',1,'p_expr','parser.py',76),
  ('expr -> arrayLiteral','expr',1,'p_expr','parser.py',77),
  ('expr -> reference','expr',1,'p_expr','parser.py',78),
  ('expr -> functionCall','expr',1,'p_expr','parser.py',79),
  ('expr -> ternaryOp','expr',1,'p_expr','parser.py',80),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_paren_expr','parser.py',86),
  ('expr -> expr PLUS expr','expr',3,'p_boolExpr','parser.py',95),
  ('expr -> expr MINUS expr','expr',3,'p_boolExpr','parser.py',96),
  ('expr -> expr TIMES expr','expr',3,'p_boolExpr','parser.py',97),
  ('expr -> expr DIVIDE expr','expr',3,'p_boolExpr','parser.py',98),
  ('expr -> expr MOD expr','expr',3,'p_boolExpr','parser.py',99),
  ('expr -> expr POW expr','expr',3,'p_boolExpr','parser.py',100),
  ('expr -> expr NEQ expr','expr',3,'p_boolExpr','parser.py',101),
  ('expr -> expr LEQ expr','expr',3,'p_boolExpr','parser.py',102),
  ('expr -> expr GEQ expr','expr',3,'p_boolExpr','parser.py',103),
  ('expr -> expr LT expr','expr',3,'p_boolExpr','parser.py',104),
  ('expr -> expr GT expr','expr',3,'p_boolExpr','parser.py',105),
  ('expr -> expr EQOP expr','expr',3,'p_boolExpr','parser.py',106),
  ('expr -> expr AND expr','expr',3,'p_boolExpr_op','parser.py',149),
  ('expr -> expr OR expr','expr',3,'p_boolExpr_op','parser.py',150),
  ('expr -> NOT expr','expr',2,'p_boolExprNeg','parser.py',165),
  ('expr -> MINUS expr','expr',2,'p_numExpr_uminus','parser.py',172),
  ('ternaryOp -> expr QMARK expr COL expr','ternaryOp',5,'p_ternaryOp','parser.py',178),
  ('assignment -> reassign','assignment',1,'p_assignment','parser.py',187),
  ('assignment -> initialize','assignment',1,'p_assignment','parser.py',188),
  ('assignment -> arrayAssign','assignment',1,'p_assignment','parser.py',189),
  ('assignment -> binOpAssign','assignment',1,'p_assignment','parser.py',190),
  ('conditional -> if else','conditional',2,'p_conditional','parser.py',196),
  ('conditional -> if','conditional',1,'p_conditional','parser.py',197),
  ('if -> NANI LPAREN expr RPAREN newScope enclosure popScope','if',7,'p_if','parser.py',203),
  ('if -> NANI LPAREN expr RPAREN newScope singleStatement popScope','if',7,'p_if','parser.py',204),
  ('else -> NOU newScope enclosure popScope','else',4,'p_else','parser.py',210),
  ('else -> NOU newScope singleStatement popScope','else',4,'p_else','parser.py',211),
  ('reassign -> ID EQ expr','reassign',3,'p_reassign','parser.py',217),
  ('functionDeclaration -> newFn newScope LPAREN argumentDeclaration RPAREN enclosure popScope','functionDeclaration',7,'p_functionDeclaration','parser.py',236),
  ('enclosure -> LBRACE RBRACE','enclosure',2,'p_enclosure','parser.py',246),
  ('enclosure -> LBRACE statements RBRACE','enclosure',3,'p_enclosure','parser.py',247),
  ('newFn -> fnType SQUIGGLY honorific ID','newFn',4,'p_newFn','parser.py',253),
  ('newScope -> <empty>','newScope',0,'p_newScope','parser.py',260),
  ('returnStatement -> expr DESU','returnStatement',2,'p_returnStatement','parser.py',268),
  ('popScope -> <empty>','popScope',0,'p_popScope','parser.py',275),
  ('honorific -> CHAN','honorific',1,'p_honorific','parser.py',283),
  ('honorific -> KUN','honorific',1,'p_honorific','parser.py',284),
  ('honorific -> SAN','honorific',1,'p_honorific','parser.py',285),
  ('honorific -> SAMA','honorific',1,'p_honorific','parser.py',286),
  ('arrayAssign -> ID LBRACK expr RBRACK EQ expr','arrayAssign',6,'p_arrayAssign','parser.py',292),
  ('functionCall -> printCall','functionCall',1,'p_functionCall','parser.py',307),
  ('functionCall -> ID LPAREN exprLst RPAREN','functionCall',4,'p_functionCall','parser.py',308),
  ('functionCall -> ID LPAREN RPAREN','functionCall',3,'p_functionCall','parser.py',309),
  ('arrayLiteral -> LBRACK RBRACK','arrayLiteral',2,'p_arrayLiteral','parser.py',328),
  ('arrayLiteral -> LBRACK exprLst RBRACK','arrayLiteral',3,'p_arrayLiteral','parser.py',329),
  ('exprLst -> expr','exprLst',1,'p_exprList','parser.py',340),
  ('exprLst -> expr COMMA exprLst','exprLst',3,'p_exprList','parser.py',341),
  ('initialize -> letInitialize','initialize',1,'p_initialize','parser.py',350),
  ('initialize -> constInitialize','initialize',1,'p_initialize','parser.py',351),
  ('letInitialize -> declaration EQ expr','letInitialize',3,'p_letInitialize','parser.py',357),
  ('constInitialize -> constDeclaration EQ expr','constInitialize',3,'p_constInitialize','parser.py',370),
  ('declaration -> arrayDeclaration','declaration',1,'p_declaration','parser.py',382),
  ('declaration -> letDeclaration','declaration',1,'p_declaration','parser.py',383),
  ('binOpAssign -> ID PEQ expr','binOpAssign',3,'p_binOpAssign','parser.py',390),
  ('binOpAssign -> ID MEQ expr','binOpAssign',3,'p_binOpAssign','parser.py',391),
  ('binOpAssign -> ID TEQ expr','binOpAssign',3,'p_binOpAssign','parser.py',392),
  ('binOpAssign -> ID DEQ expr','binOpAssign',3,'p_binOpAssign','parser.py',393),
  ('binOpAssign -> ID PP','binOpAssign',2,'p_binOpAssign','parser.py',394),
  ('binOpAssign -> ID MM','binOpAssign',2,'p_binOpAssign','parser.py',395),
  ('argumentDeclaration -> declaration','argumentDeclaration',1,'p_argumentDeclaration','parser.py',419),
  ('argumentDeclaration -> declaration COMMA argumentDeclaration','argumentDeclaration',3,'p_argumentDeclaration','parser.py',420),
  ('argumentDeclaration -> <empty>','argumentDeclaration',0,'p_argumentDeclaration','parser.py',421),
  ('constDeclaration -> REAL arrayDeclaration','constDeclaration',2,'p_constDeclaration','parser.py',433),
  ('constDeclaration -> REAL letDeclaration','constDeclaration',2,'p_constDeclaration','parser.py',434),
  ('arrayDeclaration -> type HAREM ID','arrayDeclaration',3,'p_arrayDeclaration','parser.py',442),
  ('letDeclaration -> type ID','letDeclaration',2,'p_letDeclaration','parser.py',451),
  ('whileLoop -> WHILEU LPAREN expr RPAREN ISTUDIED newScope enclosure popScope','whileLoop',8,'p_whileLoop','parser.py',458),
  ('forLoop -> SHI newScope LPAREN forTrio RPAREN enclosure popScope','forLoop',7,'p_forLoop','parser.py',465),
  ('forLoop -> SHI newScope LPAREN forElement RPAREN enclosure popScope','forLoop',7,'p_forLoop','parser.py',466),
  ('forTrio -> forAssign SEMICOL expr SEMICOL forReassign','forTrio',5,'p_forTrio','parser.py',472),
  ('forAssign -> reassign','forAssign',1,'p_forAssign','parser.py',478),
  ('forAssign -> letInitialize','forAssign',1,'p_forAssign','parser.py',479),
  ('forAssign -> arrayAssign','forAssign',1,'p_forAssign','parser.py',480),
  ('forAssign -> binOpAssign','forAssign',1,'p_forAssign','parser.py',481),
  ('forReassign -> reassign','forReassign',1,'p_forReassign','parser.py',487),
  ('forReassign -> arrayAssign','forReassign',1,'p_forReassign','parser.py',488),
  ('forReassign -> binOpAssign','forReassign',1,'p_forReassign','parser.py',489),
  ('forElement -> declaration COL ID','forElement',3,'p_forElement','parser.py',495),
  ('forElement -> constDeclaration COL ID','forElement',3,'p_forElement','parser.py',496),
  ('printCall -> BAKA LPAREN exprLst RPAREN','printCall',4,'p_print','parser.py',503),
  ('reference -> letReference','reference',1,'p_reference','parser.py',511),
  ('reference -> arrayReference','reference',1,'p_reference','parser.py',512),
  ('letReference -> ID','letReference',1,'p_letReference','parser.py',518),
  ('arrayReference -> ID LBRACK expr RBRACK','arrayReference',4,'p_arrayReference','parser.py',535),
  ('literal -> NUMBER','literal',1,'p_numExpr_number','parser.py',550),
  ('literal -> OWO','literal',1,'p_bool','parser.py',555),
  ('literal -> UWU','literal',1,'p_bool','parser.py',556),
  ('fnType -> YOKAI','fnType',1,'p_fnType','parser.py',562),
  ('fnType -> type','fnType',1,'p_fnType','parser.py',563),
  ('type -> WAIFU','type',1,'p_type','parser.py',569),
  ('type -> CATGIRL','type',1,'p_type','parser.py',570),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',576),
]
