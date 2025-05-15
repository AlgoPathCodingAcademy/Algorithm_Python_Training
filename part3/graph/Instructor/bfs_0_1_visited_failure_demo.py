from collections import deque

# adjacency list:  u -> list of (v, weight) with weight in {0, 1}
G = {
    0: [(1, 1), (2, 0)],
    1: [],
    2: [(1, 0)],
}

# ────────────────────────────────────────────────────────────────
# 0/1-BFS **WRONG** version: uses a visited set
def bfs_with_visited(start, target, graph):
    dq = deque([(start, 0)])     # (vertex, accumulated_cost)
    visited = {start}

    while dq:
        u, cost = dq.popleft()
        if u == target:
            return cost

        for v, w in graph.get(u, []):
            if v in visited:          # ▸ the fatal early-marking
                continue
            visited.add(v)
            if w == 0:
                dq.appendleft((v, cost))
            else:
                dq.append((v, cost + 1))
    return float("inf")


# ────────────────────────────────────────────────────────────────
# 0/1-BFS **CORRECT** version: keeps a distance table
def bfs_with_dist(start, target, graph):
    INF = 10**9
    dist = {u: INF for u in graph}
    dist[start] = 0
    dq = deque([start])

    while dq:
        u = dq.popleft()
        for v, w in graph[u]:
            new_cost = dist[u] + w
            if new_cost < dist[v]:        # ▸ relax edge as in Dijkstra
                dist[v] = new_cost
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return dist[target]


# ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Visited-based 0/1-BFS distance 0→1 :", bfs_with_visited(0, 1, G))
    print("Distance-array 0/1-BFS distance 0→1:", bfs_with_dist(0, 1, G))
