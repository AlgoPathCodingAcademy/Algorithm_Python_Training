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
        """
        Create an empty TopK tracker.

        :param k: how many of the largest numbers to remember
        """
        self.k = k
        self._min_heap = []            # min-heap of at most k elements

    def add(self, number):
        """
        Insert *number* into the structure.

        """

    def topk(self):
        """
        Return the k largest numbers in descending order.

        :return: list of up to k integers, largest first
        """
        


# ---------------- demo ----------------
if __name__ == '__main__':
    k = 3
    tk = TopK(k)
    for x in [5, 1, 9, 2, 7, 9]:
        tk.add(x)
        print("after adding %d: top %d = %s" % (x, k, tk.topk()))

