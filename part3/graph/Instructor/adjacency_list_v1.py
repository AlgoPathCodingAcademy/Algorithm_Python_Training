adj_list = {}
V = 8

edges = [(1,2),(1,3),(2,4),(3,4),(3,5),(6,7)]

for edge in edges:
    if edge[0] not in adj_list:
        adj_list[edge[0]] = [edge[1]]
    else:
        adj_list[edge[0]].append(edge[1])

    if edge[1] not in adj_list:
        adj_list[edge[1]] = [edge[0]]
    else:
        adj_list[edge[1]].append(edge[0])

print("partial adj_list", adj_list)

output_result = V * [0]
for index in range(V):
    if index in adj_list:
        output_result[index] = adj_list[index]
    else:
        output_result[index] = []

print("Full adj_list", output_result)
