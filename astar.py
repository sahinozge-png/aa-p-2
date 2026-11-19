import heapq
from dijkstra import build_graph

def h(n, D):
    return abs(D-n)

def astar(N, S, D):
    repetitions = 0
    expanded = 0
    adj = build_graph(N)
    repetitions += N
    g = {i: float('inf') for i in range(1, N+1)}
    repetitions += N
    parent = {i: None for i in range(1, N+1)}
    repetitions += N
    closed = set()
    repetitions += 1

    g[S] = 0
    repetitions += 1
    open_heap = [(g[S] + h(S, D), S)]
    repetitions += 1

    while open_heap:
        repetitions += 1
        f, u = heapq.heappop(open_heap)
        if u in closed:
            continue
        closed.add(u)
        expanded += 1
        if u == D:
            break

        for v, w in adj[u]:
            repetitions += 1
            new_g = g[u] + w
            if new_g < g[v]:
                g[v] = new_g
                parent[v] = u
                heapq.heappush(open_heap, (new_g + h(v, D), v))
                repetitions += 1

    path = []
    curr = D
    while curr is not None:
        repetitions += 1
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    repetitions += len(path)

    if g[D] == float('inf'):
        return [], float('inf'), repetitions, expanded
    return path, g[D], repetitions, expanded


if __name__ == "__main__":
    print(astar(8, 1, 8))
    print(astar(10, 1, 8))

    # Adım 3: N < 20 için bütün (S, D) çiftlerinde maliyeti Dijkstra ile karşılaştır
    from dijkstra import dijkstra
    total = ok = 0
    for N in range(1, 20):
        for S in range(1, N + 1):
            for D in range(1, N + 1):
                total += 1
                if astar(N, S, D)[1] == dijkstra(N, S, D)[1]:
                    ok += 1
    print(f"A* vs Dijkstra cost check: {ok}/{total} cases match")