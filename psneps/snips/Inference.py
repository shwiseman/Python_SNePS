from ..Network import *

"""
This is the main file of the SNIPS package. In here, we define the Inference class.
Authors: Ben Kallus, John Madigan, and Seamus Wiseman
"""

class Inference:
    def __init__(self, net: Network):
        self.net = net

    def ask(self, wft_str: str):
        self.ask_if(wft_str)
        self.ask_if_not(wft_str)

    def ask_if(self, wft_str: str):
        wft = wft_parser(wft_str, self.net)
        self.net.sem_hierarchy.respecify(wft.name, wft.sem_type, self.net.sem_hierarchy.get_type("Proposition"))
        if self.net.current_context.is_asserted(wft):
            print("{}! [{}] is asserted".format(wft.name, wft_str))
            return True
        return False

    def ask_if_not(self, wft_str: str):
        wft = wft_parser('not({})'.format(wft_str), self.net)
        self.net.sem_hierarchy.respecify(wft.name, wft.sem_type, self.net.sem_hierarchy.get_type("Proposition"))
        if self.net.current_context.is_asserted(wft):
            print("{}! [not({})] is asserted".format(wft.name, wft_str))
            return True
        return False

    # def _path_based_inference(self, wft: str):
