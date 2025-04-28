import heapq
class dataCollection:
    def __init__(self):
        self.heap = []
        self.hashTable = {}
        
    def delete(self,x):
        self.hashTable[x] -= 1
        
    def insert(self,x):
        if x not in self.hashTable:
            self.hashTable[x] = 1
            heapq.heappush(self.heap,x)
        else:
            self.hashTable[x] += 1

    def queryMin(self):
        while True:
            first_value = self.heap[0]
            if first_value in self.hashTable:
                if self.hashTable[first_value] == 0:
                    self.hashTable.pop(first_value)
                    heapq.heappop(self.heap)
                else:
                    break
            else:
                break
        
        return self.heap[0]
            
# ------------------------------------------------------------
# corner-case tests focusing on many copies of the same number
# ------------------------------------------------------------

def fresh():
    return dataCollection()          # assumes your class is already imported


# 0. sanity: empty → insert duplicate min → pop all duplicates → empty again
ds = fresh()
ds.insert(4); ds.insert(4); ds.insert(4)
assert ds.queryMin() == 4
ds.delete(4); ds.delete(4); ds.delete(4)
try:
    ds.queryMin()
except IndexError:
    pass
else:
    raise AssertionError("should be empty after deleting all copies")

# 1.   100 identical values
ds = fresh()
for _ in range(100):
    ds.insert(42)
assert ds.queryMin() == 42        # min must be 42 while any copy remains
for _ in range(99):
    ds.delete(42)
assert ds.queryMin() == 42        # still one live copy
ds.delete(42)                     # last copy removed
try:
    ds.queryMin()
except IndexError:
    pass
else:
    raise AssertionError("structure should be empty")

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
        try:
            ds.queryMin()
        except IndexError:
            pass
        else:
            raise AssertionError("should be empty after final deletions")

print("all corner-case duplicate tests passed ✔")

