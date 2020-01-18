 # FSM class
 class FSM:

     def __init__(self, start, accepting, intermediary, inputStr):
         self.start = start
         self.accepting = accepting
         self.intermediary = intermediary
         self.inputStr = inputStr
         self.transitionDict = {}

         '''
         transitionDict will look something like this
         {currentNode : [(char, nextNode), (char, nextNode)],
         currentNode : [(char, nextNode), (char, nextNode), (char, nextNode)]}
         '''

    def add_transition(self, currentNode, char, nextNode):
        # if current state is at node 1  and
        # the next character read is char
        # then move to node 2.

        # If currentNode already has a value in the dict,
        # we need to append to the existing list.

        valueList = transitionDict.get(currentNode)
        valueList.append((char, nextNode))
        transitionDict[currentNode] = valueList

    def transition(self, currentNode, char):
        # this will return the next node,
        # based on the currentNode and the input char.

        # First, I find the current node in the set of
        # keys. Next, I iterate through the list of tuples
        # which is the corresponding value of that key,
        # searching for char. Once I've found char, I
        # return the corresponding nextNode.

        for node in transitionDict.keys():
            if node is currentNode:
                # double-check to make sure this equality is ok
                for c,nextN in transitionDict[currentNode]:
                    if c == char:
                        return nextN
