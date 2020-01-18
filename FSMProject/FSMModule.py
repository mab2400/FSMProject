  # FSM class
  class FSM:

      def __init__(self):
          self.start = null
          self.accepting = []
          self.intermediary = []
          self.inputStr = ''

     def addTransition(self, n1, n2, 'c'):
         # if current state is at node 1  and
         # the next character read is 'c'
         # then move to node 2
