from psneps import *
net = Network.Network()
net.define_slot("agent", "Entity")
net.define_slot("has", "Entity")
net.define_slot("happy", "Entity")
net.define_caseframe("Has", "Propositional", ["agent", "has"])
net.define_caseframe("Happy", "Propositional", ["happy"])
net.assert_wft("if(Has(Dog, Bone), Happy(Dog))")
net.print_graph()
