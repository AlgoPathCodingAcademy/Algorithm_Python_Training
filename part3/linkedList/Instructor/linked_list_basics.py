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
def printLinkedList(head):
    currentNode = head
    while True:
        if currentNode != None:
            print(currentNode.data)
        else:
            break
        
        currentNode = currentNode.next

printLinkedList(node1)


def lenLinkedList(head):
    counter = 0
    currentNode = head
    while True:
        if currentNode != None:
            counter = counter + 1
        else:
            break
        
        currentNode = currentNode.next
    return counter
    
length = lenLinkedList(node1)
print("Linked List length ",length)

print("===========")



def getItemIndexLinkedList(head,index):
    counter = 0
    currentNode = head
    while True:
        if currentNode != None:
            if counter == index:
                return currentNode
            counter = counter + 1
        else:
            break
        
        currentNode = currentNode.next
    return None
    

def getMiddleLinkedList(head):
    
    length = lenLinkedList(node1)
    
    index = 0
    
    if length % 2 == 0:
        index = length // 2
    else:
        index = length // 2
        
    middle_head = getItemIndexLinkedList(head,index)
    
    return middle_head
    

printLinkedList(getMiddleLinkedList(node1))

print("===========")
#TODO Insert a Node at the Beginning
#insert a new node with a given value at the beginning of a linked list.
#add a new node whose value is 9
#Output should be 9 -> 1 -> 3 -> 5 -> 10 -> null

newNode = Node(9)

newNode.next = node1

printLinkedList(newNode)


#TODO Insert a node into the end of the list

def insertLastNode(head,data):
    
    currentNode = head
    
    #Handle corner case - Empty List
    if currentNode == None:
        head = Node(data)
        return head
    
    while True:
        if currentNode != None:
            if currentNode.next == None:
                currentNode.next = Node(data)
                break
        else:
            break
        
        currentNode = currentNode.next
    return head
    

printLinkedList(insertLastNode(node1,12))


def insert_at_position(head, value, position):
    counter = 0
    currentNode = head
    
    #Handle corner case - The top of the linked list or empty linkedlist 
    if position == 0 or head == None:
        newNode = Node(value)
        newNode.next = head
        return newNode
    
    while True:
        if currentNode != None:
            if counter == position - 1:
                newNode = Node(value)
                newNextNode = currentNode.next
                currentNode.next = newNode
                newNode.next = newNextNode
                break
                
                
            counter = counter + 1
        else:
            break
        
        currentNode = currentNode.next
    return head
    
    
printLinkedList(insert_at_position(None, 20, 0))


def delete_node_by_value(head, value):
    # Implement the function
    
    #handle special case
    currentNode = head
    while True:
        if currentNode != None:
            if currentNode.next != None:
                if currentNode.next.data == value:
                    currentNode.next = currentNode.next.next
                    return head
        else:
            break
        
        currentNode = currentNode.next
        
    return head
    
printLinkedList(delete_node_by_value(node1,1))


def delete_at_position(head, position):
    counter = 0
    currentNode = head
    
    #Handle corner case - The top of the linked list or empty linkedlist 
    if position == 0:
        head = head.next
        return head
    
    while True:
        if currentNode != None:
            if counter == position - 1:
                nextNode = currentNode.next
                if nextNode != None:
                    newNextNode = nextNode.next
                    currentNode.next = newNextNode
                    break
                else:
                    currentNode.next = None
                
                
            counter = counter + 1
        else:
            break
        
        currentNode = currentNode.next
    return head
    
printLinkedList(node1)


printLinkedList(delete_at_position(node1, 0))


def delete_linked_list(head):
    dummyNode = Node(float("-inf"))
    dummyNode.next = head
    
    currentNode = dummyNode
    while True:
        if currentNode != None:
            nextNode = currentNode.next
            if nextNode != None:
                newNextNode = nextNode.next
                currentNode.next = newNextNode
            else:
                newNextNode = None
                break
            
        else:
            break
        
    return dummyNode.next
    

printLinkedList(delete_linked_list(node1))


list_input = [2,3,4,5]
dummyNode = Node(float("-inf"))
head = dummyNode
for index in range(len(list_input)):
    newNode = Node(list_input[index])
    dummyNode.next = newNode
    dummyNode = newNode
    
printLinkedList(head.next)
