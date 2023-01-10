class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(node):
    print(node.data)
    if node.next is not None:
        print_linked_list(node.next)



"""
his function takes a node as input and prints its data. If the node has a next pointer 
(i.e., it's not the last node in the list), the function calls itself with the next node
 as input, and so on. This creates a chain of function calls, each one printing the data
  of the next node in the list, until the last node is reached and the recursion stops.
"""
