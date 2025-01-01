class graph:
    def __init__(self, directed):
        self.directed = directed
        self.nodes = {}
        self.adj_list = {}
        
    def add_node(self, node_id, value):
        if node_id not in self.nodes:
            self.nodes[node_id] = value
            self.adj_list[node_id] = []
            
    def add_edge(self,u,v):
        if u not in self.adj_list:
            print("Node",u,"does not exist")
            return
        if v not in self.adj_list:
            print("Node",v,"does not exist")
            return

        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
            
        if not self.directed:
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)

    def show(self):
        for key in self.adj_list:
            print("node",key,"connect with",self.adj_list[key])

graphObj = graph(False)
graphObj.add_node(1,"")
graphObj.add_node(2,"")
graphObj.add_node(3,"")
graphObj.add_node(4,"")

graphObj.add_edge(1,3)
graphObj.add_edge(1,2)
graphObj.add_edge(2,4)

graphObj.show()
