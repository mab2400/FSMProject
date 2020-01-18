 # construct a new FSM, given the starting node, a list of accepting
 # nodes, and a list of intermediary nodes.

 fsm = FSM(start, accepting, intermediary)

 # set the transition functions
     # based on input --> HOW EXACTLY AM I GOING TO DO THIS?
     # using the dict, I will be able to access the node object from the user's inputted        strings
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
