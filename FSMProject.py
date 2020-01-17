#_______________________________________

# FSM class
class FSM:

# Nodes
    # User inputs
    # 1) Starting node
    # 2) Accepting node(s)
    # 3) Intermediary node(s)

# Node start =
# Node[] accepting =
# Node[] intermediary =

# inputStr variable: a string of characters
    # in the main method we'll get each char from the input one at a time

    def __init__(self):
        self.start = null
        self.accepting = []
        self.intermediary = []
        self.inputStr = ''
        self.nodeDict = {}

# Dict to connect inputted strings of node names to the actual node objects
# I populate this dict in the main method when I take in input.
# user inputs 'A', 'B', 'C' which my program should transform into node objects A, B, C

#_______________________________________

# Node class

# name --> based on the inputted node names from the user in main method
# transition() function --> how would the user set the transition function?

class Node:

    def __init__(self, inputName):
        self.name = inputName

    def transition(self):
        # TRANSITION FUNCTION
        # return a Node
#_______________________________________

# construct a new FSM.

fsm = FSM()

# construct inputted nodes:
    # set start, accepting, intermediary of the FSM object
    # this should be done at the same time as you construct inputted nodes.
    # like this:
    # input start node: __
    # [constructs node, sets start variable in FSM class as that node ]
    # input accepting node(s): __
    # [constructs node(s) using a loop, creates a list and sets variable in FSM class]
    # input intermediary node(s): __
    # [constructs node(s) using a loop, creates a list and sets variable in FSM class]

startStr = input("Start node: ")
start = Node(startStr)
# add to the FSM
fsm.start = start
# add to the FSM dict
fsm.nodeDict[startStr] = start

acceptingStr = input("Accepting node(s): ")
for nodeStr in acceptingStr.split():
    node = Node(nodeStr)
    # add to the FSM
    fsm.accepting.append(node)
    # add to the FSM dict
    fsm.nodeDict[nodeStr] = node

intermediaryStr = input("Intermediary node(s): ")
for nodeStr in intermediaryStr.split():
    node = Node(nodeStr)
    # add to the FSM
    fsm.intermediary.append(node)
    # add to the FSM dict
    fsm.nodeDict[nodeStr] = node

# set the transition functions
    # based on input --> HOW EXACTLY AM I GOING TO DO THIS?
    # using the dict, I will be able to access the node object from the user's inputted strings
# while loop iterates through the nodes starting with the given start node
'''
node = start
while(input is still being read):
    read next char of input
    put input into node's transition(), returns the next node
    node = result of transition()

if(at accepting node):
    accepted!
else:
    not accepted!
'''
