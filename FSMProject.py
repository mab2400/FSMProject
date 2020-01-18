import FSMModule, NodeModule
# Construct a new FSM, given the starting node, a list of accepting
# nodes, a list of intermediary nodes, and the input string.

fsm = FSM(start, accepting, intermediary, inputStr)

'''
Transition functions will be set in my test code
Like this:
add_transition(node1, node2, “c”)
add_transition(node2, node3, “d”)

The for loop below goes through the nodes, beginning with the
given start node. Within the loop, I update the currentNode
based on the transition function of that node. If at any point
we arrive at one of the accepting nodes, then I break out of the
loop because we are finished. If by the end of the inputStr
we have not reached an accepting node, I print "Not accepted."

'''

currentNode = fsm.start

for char in inputStr:

    currentNode = fsm.transition(currentNode, char)

    if currentNode in fsm.accepting:
        print("Accepted!")
        break

if currentNode not in fsm.accepting:
    print("Not accepted.")
