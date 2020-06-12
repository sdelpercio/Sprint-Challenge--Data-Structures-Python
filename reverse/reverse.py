class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # check for empty list, single item list then escape
        if self.head == None:
            return
        if node == self.head and not node.next_node:
            return
        
        # if current node is none then escape
        if node == None:
            return
        
        # if last item in list, set new head, then escape
        if node.next_node == None:
            self.head = node
            return
            
        # else recurse
        self.reverse_list(node.next_node, node)
        
        # on second pass
        # point next node backwards, remove current next to make one way LL
        node.next_node.next_node = node
        node.next_node = None
        return
        
            
        
            
        
        