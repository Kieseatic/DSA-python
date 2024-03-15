class SelfAdjustingList:
    class Node:
        def _init__(self,value,next= None,prev =None):
            self.value=value
            self.next=next
            self.prev=prev

    def __init__(self,id_list):
        self.head= None
        self.tail = None

        for item in id_list:
            new_node = SelfAdjustingList.Node(item, None, None)
            if self.back:
                new_node.prev = self.back
            else:
                self.front = new_node
            self.back = new_node
    
    def search(self,v):
        currentNode = self.head

        while currentNode:
            if currentNode.value == v:
                if currentNode != self.head:
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev= currentNode.prev

                if currentNode.next == None:
                    self.tail = currentNode.prev

                currentNode.next = self.front
                currentNode.prev = None
                self.front.prev = currentNode
                self.front = currentNode

            return True
        currentNode = currentNode.next
        return False
                    

