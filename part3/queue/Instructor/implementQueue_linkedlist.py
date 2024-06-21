#Implement a Queue by singly linked list. Support the following basic methods:

#enqueue(item). Put a new item in the queue.
#dequeue(). Move the first item out of the queue, return it. If the queue is empty, returned. -1.、

class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.dummy = ListNode(float("-inf"))
        self.rear = self.dummy 

    def printList(self,head):
        current = head
        while True:
            if current != None:
                print(current.val)
                current = current.next
            else:
                break

    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        currentNode = self.rear
        currentNode.next = ListNode(item)

        self.rear = currentNode.next

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        nextNode = self.dummy.next
        value = -1
        if nextNode != None:
            value = nextNode.val
            self.dummy.next = nextNode.next

            if nextNode == self.rear:
                self.rear = self.dummy
        return value

#Test Case 1
enqueue(1)
enqueue(2)
enqueue(3)
dequeue()  #return 1
enqueue(4)
dequeue()  #return 2


#Test Case 2
enqueue(10)
dequeue() #return 10
dequeue() #return -1
