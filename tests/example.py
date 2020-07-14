from psneps import *
net = Network()
net.define_slot("agent", "Entity")
net.define_slot("has", "Thing")
net.define_slot("happy_thing", "Thing")

net.define_context("test")
net.set_current_context("test")

net.define_caseframe("Has", "Propositional", ["agent", "has"])
net.define_caseframe("Happy", "Propositional", ["happy_thing"])

# net.assert_wft("and(every(x, andor{1, 3}(x, Human)), every(z, andor{1, 2}(z, Human)), some(y(x, z), Isa(y, Dog)), some(q(z, x, x), Isa(q, Dog)))")
net.assert_wft("andor{0, 3}(a, a, b, b, c, d)")
net.assert_wft("nand(a, b, c, d)")

# net.assert_wft("2=>([a, b, c, d], [not(e), f, g])")
# net.assert_wft("and(a, b)")

snips = Inference(net)
snips.toggle_debug()
snips.ask("e")

print(net.find_slot("equiv"))

net.export_graph()
# net.print_graph()
