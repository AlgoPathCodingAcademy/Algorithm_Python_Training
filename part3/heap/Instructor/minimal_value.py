import heapq
class dataCollection:
    def __init__(self):
        self.hash_ = {}
        self.heap_ = []

        
    def delete(self,x):
        self.hash_[x] -= 1
        if self.hash_[x] == 0:
            del self.hash_[x]
        
    def insert(self,x):
        if x not in self.hash_:
            self.hash_[x] = 1
        else:
            self.hash_[x] += 1
            
        heapq.heappush(self.heap_,x)

    def queryMin(self):
        
        while True:
            # check top of the heap
            if len(self.heap_) == 0:
                return None
            
            item = self.heap_[0]
            
            # Because item are only deleted in delete function and heaqp is not 
            # aware of this
            if item not in self.hash_:
                # deleted in the hash_ table already
                heapq.heappop(self.heap_)
            else:
                return item
                
                

            
# ------------------------------------------------------------
# corner-case tests focusing on many copies of the same number
# ------------------------------------------------------------

# This version expects `queryMin()` to return `None` when the data
# structure is empty, instead of raising an IndexError.
# ------------------------------------------------------------

def fresh():
    return dataCollection()          # assumes your class is already imported


# 0. sanity: empty → insert duplicate min → pop all duplicates → empty again
ds = fresh()
ds.insert(4); ds.insert(4); ds.insert(4)
assert ds.queryMin() == 4
ds.delete(4); ds.delete(4); ds.delete(4)
assert ds.queryMin() is None, "should be empty after deleting all copies"

# 1.   100 identical values
ds = fresh()
for _ in range(100):
    ds.insert(42)
assert ds.queryMin() == 42        # min must be 42 while any copy remains
for _ in range(99):
    ds.delete(42)
assert ds.queryMin() == 42        # still one live copy
ds.delete(42)                     # last copy removed
assert ds.queryMin() is None, "structure should be empty"

# 2. duplicates of two different numbers, min copies deleted first
ds = fresh()
for _ in range(5):
    ds.insert(1)                  # smaller key (min)
for _ in range(7):
    ds.insert(3)
assert ds.queryMin() == 1
for _ in range(4):                # delete 4 of the 5 copies of 1
    ds.delete(1)
assert ds.queryMin() == 1         # still one live min
ds.delete(1)                      # delete last copy of min
assert ds.queryMin() == 3         # 3 becomes new minimum

# 3. min has many copies, but larger key also has many copies
ds = fresh()
for _ in range(10):
    ds.insert(2)
for _ in range(10):
    ds.insert(5)
assert ds.queryMin() == 2
# delete five copies of 2 interleaved with deletions of 5 (not min)
for _ in range(5):
    ds.delete(2)
    ds.delete(5)
assert ds.queryMin() == 2         # still min because 5 copies of 2 remain

# 4. stress: insert N copies of ascending keys, then delete in reverse
N = 50
ds = fresh()
for k in range(1, N + 1):
    for _ in range(N):            # N copies of each key k
        ds.insert(k)
assert ds.queryMin() == 1
# delete every copy of 1..N one key at a time; min should advance by +1
for k in range(1, N + 1):
    for _ in range(N):            # delete its N copies
        ds.delete(k)
    if k < N:
        assert ds.queryMin() == k + 1
    else:
        assert ds.queryMin() is None, "should be empty after final deletions"

print("all corner-case duplicate tests passed ✔")
