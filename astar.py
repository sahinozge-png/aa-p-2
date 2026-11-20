import heapq                                                                        # Import heapq for min-heap priority queue     | 1 time
from dijkstra import build_graph                                                    # Import shared graph builder from dijkstra   | 1 time

def h(n, D):                                                                        # Define admissible heuristic h(n,D) = |D - n| | <= E times
    return abs(D - n)                                                               # Return absolute difference as heuristic     | <= E times

def astar(N, S, D):                                                                 # Define A* search algorithm function         | 1 time per call
    if not (1 <= S <= N and 1 <= D <= N):                                           # Validate S and D are within [1, N]          | 1 time
        raise ValueError(f"S and D must be between 1 and {N}.")                     # Raise clear error on invalid city input     | <= 1 time

    expanded = 0                                                                    # Initialize expanded nodes counter           | 1 time
    adj, repetitions = build_graph(N)                                               # Build graph and get exact build repetitions | 1 time
    g = {i: float('inf') for i in range(1, N + 1)}                                  # Initialize g-scores (cost from S) to inf    | N times
    repetitions += N                                                                # Count N g-score initializations             | 1 time
    parent = {i: None for i in range(1, N + 1)}                                     # Initialize parent dictionary for path       | N times
    repetitions += N                                                                # Count N parent initializations              | 1 time
    closed = set()                                                                  # Initialize closed set of visited nodes      | 1 time
    repetitions += 1                                                                # Count closed set initialization             | 1 time

    g[S] = 0                                                                        # Set start node g-score to 0                 | 1 time
    repetitions += 1                                                                # Count start g-score assignment              | 1 time
    open_heap = [(g[S] + h(S, D), S)]                                               # Initialize open min-heap with (f(S), S)     | 1 time
    repetitions += 1                                                                # Count open heap initialization              | 1 time

    while open_heap:                                                                # Loop while open min-heap is not empty       | <= E + 1 times
        repetitions += 1                                                            # Count while-loop condition check            | <= E + 1 times
        f, u = heapq.heappop(open_heap)                                             # Pop node u with lowest f = g + h score      | <= E times
        if u in closed:                                                             # Skip if node u was already expanded         | <= E times
            continue                                                                # Ignore duplicate entry in heap              | <= E - N times
        closed.add(u)                                                               # Mark node u as expanded in closed set       | <= N times
        expanded += 1                                                               # Increment expanded node counter             | <= N times
        if u == D:                                                                  # Stop early if destination D is reached      | <= N times
            break                                                                   # Exit loop once shortest path is found      | <= 1 time

        for v, w in adj[u]:                                                         # Iterate through all neighbors v of u        | <= E times
            repetitions += 1                                                        # Count each neighbor relaxation check        | <= E times
            new_g = g[u] + w                                                        # Calculate tentative g-score for neighbor v  | <= E times
            if new_g < g[v]:                                                        # Check if new path to v is better            | <= E times
                g[v] = new_g                                                        # Update best known g-score for v             | <= E times
                parent[v] = u                                                       # Set u as predecessor of v                   | <= E times
                heapq.heappush(open_heap, (new_g + h(v, D), v))                     # Push (f(v), v) into open min-heap           | <= E times
                repetitions += 1                                                    # Count heap push operation                   | <= E times

    path = []                                                                       # Initialize list for shortest path           | 1 time
    curr = D                                                                        # Start backtracking from destination D       | 1 time
    while curr is not None:                                                         # Follow parent pointers back to source S     | <= N times
        repetitions += 1                                                            # Count each backtracking step                | <= N times
        path.append(curr)                                                           # Append node to path list                    | <= N times
        curr = parent[curr]                                                         # Move to predecessor node                    | <= N times
    path.reverse()                                                                  # Reverse path to get S -> D order            | 1 time
    repetitions += len(path)                                                        # Count path reversal operations              | 1 time

    if g[D] == float('inf'):                                                        # Check if destination D is unreachable       | 1 time
        return [], float('inf'), repetitions, expanded                              # Return empty path and inf if unreachable    | <= 1 time
    return path, g[D], repetitions, expanded                                        # Return path, cost, repetitions, expanded    | 1 time