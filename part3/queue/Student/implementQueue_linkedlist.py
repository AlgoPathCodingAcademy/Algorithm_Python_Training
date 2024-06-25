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

    def printList(self):
        current = self.dummy.next
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

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here

#Test Case 1

myQueue = MyQueue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue.dequeue())  #return 1
myQueue.enqueue(4)
print(myQueue.dequeue())  #return 2

#Test Case 2

myQueue = MyQueue()
myQueue.enqueue(10)

print(myQueue.dequeue()) #return 10
print(myQueue.dequeue()) #return -1