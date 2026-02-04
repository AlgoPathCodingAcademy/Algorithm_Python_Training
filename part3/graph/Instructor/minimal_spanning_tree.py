class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.num_sets = 0
        
    def is_in(self, x):
        if x not in self.parent:
            return False
            
        return True
        
    def find(self,x):
        node = x
        while True:
            parent = self.parent[node]
            if parent == node:
                break
            
            node = parent

        node_ = x
        while True:
            parent  = self.parent[node_]
            if node_ == parent:
                break

            self.parent[node_] = node
            node_ = parent
        
        return node_
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.num_sets = self.num_sets - 1
        
        return True
        
    def add(self, x):
        if x in self.parent:
            return
        
        self.parent[x] = x
        self.size[x] = 1
        self.num_sets += 1
        
    def connected(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return True
            
        return False
        
    def get_num_of_sets(self):
        return self.num_sets
        
        
    def get_size_of_set(self,x):
        root = self.find(x)
        return self.size[root]
        

uf = UnionFind()  # Initialize an empty Union-Find structure

n = 4
edges = [
    (0, 1, 1),
    (0, 2, 4),
    (1, 2, 2),
    (1, 3, 5),
    (2, 3, 3)
]

'''
n = 4
edges = [
    (0, 1, 1),
    (2, 3, 4)
]
'''

edges.sort(key=lambda item:item[-1])

print(edges)

for node in range(n):
    uf.add(node)

total_weights = 0
edges_used = 0

for u,v,weight in edges:
    if uf.union(u,v):
        total_weights += weight
        edges_used = edges_used + 1
    
    if edges_used == n-1:
        break
        
if edges_used != n-1:
    print("no MST")
            
print(total_weights)
