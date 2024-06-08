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

node4 = Node(10)
node3.next = node4

#TODO, iterate the link list so that we print each value of the node
#No len() function
currentNode = node1
while True:
    if currentNode != None:
        # logic
        print(currentNode.data)
    else:
        break
    
    currentNode = currentNode.next
    

#TODO, print the value of ith node (Assume it is less then the length of the link list)
currentNode = node1
index = 0
counter = 0
while True:
    if currentNode != None:
        # logic
        print(currentNode.data)
        if counter == index:
            print(index, "th Node ", currentNode.data)
        
        counter = counter + 1
    else:
        break
    
    currentNode = currentNode.next
    
    
#TODO, Get the middle of the link list
#print the value of the middle node of the linked list.
#If there are two middle nodes, return the second middle node.
# Example 1. 1->2->3->4->5], output: 3
# Example 2. 1->2->3->4->5->6, output: 4
# In our case, it should ouput 5
# This solution uses two passes.
# One pass to calculate the length
# Another pass to return the node
currentNode = node1
counter = 0
while True:
    if currentNode != None:
        counter = counter + 1
        #logic
    else:
        break

    currentNode = currentNode.next

if (counter-1) % 2 == 0:
    index = (counter-1) // 2
else:
    index = (counter-1) // 2 + 1

currentNode = node1
counter = 0

while True:
    if currentNode != None:
        if counter >= index:
            print(currentNode.data)
            break
            #return currentNode
        counter = counter + 1
        #logic
    else:
        break

    currentNode = currentNode.next
    
#TODO Insert a Node at the Beginning
#insert a new node with a given value at the beginning of a linked list.
#add a new node whose value is 9
#Output should be 9 -> 1 -> 3 -> 5 -> 10 -> null
targetNumber = 9
newNode = Node(targetNumber)
newNode.next = node1
#The head of the node is still node1
node1 = newNode


    
#TODO Given a list [2,3,4,5], create a link list:
#2->3->4->5->None
nums = [2,3,4,5]

currentNode = Node(nums[0])
head = currentNode
for index in range(1,len(nums)):
    currentNode.next = Node(nums[index])

    currentNode = currentNode.next
    
#Show the linklist
currentNode = head
output = ""
while True:
    if currentNode != None:
        output = output + str(currentNode.data) + "->"
        currentNode = currentNode.next
    else:
        break

print(output)

def printList(head):
    currentNode = head
    while True:
        if currentNode != None:
            print(currentNode.data)
        else:
            break
        
        currentNode = currentNode.next


#TODO Insert a node into the end of the list
newNode = Node(6)
currentNode = head
if currentNode == None:
    # new head
    head = currentNode

lastNode = None
while True:
    #print("15.Show...")
    if currentNode != None:
        # Logic
        if currentNode.next == None:
           currentNode.next = newNode
           break

        currentNode = currentNode.next
    else:
        break

#lastNode.next = newNode
#print("last node", lastNode.data)
printList(head)

print("============")

#TODO implement function insert_at_position
#2->3->4->5->6
def insert_at_position(head, value, position):
    # Implement the function
    newNode = Node(value)
    
    if position == 0:
        newNode.next = head
        return newNode
        
    currentNode = head
    counter = 0
    while True:
        if currentNode != None:
            if position -1 == counter:
                # Direct insert element
                # Or could return the node and then do the insertion.
                nextItem = currentNode.next
                currentNode.next = newNode
                newNode.next = nextItem
                break
            
            counter = counter + 1
            currentNode = currentNode.next
        else:
            break
        
insert_at_position(head,7,1)
printList(head)
    
    
print("============")
#TODO implement function delete_at_position
#2->7->3->4->5->6
def delete_at_position(head, position):
    # Implement the function
 
    if position == 0:
        newHead = head.next
        return newHead
        
    currentNode = head
    counter = 0
    while True:
        if currentNode != None:
            if position -1 == counter:
                # Direct delete element
                # Or could return the node and then do the insertion.
                if currentNode.next != None:
                    currentNode.next = currentNode.next.next    
                else:
                    # delete the end node
                    currentNode.next = None
                break
            
            counter = counter + 1
            currentNode = currentNode.next
        else:
            break
        
    return head
        
head = delete_at_position(head,5)
printList(head)

print("===Delete===")
#2->7->3->4->5
def delete_node_by_value(head, value):
    currentNode = head
    
    if currentNode != None:
        if currentNode.data == value:
            #delete node
            head = currentNode.next
            return head

    while True:
        if currentNode != None:
            nextItem = currentNode.next
            
            if nextItem != None:
                if value == nextItem.data:
                    #delete
                    currentNode.next = nextItem.next
                    break
        else:
            break
        
        currentNode = currentNode.next
        
    return head
        
head = delete_node_by_value(head,3)
printList(head)

print("===Delete Entire Linked List===")

#TODO Delete entire linked list
def delete_linked_list(head):
    currentNode = head
    #print(currentNode.data)
    while True:
        if currentNode != None:
            nextItem = currentNode.next
            
            if nextItem != None:
                print("Deleting me ", nextItem.data)
                currentNode.next = nextItem.next
            else:
                break
        else:
            break
        
        #currentNode = currentNode.next
   
    head = None
    return head
    

head = delete_linked_list(head)
printList(head)

print("======Use Dummy Node=====")

#Dummy node
def delete_node_by_value(head, value):
    # Create a dummy node that points to the head of the list
    dummy = Node(float("-inf"))
    dummy.next = head
    currentNode = dummy
    while True:
        if currentNode != None:
            #logic
            nextItem = currentNode.next
            if nextItem != None:
                if nextItem.data == value:
                    currentNode.next = nextItem.next
                    break
        else:
            break

        currentNode = currentNode.next

    return dummy.next


head = delete_node_by_value(head, 2)
printList(head)
