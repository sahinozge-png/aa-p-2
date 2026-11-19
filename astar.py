import heapq
from dijkstra import build_graph

def h(n, D):
    return abs(D-n)

def astar(N, S, D):
    adj = build_graph(N)
    g = {i: float('inf') for i in range(1, N+1)}
    parent = {i: None for i in range(1, N+1)}
    closed = set()

    g[S] = 0
    open_heap = [(g[S] + h(S, D), S)]

    while open_heap:
        f, u = heapq.heappop(open_heap)
        if u in closed:
            continue 
        closed.add(u)
        if u == D:
            break

        for v, w in adj[u]:
            new_g = g[u] + w
            if new_g < g[v]:
                g[v] = new_g
                parent[v] = u
                heapq.heappush(open_heap, (new_g + h(v, D), v))

    path = []
    curr = D
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    if g[D] == float('inf'):
        return [], float('inf')
    return path, g[D]


if __name__ == "__main__":
    print(astar(8, 1, 8))
    print(astar(10, 1, 8))