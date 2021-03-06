from __future__ import annotations # Allows type hints to reference self's type. Python 4.0 will have this feature by default.
from .Slot import *
from .SemanticType import SemanticType, SemanticHierarchy
from .SNError import SNError
from re import match
from typing import List, Set

# =====================================
# -------------- GLOBALS --------------
# =====================================

class CaseframeError(SNError):
    pass

# =====================================
# ------------- CASEFRAME -------------
# =====================================

class Caseframe:
    def __init__(self, name: str, sem_type: SemanticType,
                 sem_hierarchy: SemanticHierarchy,
                 docstring: str, slots: List[Slot]) -> None:
        self.name = name
        self.sem_type = sem_type
        self.sem_hierarchy = sem_hierarchy
        self.docstring = docstring
        self.slots = slots
        self.aliases = set([self.name])
        self.adj_to = set()
        self.adj_from = set()

    def add_alias(self, alias: str) -> None:
        """ Adds new alias to array """
        self.aliases.add(alias)

    def has_alias(self, alias: str) -> bool:
        """ Checks if string in aliases """
        return alias in self.aliases

    def __eq__(self, other: Caseframe) -> bool:
        """ Returns true if both arguments are equivalent caseframes.
            Two caseframes are equivalent when:
                1. They have the same type
                2. They have the same slots (disregarding order) """
        return other is not None and self.sem_type is other.sem_type and self.slots == other.slots

    def __hash__(self) -> int:
        return id(self) # Caseframes are unique

    def __str__(self) -> str:
        return "<{}>: {}\n".format(self.name, self.docstring) + \
               "\tSemantic Type: {}\n".format(self.sem_type.name) + \
               "\tAliases: [{}]\n".format(", ".join(self.aliases)) + \
               "\tSlots: [{}]".format(", ".join([slot.name for slot in self.slots]))

    def add_adj_to(self, other: Caseframe) -> None:
        self.adj_to.add(other)

    def add_adj_from(self, other: Caseframe) -> None:
        self.adj_from.add(other)

    def adjustable(self, other: Caseframe) -> bool:
        """ Returns true if this caseframe can adjust to the other. """
        return self.can_pos_adj(other) or \
               self.can_neg_adj(other) or \
               self.pseudo_adjustable(other)

    def can_pos_adj(self, other: Caseframe) -> bool:
        """ Returns true if self is a caseframe that is pos_adj to the caseframe
            other. Self caseframe is pos_adj to other caseframe if:
                1. self.type is the same, or a subtype of other.type
                2. Every slot in self.slots - other.slots is pos_adj reducible and min = 0
                3. Every slot in other.slots - self.slots is pos_adj expandable and min = 0 """
        if self.sem_type is other.sem_type or other.sem_type.subtype(self.sem_type):
            if all(slot.pos_adj is AdjRule.REDUCE and slot.min == 0 for slot in set(self.slots) - set(other.slots)) and \
               all(slot.pos_adj is AdjRule.EXPAND and slot.min == 0 for slot in set(other.slots) - set(self.slots)):
                return True
        return False

    def can_neg_adj(self, other: Caseframe) -> bool:
        """ Returns true if self is a caseframe that is neg_adj to the caseframe
            other. Self caseframe is neg_adj to other caseframe if:
                1. self is the same, or a subtype of other
                2. Every slot in self.slots - other.slots is neg_adj reducible and min = 0
                3. Every slot in other.slots - self.slots is neg_adj expandable and min = 0 """
        if self.sem_type is other.sem_type or other.sem_type.subtype(self.sem_type):
            if all(slot.neg_adj is AdjRule.REDUCE and slot.min == 0 for slot in set(self.slots) - set(other.slots)) and \
               all(slot.neg_adj is AdjRule.EXPAND and slot.min == 0 for slot in set(other.slots) - set(self.slots)):
                return True
        return False

    def pseudo_adjustable(self, other: Caseframe) -> bool:
        """ Special case for adjustments, based on fopl. """
        return self.name == "Nor" and other.name == "AndOr"

# =====================================
# --------------- FRAME ---------------
# =====================================

class Frame:
    def __init__(self, caseframe: Caseframe, filler_set=None) -> None:
        self.caseframe = caseframe
        self.filler_set = [] if filler_set is None else filler_set

        # Confirm correct number of fillers and that fillers correspond to the caseframe's slots
        self.verify_fillers()

    def verify_fillers(self) -> None:
        """ Check fillers correspond to slots
            Fillers are entered as a list of type Fillers:
                - Each Fillers instance corresponds to one slot
                - One slot might have multiple nodes """

        # Confirm proper number of fillers for all slots in caseframe before building slot
        if len(self.filler_set) != len(self.caseframe.slots):
            raise CaseframeError('ERROR: Wrong number of fillers. "' + self.caseframe.name + '" takes ' + \
                                 str(len(self.caseframe.slots)) + ' fillers.')

        for i in range(len(self.filler_set)):
            slot = self.caseframe.slots[i]
            fillers = self.filler_set[i]

            # Check if filler has a legal semantic type for the slot, and casts its type if so
            for node in fillers.nodes:
                sem_hierarchy = self.caseframe.sem_hierarchy
                sem_hierarchy.fill_slot(node, slot.sem_type)

            # Ensures number of fillers is within min/max of slots
            if len(fillers) < slot.min:
                raise CaseframeError('ERROR: Fewer than minimum required slots provided for "' + slot.name + '"')
            if slot.max is not None and len(fillers) > slot.max:
                raise CaseframeError('ERROR: Greater than maximum slots provided for "' + slot.name + '"')

    def get_filler_set(self, slot: Slot) -> Set[Slot]:
        """ Returns a set of all fillers that are used with given slot """
        slot_fillers = set()
        for i in range(len(self.caseframe.slots)):
            if self.caseframe.slots[i] is slot:
                # Adds all fillers at the end of cables designated by the slot's name
                slot_fillers.update(self.filler_set[i].nodes)
        return slot_fillers

    def __eq__(self, other: Caseframe) -> bool:
        return self.caseframe is other.caseframe and self.filler_set == other.filler_set

    def __str__(self) -> str:
        ret = self.caseframe.name
        for i in range(len(self.filler_set)):
            ret += self.filler_set[i].to_str(self.caseframe.slots[i].name)
        return ret

