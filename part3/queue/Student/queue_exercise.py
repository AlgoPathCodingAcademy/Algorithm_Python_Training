import collections

#TODO
def record_hit(hits, size, score):

#TODO
def get_hits(hits):

size = 3
hits = collections.deque()

record_hit(hits, size, 1)
record_hit(hits, size, 4)
record_hit(hits, size, 6)
get_hits(hits)  # Output: 1,4,6

record_hit(hits, size, 5)
get_hits(hits)  # Output: 4,6,5

