class Node:
    def __init__(self,value,nextNode = None, prevNode=None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode= prevNode

class DoublyList: 
    def __init__(self):  #initializing first and last element of the list
        self.head = None
        self.tail= None  

    def append(self,value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            #setting the next node of the new node as the head 
            newNode.nextNode = self.head
            #adding new node next to the head of current list
            self.head.prevNode = newNode
            # setting the new node added as the new tail
            self.head =newNode

    def popFront(self):
        if self.head is not None:
            rm = self.head
            self.head= self.head.nextNode
            del rm

    def printForward(self):
        currentNode = self.head   #keep current node as the head of the list to print from the head 
        while currentNode:
            print(currentNode.value, end ="<->")
            currentNode = currentNode.nextNode
        print('None)')

    def printBackward(self):
        currentNode = self.tail
        while currentNode:
            print(currentNode.value,end = '<->')
            currentNode = currentNode.prevNode
        print("None")


    # Example usage:
doubly_linked_list = DoublyList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.popFront()
# Print the list forward
print("Forward:")
doubly_linked_list.printForward()

# Print the list backward
print("\nBackward:")
doubly_linked_list.printBackward()

# with sentinel 

