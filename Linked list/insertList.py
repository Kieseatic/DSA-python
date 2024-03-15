class LinkedList: 
    def __init__ (self, value , nextNode= None):
        self.value = value
        self.nextNode = nextNode   #pointer to the next node of the list 

class listContainer:
    def __init__(self,head= None):
        self.head = head   #the first element of the list 

    def insert(self,value):
        node = LinkedList(value)  #creating a new list 

        if self.head is None:   #agr list empty hai toh first element apna naya node ban jayega 
            self.head = node

        else: 
            currentNode = self.head      #List ka pehla element is currentNode taaki we can traverse thru the list
            while True:
                if currentNode.nextNode is None:
                    currentNode.nextNode = node
                    break
                currentNode = currentNode.nextNode


    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value,"->",end = " ")
            currentNode = currentNode.nextNode

        print("End of list")

listInsert = listContainer()

listInsert.insert(1)
listInsert.insert(2)
listInsert.insert(3)

listInsert.printList()



