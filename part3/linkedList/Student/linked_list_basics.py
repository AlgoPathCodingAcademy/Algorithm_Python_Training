class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating the linked list 1 -> 3 -> 5 -> null
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)

# Linking the nodes
node1.next = node2
node2.next = node3

#TODO add another node which has value 10 to the end of th list
# 1 -> 3 -> 5 -> 10 -> null


#TODO, iterate the link list so that we print each value of the node
#No len() function
    

#TODO, print the value of ith node (Assume it is less then the length of the link list)
    
    
#TODO, Get the middle of the link list
#print the value of the middle node of the linked list.
#If there are two middle nodes, return the second middle node.
# Example 1. 1->2->3->4->5], output: 3
# Example 2. 1->2->3->4->5->6, output: 4
# In our case, it should ouput 5
# This solution uses two passes.
# One pass to calculate the length
# Another pass to return the node


#TODO Insert a Node at the Beginning
#insert a new node with a given value at the beginning of a linked list.
#add a new node whose value is 9
#Output should be 9 -> 1 -> 3 -> 5 -> 10 -> null


#TODO Given a list [2,3,4,5], create a link list:
#2->3->4->5->None
    
#TODO print a linklist


#TODO Insert a node into the end of the list

print("============")

#TODO implement function insert_at_position
#2->3->4->5->6
def insert_at_position(head, value, position):
    pass
        
    
print("============")
#TODO implement function delete_at_position
#2->7->3->4->5->6
def delete_at_position(head, position):
# Implement the function
    pass

print("===Delete===")
#2->7->3->4->5
def delete_node_by_value(head, value):
    pass

print("===Delete Entire Linked List===")

#TODO Delete entire linked list
def delete_linked_list(head):
    pass

print("======Use Dummy Node=====")

#Dummy node
def delete_node_by_value(head, value):
    # Create a dummy node that points to the head of the list
    pass
