class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while True:
            if fast == None or fast.next == None:
                return slow
            else:
                fast = fast.next.next
                slow = slow.next
    ######################################



my_linked_list = None
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)

while True:
    val = input("Enter a number: ")
    if val == "stop":
        break
    if not val.isnumeric():
        print("Error, not a number")
        continue
    if my_linked_list == None:
        my_linked_list = LinkedList(val)
        continue
    my_linked_list.append(val)

print( my_linked_list.find_middle_node().value )

