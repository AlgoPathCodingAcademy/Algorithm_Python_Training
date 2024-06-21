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
        newNode = ListNode(x)
    
        if self.dummy.next != None:
            nextNode = self.dummy.next
            newNode.next = nextNode

        self.dummy.next = newNode
        

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if self.dummy.next != None:
            self.dummy.next = self.dummy.next.next

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.dummy.next.val

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        if self.dummy.next == None:
            return True
        else:
            return False

push(1)
pop()
push(2)
top()  # return 2
pop()
isEmpty() # return true
push(3)
isEmpty() # return false
