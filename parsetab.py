
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'And AndImpl AndOr Close Comma DoubImpl Every Identifier Impl Integer LBrace LBracket LParen Nand None Nor Not Or OrImpl QIdentifier RBrace RBracket RParen SetOf Some Thnor Thnot Thresh WftNode Xor\n    Wft :               FWft\n        |               OWft\n    \n    FWft :              AtomicName\n         |              WftNode\n         |              Function\n    \n    OWft :              BinaryOp\n         |              NaryOp\n         |              MinMaxOp\n         |              CloseStmt\n         |              EveryStmt\n         |              SomeStmt\n         |              QIdenStmt\n    \n    BinaryOp :          Impl LParen Argument Comma Argument RParen\n             |          OrImpl LParen Argument Comma Argument RParen\n             |          AndImpl LParen Argument Comma Argument RParen\n    \n    NaryOp :            And LParen Wfts RParen\n           |            Or LParen Wfts RParen\n           |            Not LParen Wfts RParen\n           |            Nor LParen Wfts RParen\n           |            Thnot LParen Wfts RParen\n           |            Thnor LParen Wfts RParen\n           |            Nand LParen Wfts RParen\n           |            Xor LParen Wfts RParen\n           |            DoubImpl LParen Wfts RParen\n    \n    MinMaxOp :          AndOr LBrace Integer Comma Integer RBrace LParen Wfts RParen\n             |          Thresh LBrace Integer Comma Integer RBrace LParen Wfts RParen\n             |          Thresh LBrace Integer RBrace LParen Wfts RParen\n    \n    EveryStmt :         Every LBrace AtomicName RBrace LParen Wfts RParen\n              |         Every LBrace AtomicName RBrace LParen RParen\n    \n    SomeStmt :          Some LBrace AtomicName LParen AtomicName RParen RBrace LParen Wfts RParen\n             |          Some LBrace AtomicName LParen AtomicName RParen RBrace LParen RParen\n    \n    CloseStmt :         Close LParen AtomicNameSet Comma Wft RParen\n    \n    Function :          FWft LParen Arguments RParen\n    \n    QIdenStmt :         QIdentifier LParen Wfts RParen\n              |         QIdentifier LParen RParen\n    \n    Argument :          Wft\n             |          None\n             |          ArgumentFunction\n             |          LBracket Wfts RBracket\n             |          LBracket RBracket\n    \n    ArgumentFunction :  SetOf LParen Wfts RParen\n        |               SetOf LParen RParen\n    \n    Wfts :              Wft\n         |              Wfts Comma Wft\n    \n    Arguments :         Argument\n              |         Arguments Comma Argument\n    \n    AtomicNameSet :     AtomicName\n                  |     LParen AtomicNames RParen\n    \n    AtomicNames :       AtomicName\n                |       AtomicNames Comma AtomicName\n    \n    AtomicName :        Identifier\n               |        Integer\n    '
    
