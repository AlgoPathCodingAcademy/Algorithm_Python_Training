#Implement a stack.

class ListNode:
    def __init__(self,value,next):
        self.val = value
        self.next = None

class Stack:
    def __init__(self):
        self.dummy = ListNode(float("-inf"))
    
    def printList(self,head):
        current = head
        while True:
            if current != None:
                print(current.val)
                current = current.next
            else:
                break

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here

    """
    @return: nothing
    """
    def pop(self):
        # write your code here

    """
    @return: An integer
    """
    def top(self):
        # write your code here

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here

push(1)
pop()
push(2)
top()  #return 2
pop()
isEmpty() #return true
push(3)
isEmpty() #return false
