class LinkedList:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

# Creating linked list nodes
node1 = LinkedList("2")
node2 = LinkedList("3")
node3 = LinkedList("4")

# Connecting nodes
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = None

# Traversing the linked list
currentNode = node1
while currentNode is not None:
    print(currentNode.value, "->", end=" ")
    currentNode = currentNode.nextNode

# Print "End of list" when the traversal is complete
print("End of list")
