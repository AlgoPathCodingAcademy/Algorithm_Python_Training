"""
Top-K Data Structure
---------------------------------------

Implement a container that keeps track of the k largest numbers inserted so far.

Operations
~~~~~~~~~~
* add(number)  – insert a value.
* topk()       – return the current k largest values in **descending** order.

The value of k is fixed when the object is created.  Each add should run in
O(log k) time, so a small heap of size ≤ k is the natural choice.
"""

import heapq


class TopK(object):
    def __init__(self, k):
        '''
        Create an empty TopK tracker.

        :param k: how many of the largest numbers to remember
        '''
        self.k = k
        self.heap = []
        


    def add(self, number):
        '''
        Insert *number* into the structure.

        Keep only the k largest elements seen so far.
        '''
        heapq.heappush(self.heap,number)
        
        itemsInHeap = len(self.heap)
        if itemsInHeap > self.k:
            heapq.heappop(self.heap)
            

    def topk(self):
        return sorted(self.heap,reverse=True)
        


# ---------------- demo ----------------
if __name__ == '__main__':
    k = 3
    tk = TopK(k)
    for x in [5, 1, 9, 2, 7, 9]:
        tk.add(x)
        print("after adding %d: top %d = %s" % (x, k, tk.topk()))
