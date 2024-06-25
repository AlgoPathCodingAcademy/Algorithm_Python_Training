class ListNode:
    def __init__(self,value):
        self.val = value
        self.next = None

class Stack:
    def __init__(self):
        self.dummy = ListNode(float("-inf"),)
    
    def printList(self):
        current = self.dummy.next
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
        
        if self.dummy.next == None:
            self.dummy.next = ListNode(x)
        else:
            newNode = ListNode(x)
            nextNode = self.dummy.next
            newNode.next = nextNode
            self.dummy.next = newNode
        

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if self.dummy.next  == None:
            return
        
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
        if self.dummy.next == None:
            return True
        else:
            return False
        # write your code here

myStack = Stack()
myStack.push(1)
myStack.pop()
myStack.push(2)
print(myStack.top())  #return 2
myStack.pop()
print(myStack.isEmpty()) #return true
myStack.push(3)
print(myStack.isEmpty()) #return false