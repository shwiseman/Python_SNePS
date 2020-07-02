from . import WftLex
from .ply import *
from ..Network import *
from ..Caseframe import Frame, Fillers
from ..Node import Base, Molecular, Indefinite, Arbitrary, MinMaxOpNode
from ..Error import SNError

class SNePSWftError(SNError):
    pass

current_network = None
tokens = WftLex.tokens
topWft = None
assertedWfts = set()

# =====================================
# -------------- RULES ----------------
# =====================================

def p_Wft(p):
    '''
    Wft :               BinaryOp
         |              NaryOp
         |              MinMaxOp
         |              CloseStmt
         |              EveryStmt
         |              SomeStmt
         |              QIdenStmt
         |              AtomicName
         |              Y_WftNode
         |              Function
    '''
    p[0] = p[1]
    global topWft
    topWft = p[1]

# e.g. if(wft1, wft2)
def p_BinaryOp(p):
    '''
    BinaryOp :          Impl LParen Argument Comma Argument RParen
             |          OrImpl LParen Argument Comma Argument RParen
             |          AndImpl LParen Argument Comma Argument RParen
    '''
    if p[1] == "if" or p[1] == "orimpl":
        caseframe_name = p[1]
    else:
        caseframe_name = "andimpl"
    filler_set = [p[3], p[5]]
    p[0] = build_molecular(caseframe_name, filler_set)


# e.g. and(wft1, wft2)
def p_NaryOp(p):
    '''
    NaryOp :            And LParen Wfts RParen
           |            Or LParen Wfts RParen
           |            Not LParen Wfts RParen
           |            Nor LParen Wfts RParen
           |            Thnot LParen Wfts RParen
           |            Thnor LParen Wfts RParen
           |            Nand LParen Wfts RParen
           |            Xor LParen Wfts RParen
           |            DoubImpl LParen Wfts RParen
    '''
    filler_set = [Fillers(p[3])]
    p[0] = build_molecular(p[1], filler_set)

# e.g. thresh{1, 2}(wft1)
def p_MinMaxOp(p):
    '''
    MinMaxOp :          AndOr LBrace Integer Comma Integer RBrace LParen Wfts RParen
             |          Thresh LBrace Integer Comma Integer RBrace LParen Wfts RParen
             |          Thresh LBrace Integer RBrace LParen Wfts RParen
    '''
    min = p[3]
    if len(p) == 8:
        filler_set = [Fillers(p[6])]
        max = int(len(p[6])) - 1
    else:
        max = int(p[5])
        filler_set = [Fillers(p[8])]
    p[0] = build_minmax(p[1], filler_set, min, max)

# e.g. every{x}(Isa(x, Dog))
def p_EveryStmt(p):
    '''
    EveryStmt :         Every LParen AtomicName Comma Argument RParen
    '''

# e.g. some{x(y)}(Isa(x, y))
def p_SomeStmt(p):
    '''
    SomeStmt :          Some LParen AtomicName LParen AtomicName RParen Comma Argument RParen
    '''

# e.g. close(Dog, wft1)
def p_CloseStmt(p):
    '''
    CloseStmt :         Close LParen AtomicNameSet Comma Wft RParen
    '''


# e.g. brothers(Tom, Ted)
def p_Function(p):
    '''
    Function :          Identifier LParen Arguments RParen
             |          Integer LParen Arguments RParen
    '''
    filler_set = p[3]
    p[0] = build_molecular(p[1], filler_set)

# e.g. ?example()
def p_QIdenStmt(p):
    '''
    QIdenStmt :         QIdentifier LParen Wfts RParen
              |         QIdentifier LParen RParen
    '''
    raise SNePSWftError("Not yet implemented!")

# e.g. wft1
def p_Argument1(p):
    '''
    Argument :          Wft
    '''
    p[0] = Fillers([p[1]])

# e.g. None
def p_Argument2(p):
    '''
    Argument :          None
    '''
    p[0] = Fillers()

# e.g. setOf(wft1, wft2)
def p_Argument3(p):
    '''
    Argument :          ArgumentFunction
             |          LBracket RBracket
             |          LBracket Wfts RBracket
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = Fillers()
    else:
        p[0] = Fillers(p[2])

def p_ArgumentFunction(p):
    '''
    ArgumentFunction :  SetOf LParen RParen
        |               SetOf LParen Wfts RParen
    '''
    if len(p) == 4:
        p[0] = Fillers()
    else:
        p[0] = Fillers(p[3])

def p_Wfts(p):
    '''
    Wfts :              Wft
         |              Wfts Comma Wft
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_Arguments(p):
    '''
    Arguments :         Argument
              |         Arguments Comma Argument
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_AtomicNameSet(p):
    '''
    AtomicNameSet :     AtomicName
                  |     LParen AtomicNames RParen
    '''


def p_AtomicNames(p):
    '''
    AtomicNames :       AtomicName
                |       AtomicNames Comma AtomicName
    '''


def p_AtomicName(p):
    '''
    AtomicName :        Identifier
               |        Integer
    '''
    current_network.define_term(p[1])
    p[0] = current_network.find_term(p[1])

def p_AtomicName2(p):
    '''
    Y_WftNode :         WftNode
    '''
    if int(p[1][3:]) >= Molecular.counter:
        raise SNePSWftError('Invalid wft number. Max number: {}'.format(Molecular.counter - 1))

    p[0] = current_network.nodes[p[1]]

def p_error(p):
    if p is None:
        raise SNePSWftError("PARSING FAILED: Term reached end unexpectedly.")
    else:
        raise SNePSWftError("PARSING FAILED: Syntax error on token '" + p.type + "'")

# =====================================
# ------------ RULES END --------------
# =====================================

def build_molecular(caseframe_name, filler_set):
    """ Builds and returns (or simply returns) a Molecular node from given parameters """
    caseframe = current_network.find_caseframe(caseframe_name)
    frame = Frame(caseframe, filler_set)
    for node in current_network.nodes.values():
        if node.has_frame(frame):
            return node
    wftNode = Molecular(frame)
    current_network.nodes[wftNode.name] = wftNode
    assertedWfts.add(wftNode)
    return wftNode


def build_minmax (caseframe_name, filler_set, min, max):
    """ Builds and returns (or simply returns) a MinMaxOp node from given parameters """
    caseframe = current_network.find_caseframe(caseframe_name)
    frame = Frame(caseframe, filler_set)
    for node in current_network.nodes.values():
        if node.has_frame(frame) and node.has_min_max(min, max):
            return node
    wftNode = MinMaxOpNode(frame, min, max)
    current_network.nodes[wftNode.name] = wftNode
    assertedWfts.add(wftNode)
    return wftNode


def wft_parser(wft, network):
    global current_network
    current_network = network
    yacc.yacc()
    if wft != '':
        try:
            yacc.parse(wft)
            global topWft
            global assertedWfts
            return (topWft, assertedWfts)
        except SNError as e:
            if type(e) is not SNePSWftError:
                print("PARSING FAILED:\n\t", end='')
            print(e)