_lr_action_items = {'WftNode':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'Identifier':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,58,75,83,86,87,88,89,91,105,107,119,121,123,137,138,144,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'Integer':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,58,75,83,86,87,88,89,91,100,101,105,107,119,121,123,137,138,144,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,73,74,15,15,15,15,15,15,15,15,15,15,15,15,117,118,15,15,15,15,15,15,15,15,]),'Impl':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'OrImpl':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'AndImpl':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'And':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'Or':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'Not':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'Nor':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'Thnot':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'Thnor':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'Nand':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'Xor':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'DoubImpl':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'AndOr':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'Thresh':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'Close':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'Every':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'Some':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'QIdentifier':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,81,82,90,92,93,94,95,96,97,98,99,108,126,127,128,133,135,139,140,145,146,147,149,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-51,-52,-35,-33,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-13,-14,-15,-32,-29,-27,-28,-25,-26,-31,-30,]),'RParen':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,52,53,54,55,56,57,63,64,65,66,67,68,69,70,71,72,80,81,82,85,86,90,92,93,94,95,96,97,98,99,103,104,108,109,110,111,112,113,114,115,116,122,123,124,125,126,127,128,131,132,133,134,135,139,140,142,143,144,145,146,147,148,149,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-51,-52,81,82,-45,-36,-37,-38,90,-43,92,93,94,95,96,97,98,99,108,-35,-33,-40,112,-16,-17,-18,-19,-20,-21,-22,-23,-24,120,-49,-34,-46,-39,125,-42,126,127,128,-44,133,135,136,-41,-13,-14,-15,139,-50,-32,140,-29,-27,-28,145,146,147,-25,-26,-31,149,-30,]),'Comma':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,53,54,55,56,57,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,82,84,85,90,92,93,94,95,96,97,98,99,103,104,108,109,110,111,112,116,120,125,126,127,128,131,132,133,134,135,139,140,142,143,145,146,147,148,149,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-51,-52,83,-45,-36,-37,-38,87,88,89,91,-43,91,91,91,91,91,91,91,91,100,101,105,-47,91,-35,-33,91,-40,-16,-17,-18,-19,-20,-21,-22,-23,-24,121,-49,-34,-46,-39,91,-42,-44,-48,-41,-13,-14,-15,91,-50,-32,91,-29,-27,-28,91,91,-25,-26,-31,91,-30,]),'RBracket':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,58,64,81,82,84,90,92,93,94,95,96,97,98,99,108,116,126,127,128,133,135,139,140,145,146,147,149,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-51,-52,85,-43,-35,-33,110,-16,-17,-18,-19,-20,-21,-22,-23,-24,-34,-44,-13,-14,-15,-32,-29,-27,-28,-25,-26,-31,-30,]),'LParen':([2,4,5,6,14,15,16,17,18,19,20,21,22,23,24,25,26,27,30,33,49,59,79,82,102,106,129,130,141,],[34,-3,-4,-5,-51,-52,35,36,37,38,39,40,41,42,43,44,45,46,49,52,75,86,107,-33,119,123,137,138,144,]),'RBrace':([14,15,74,78,117,118,136,],[-51,-52,102,106,129,130,141,]),'LBrace':([28,29,31,32,],[47,48,50,51,]),'None':([34,35,36,37,83,87,88,89,],[56,56,56,56,56,56,56,56,]),'LBracket':([34,35,36,37,83,87,88,89,],[58,58,58,58,58,58,58,58,]),'SetOf':([34,35,36,37,83,87,88,89,],[59,59,59,59,59,59,59,59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Wft':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[1,55,55,55,55,64,64,64,64,64,64,64,64,64,64,64,55,64,55,55,55,116,122,64,64,64,64,64,]),'FWft':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'OWft':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'AtomicName':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,58,75,83,86,87,88,89,91,105,107,119,121,123,137,138,144,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,77,78,79,4,4,104,4,4,4,4,4,4,4,124,4,132,4,4,4,4,]),'Function':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'BinaryOp':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'NaryOp':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'MinMaxOp':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'CloseStmt':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'EveryStmt':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'SomeStmt':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'QIdenStmt':([0,34,35,36,37,38,39,40,41,42,43,44,45,46,52,58,83,86,87,88,89,91,105,119,123,137,138,144,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'Arguments':([34,],[53,]),'Argument':([34,35,36,37,83,87,88,89,],[54,60,61,62,109,113,114,115,]),'ArgumentFunction':([34,35,36,37,83,87,88,89,],[57,57,57,57,57,57,57,57,]),'Wfts':([38,39,40,41,42,43,44,45,46,52,58,86,119,123,137,138,144,],[63,65,66,67,68,69,70,71,72,80,84,111,131,134,142,143,148,]),'AtomicNameSet':([49,],[76,]),'AtomicNames':([75,],[103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Wft","S'",1,None,None,None),
  ('Wft -> FWft','Wft',1,'p_Wft','WftParse.py',15),
  ('Wft -> OWft','Wft',1,'p_Wft','WftParse.py',16),
  ('FWft -> AtomicName','FWft',1,'p_FWft','WftParse.py',23),
  ('FWft -> WftNode','FWft',1,'p_FWft','WftParse.py',24),
  ('FWft -> Function','FWft',1,'p_FWft','WftParse.py',25),
  ('OWft -> BinaryOp','OWft',1,'p_OWft','WftParse.py',32),
  ('OWft -> NaryOp','OWft',1,'p_OWft','WftParse.py',33),
  ('OWft -> MinMaxOp','OWft',1,'p_OWft','WftParse.py',34),
  ('OWft -> CloseStmt','OWft',1,'p_OWft','WftParse.py',35),
  ('OWft -> EveryStmt','OWft',1,'p_OWft','WftParse.py',36),
  ('OWft -> SomeStmt','OWft',1,'p_OWft','WftParse.py',37),
  ('OWft -> QIdenStmt','OWft',1,'p_OWft','WftParse.py',38),
  ('BinaryOp -> Impl LParen Argument Comma Argument RParen','BinaryOp',6,'p_BinaryOp','WftParse.py',44),
  ('BinaryOp -> OrImpl LParen Argument Comma Argument RParen','BinaryOp',6,'p_BinaryOp','WftParse.py',45),
  ('BinaryOp -> AndImpl LParen Argument Comma Argument RParen','BinaryOp',6,'p_BinaryOp','WftParse.py',46),
  ('NaryOp -> And LParen Wfts RParen','NaryOp',4,'p_NaryOp','WftParse.py',53),
  ('NaryOp -> Or LParen Wfts RParen','NaryOp',4,'p_NaryOp','WftParse.py',54),
  ('NaryOp -> Not LParen Wfts RParen','NaryOp',4,'p_NaryOp','WftParse.py',55),
  ('NaryOp -> Nor LParen Wfts RParen','NaryOp',4,'p_NaryOp','WftParse.py',56),
  ('NaryOp -> Thnot LParen Wfts RParen','NaryOp',4,'p_NaryOp','WftParse.py',57),
  ('NaryOp -> Thnor LParen Wfts RParen','NaryOp',4,'p_NaryOp','WftParse.py',58),
  ('NaryOp -> Nand LParen Wfts RParen','NaryOp',4,'p_NaryOp','WftParse.py',59),
  ('NaryOp -> Xor LParen Wfts RParen','NaryOp',4,'p_NaryOp','WftParse.py',60),
  ('NaryOp -> DoubImpl LParen Wfts RParen','NaryOp',4,'p_NaryOp','WftParse.py',61),
  ('MinMaxOp -> AndOr LBrace Integer Comma Integer RBrace LParen Wfts RParen','MinMaxOp',9,'p_MinMaxOp','WftParse.py',78),
  ('MinMaxOp -> Thresh LBrace Integer Comma Integer RBrace LParen Wfts RParen','MinMaxOp',9,'p_MinMaxOp','WftParse.py',79),
  ('MinMaxOp -> Thresh LBrace Integer RBrace LParen Wfts RParen','MinMaxOp',7,'p_MinMaxOp','WftParse.py',80),
  ('EveryStmt -> Every LBrace AtomicName RBrace LParen Wfts RParen','EveryStmt',7,'p_EveryStmt','WftParse.py',87),
  ('EveryStmt -> Every LBrace AtomicName RBrace LParen RParen','EveryStmt',6,'p_EveryStmt','WftParse.py',88),
  ('SomeStmt -> Some LBrace AtomicName LParen AtomicName RParen RBrace LParen Wfts RParen','SomeStmt',10,'p_SomeStmt','WftParse.py',95),
  ('SomeStmt -> Some LBrace AtomicName LParen AtomicName RParen RBrace LParen RParen','SomeStmt',9,'p_SomeStmt','WftParse.py',96),
  ('CloseStmt -> Close LParen AtomicNameSet Comma Wft RParen','CloseStmt',6,'p_CloseStmt','WftParse.py',103),
  ('Function -> FWft LParen Arguments RParen','Function',4,'p_Function','WftParse.py',110),
  ('QIdenStmt -> QIdentifier LParen Wfts RParen','QIdenStmt',4,'p_QIdenStmt','WftParse.py',117),
  ('QIdenStmt -> QIdentifier LParen RParen','QIdenStmt',3,'p_QIdenStmt','WftParse.py',118),
  ('Argument -> Wft','Argument',1,'p_Argument','WftParse.py',125),
  ('Argument -> None','Argument',1,'p_Argument','WftParse.py',126),
  ('Argument -> ArgumentFunction','Argument',1,'p_Argument','WftParse.py',127),
  ('Argument -> LBracket Wfts RBracket','Argument',3,'p_Argument','WftParse.py',128),
  ('Argument -> LBracket RBracket','Argument',2,'p_Argument','WftParse.py',129),
  ('ArgumentFunction -> SetOf LParen Wfts RParen','ArgumentFunction',4,'p_ArgumentFunction','WftParse.py',135),
  ('ArgumentFunction -> SetOf LParen RParen','ArgumentFunction',3,'p_ArgumentFunction','WftParse.py',136),
  ('Wfts -> Wft','Wfts',1,'p_Wfts','WftParse.py',142),
  ('Wfts -> Wfts Comma Wft','Wfts',3,'p_Wfts','WftParse.py',143),
  ('Arguments -> Argument','Arguments',1,'p_Arguments','WftParse.py',149),
  ('Arguments -> Arguments Comma Argument','Arguments',3,'p_Arguments','WftParse.py',150),
  ('AtomicNameSet -> AtomicName','AtomicNameSet',1,'p_AtomicNameSet','WftParse.py',156),
  ('AtomicNameSet -> LParen AtomicNames RParen','AtomicNameSet',3,'p_AtomicNameSet','WftParse.py',157),
  ('AtomicNames -> AtomicName','AtomicNames',1,'p_AtomicNames','WftParse.py',163),
  ('AtomicNames -> AtomicNames Comma AtomicName','AtomicNames',3,'p_AtomicNames','WftParse.py',164),
  ('AtomicName -> Identifier','AtomicName',1,'p_AtomicName','WftParse.py',170),
  ('AtomicName -> Integer','AtomicName',1,'p_AtomicName','WftParse.py',171),
]
