# TODO:Implement function "delete_node" using dummy node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, value):
    #TODO use dummy node to complete this function
    dummyNode = Node(float("-inf"))
    dummyNode.next = head
    currentNode = dummyNode
    while True:
        if currentNode != None:
            nextItem = currentNode.next
            if nextItem != None:
                 if nextItem.data == value:
                     newNextItem = nextItem.next
                     currentNode.next = newNextItem
                     break
        else:
            break
        
        currentNode = currentNode.next
    
    return dummyNode.next


# Helper function to print the linked list
def print_list(node):
    while node is not None:
        print(node.data, end=" -> ")
        node = node.next
    print("null")

# Create and link nodes: 1 -> 2 -> 3 -> 4 -> 5
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original list:")
print_list(node1)

# Test deleting a node by value
head = delete_node(node1, 3)
print("List after deleting value 3:")
print_list(head)  # Expected output: 1 -> 2 -> 4 -> 5 -> null

# Test deleting the head node
head = delete_node(head, 1)
print("List after deleting value 1 (head node):")
print_list(head)  # Expected output: 2 -> 4 -> 5 -> null
