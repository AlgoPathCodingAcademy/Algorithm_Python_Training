# Problem Statement: You are given an unweighted graph represented as an adjacency list and two nodes:
# start_node and end_node. Your task is to find the shortest path (in terms of the number of edges) between these two nodes.
# If there is no path between the two nodes, return -1.

# Input Format:
# The first line contains two integers n and m:
# n: the number of nodes (labeled 1 through n).
# m: the number of edges.
# The next m lines each contain two integers u and v indicating an undirected edge between nodes u and v.
# The final line contains two integers, start_node and end_node.

# Output Format:
# Output a single integer: the length of the shortest path between start_node and end_node. If no path exists, output -1.

# Example input:
# 8 9
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 4 6
# 5 7
# 6 8
# 7 8
# 1 8
# Example Output:
# 4

# Explanation: The graph can be visualized as follows:
#    1
#   / \
#  2   3
# / \    \
#4   5    6
# \   \   /
#  6   7-8

# The shortest path from node 1 to node 8 is:
# 1 → 3 → 6 → 8
# The shortest path has a length of 4.