# =====================================
# -------------- FILLERS --------------
# =====================================

class Fillers:
    """ Form 'cables'/'cablesets' """

    def __init__(self, nodes=None) -> None:
        self.nodes = set() if nodes is None else set(nodes)

    def __len__(self) -> int:
        return len(self.nodes)

    def to_str(self, slot_name: str) -> str:
        """ We don't use __str__ for this because we need another parameter. """
        return "\n\t  " + slot_name + ":" + "".join("\n\t    " + str(node) for node in self.nodes)

    def __eq__(self, other: Fillers) -> bool:
        return self.nodes == other.nodes

# =====================================
# --------------- MIXIN ---------------
# =====================================

class CaseframeMixin:
    """ Provides functions related to caseframes to network """

    def __init__(self) -> None:
        if type(self) is CaseframeMixin:
            raise NotImplementedError("Mixins can't be instantiated.")

        self.caseframes = {} # Maps strings to Caseframe objects

    def find_caseframe(self, name: str) -> Caseframe:
        """ Locates a named caseframe in the network and returns the associated object. """
        for caseframe in self.caseframes.values():
            if caseframe.has_alias(name):
                return caseframe
        else:
            raise CaseframeError('ERROR: Caseframe "' + name + '" not defined.')

    def list_caseframes(self) -> None:
        """ Prints out all representations for all of the defined caseframes. """
        for caseframe in self.caseframes:
            print(self.caseframes[caseframe])

    def same_frame(self, aliases: List[str], caseframe_str: str):
        """ Add aliases to caseframe. """
        caseframe = self.find_caseframe(caseframe_str)
        for alias in aliases:

            # Ensures user cannot give two caseframes the same alias
            try:
                existing_caseframe = self.find_caseframe(alias)
            except CaseframeError:
                existing_caseframe = None
            if existing_caseframe is not None and existing_caseframe is not caseframe:
                raise CaseframeError('ERROR: A caseframe with alias "' + alias + '" already exists.')

            caseframe.add_alias(alias)

    def define_caseframe(self, name: str, sem_type_name: str, slot_names: List[str], docstring: str = "") -> None:
        """ Defines a new caseframe in the network """

        if not match(r'^[A-Za-z][A-Za-z0-9_]*$', name):
            raise CaseframeError("ERROR: The caseframe name '{}' is not allowed".format(name))

        # Checks provided slots names are valid
        frame_slots = []
        for slot_name in slot_names:
            if slot_name not in self.slots:
                raise CaseframeError("ERROR: The slot '{}' does not exist".format(slot_name))
            frame_slots.append(self.slots[slot_name])

        # Checks provided type is valid
        # If the type was invalid, get_type will raise an error.
        sem_type = self.sem_hierarchy.get_type(sem_type_name)

        # Builds new caseframe with given parameters
        new_caseframe = Caseframe(name, sem_type, self.sem_hierarchy, docstring, frame_slots)

        # Checks if identical to existing caseframe
        for caseframe in self.caseframes.values():
            if caseframe.has_alias(name):
                raise CaseframeError("ERROR: Caseframe name '{}' is already taken".format(name))

            if new_caseframe == caseframe:
                print("The existing caseframe \"{}\" is identical to the new caseframe you have defined".format(
                    caseframe.name, name))

                # Allows user to use new name as an alias, if an identical caseframe already exists
                while True:
                    response = input('Would you like to add an alias to "' + caseframe.name + '"? (y/N)')
                    if "YES".startswith(response.upper()):
                        caseframe.add_alias(name)
                        break
                    elif "NO".startswith(response.upper()):
                        break
                    else:
                        print("What?")

                # Allows user to use new docstring, if an identical caseframe already exists
                while True:
                    response = input('Would you like to override the docstring for "'+ caseframe.name + '"? (y/N)')
                    if "YES".startswith(response.upper()):
                        caseframe.docstring = docstring
                        break
                    elif "NO".startswith(response.upper()):
                        break
                    else:
                        print("Huh?")

                # Exit early if the caseframe already exists
                return

        # Add adjustments to other caseframes in network
        for case in self.caseframes.values():
            if new_caseframe.adjustable(case):
                new_caseframe.add_adj_to(case)
                case.add_adj_from(new_caseframe)
            if case.adjustable(new_caseframe):
                case.add_adj_to(new_caseframe)
                new_caseframe.add_adj_from(case)

        # If new/unique, adds to dictionary
        self.caseframes[new_caseframe.name] = new_caseframe
