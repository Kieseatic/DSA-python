class SelfAdjustingList:
    class Node:
        def __init__(self, dat, nx=None, pr=None):
            self.data = dat
            self.next = nx
            self.prev = pr

    def __init__(self, id_list):
        self.front = None
        self.back = None

        for item in id_list:
            new_node = SelfAdjustingList.Node(item, None, None)
            if self.back:
                new_node.prev = self.back
            else:
                self.front = new_node
            self.back = new_node
    
    def search(self, v):
        current_node = self.front

        while current_node:
            if current_node.data == v:

                if current_node != self.front:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev

                if current_node.next is None:
                    self.back = current_node.prev

                current_node.next = self.front
                current_node.prev = None
                self.front.prev = current_node
                self.front = current_node

                return True
            current_node = current_node.next
        return False
                    

    def print_list(self):
        result = []
        current_node = self.front
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result

# Example usage
my_list = SelfAdjustingList([1, 2, 3, 4, 5])

# Print the original list
original_list = []
current_node = my_list.front
while current_node:
    original_list.append(current_node.data)
    current_node = current_node.next
print("Original list:", original_list)

# Perform a search for the value 3
result = my_list.search(3)

# Print the list after search
after_search_list = []
current_node = my_list.front
while current_node:
    after_search_list.append(current_node.data)
    current_node = current_node.next
print("After searching:", after_search_list)

'''
def search(self, v):
        current_node = self.front

        while current_node:
            if current_node.data == v:
                # If the found node is not already the front, adjust the list
                if current_node != self.front:
                    current_node.prev.next = current_node.next

                    if current_node.next:
                        current_node.next.prev = current_node.prev
                    else:
                        self.back = current_node.prev

                    current_node.next = self.front
                    current_node.prev = None
                    self.front.prev = current_node
                    self.front = current_node

                return True
            current_node = current_node.next

        return False

'''
# with sentinel 
class SelfAdjustingList:
    class Node:
        def __init__(self, dat, nx=None, pr=None):
            self.data = dat
            self.next = nx
            self.prev = pr

    def __init__(self, id_list):
        # Create head and tail sentinel nodes
        self.front = SelfAdjustingList.Node(None)
        self.back = SelfAdjustingList.Node(None)

        # Connect head and tail
        self.front.next = self.back
        self.back.prev = self.front

        # Populate the list with initial data
        for item in id_list:
            new_node = SelfAdjustingList.Node(item, self.back, self.back.prev)
            self.back.prev.next = new_node
            self.back.prev = new_node

    def search(self, v):
        current_node = self.front.next  # Skip the head sentinel

        while current_node != self.back:
            if current_node.data == v:
                # Move the found node to the front
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

                current_node.next = self.front.next
                current_node.prev = None
                self.front.next.prev = current_node
                self.front.next = current_node

                return True
            current_node = current_node.next

        return False

    