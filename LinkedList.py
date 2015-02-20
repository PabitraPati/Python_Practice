
class Node(object):
    '''
    Creates a node with the data field and pointer for next node.
    '''
    def __init__(self, data=None, nextnode=None):
        self.data = data
        self.nextnode = nextnode    

class LinkedList(object):
    '''
    LinkedList class for performing various operations on linkded list.
    '''
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addnode(self, data):
        '''
        Adds a node with the given data to the end of the linked list.
        '''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node        # add first node to the linked list
        if self.tail is not None:
            self.tail.nextnode = new_node    
        self.tail = new_node
        
        # print the new linked list        
        self.printlist()        
    
    def insert(self, data, index):
        '''
        Insert a node at the given index of the linked list.
        '''
        new_node = Node(data)

        if index == 1:
            # Insert at the beginning
            new_node.nextnode = self.head
            self.head = new_node
        else:
            node = self.head
            prev = None
            i = 1
            while(i < index):
                prev = node
                node = node.nextnode
                i+=1
            new_node.nextnode = prev.nextnode     # new node's next points to previous node's next
            prev.nextnode = new_node              # previous node's next point to the new node being added
        
        # print the new linked list
        self.printlist()
        
    def remove(self, index):
        '''
        Removes a perticular node with given index from the linked list.
        '''
        prev = None
        node = self.head
        i = 1
        while(node != None ) and (i < index):
            prev = node
            node =node.nextnode
            i+=1
        if prev is None:
            self.head = node.nextnode
        else:
            prev.nextnode = node.nextnode
        
        # print the new linked list        
        self.printlist()
    
    def printlist(self):
        node = self.head
        while node != None:
            print  " --> ",
            print node.data,
            node = node.nextnode
        print "\n"
        
        
link = LinkedList()
link.addnode("A")
link.addnode("B")
link.addnode("C")
link.addnode("D")
link.insert("M", 3)
link.remove(3)
link.remove(4)
