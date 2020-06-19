from .SemanticType import SemanticMixIn
from .Context import ContextMixIn
from .Slot import SlotMixIn
from .Node import NodeMixIn
from .Caseframe import CaseframeMixIn
from .WftParse import wft_parser
from sys import stderr

class Network(SlotMixIn, CaseframeMixIn, SemanticMixIn, NodeMixIn, ContextMixIn):
    def __init__(self):
        for cls in type(self).__bases__:
            cls.__init__(self)

        # self.nodes = {} (defined in Node.py)
        # self.caseframes = {} (defined in Caseframe.py)
        # self.slots = {} (defined in Slot.py)
        # self.sem_hierarchy = SemanticHierarchy() (defined in SemanticType.py)
        # self.contexts = {} (defined in Context.py)
        # self.default_context = Context("_default", docstring="The default context", hyps={}, ders={}) (defined in Context.py)
        self.build_default()

    def build_default(self):
        """ Builds the default context """

        # Types
        # =====

        # Entities
        self.define_type("Act")
        self.define_type("Propositional")
        self.define_type("Thing")
        self.define_type("Policy")

        # Propositional
        self.define_type("Proposition", ["Propositional"])
        self.define_type("WhQuestion", ["Propositional"])

        # Things
        self.define_type("Category", ["Thing"])
        self.define_type("Action", ["Thing"])

        self.define_caseframe("and", "Proposition", )


        # Slots
        # =====

        # Propositions

        # Rules

        # SNeRE

        # Condition-Action Rules


        # Caseframes
        # ==========

    def assert_wft(self, wft_str, value="hyp"):
        if value != "hyp" and value != "true":
            print("Invalid parameters on assertion. Must be either true or hyp.", file=stderr)
            return

        wft_parser(wft_str, self)
