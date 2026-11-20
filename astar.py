import heapq                                                                        # Import heapq for min-heap priority queue     | 1 time
import math                                                                         # math.ceil for the hop-based heuristic        | 1 time
from dijkstra import build_graph                                                    # Import shared graph builder from dijkstra   | 1 time

def h(n, D):                                                                        # Given admissible heuristic h(n,D) = |D - n|  | <= E + 1 times
    return abs(D - n)                                                               # Return absolute difference as heuristic     | <= E + 1 times

def h_zero(n, D):                                                                   # Alternative: h = 0 (A* becomes Dijkstra)    | <= E + 1 times
    return 0                                                                        # No information about the goal              | <= E + 1 times

def h_sum(n, D):                                                                    # Alternative: h = n + D (first + last edge)  | <= E + 1 times
    if n == D:                                                                      # Already at the goal?                        | <= E + 1 times
        return 0                                                                    # Nothing left to travel                      | <= 1 time
    return n + D                                                                    # Path cost = n + D + 2*(intermediate cities) | <= E times

def h_hops(n, D):                                                                   # Alternative: hop-based bound (exact here)    | <= E + 1 times
    if n == D:                                                                      # Already at the goal?                        | <= E + 1 times
        return 0                                                                    # Nothing left to travel                      | <= 1 time
    k = math.ceil(abs(D - n) / 3)                                                   # Minimum hops: one hop moves at most 3 cities| <= E times
    low, high = min(n, D), max(n, D)                                                # Smaller and larger end of the trip          | <= E times
    return low + (2 * k - 1) * high - 3 * k * (k - 1)                               # = low + high + 2*sum(high - 3m), m=1..k-1   | <= E times

def astar(N, S, D, heuristic=h, trace=False):                                       # A* search; default heuristic is the given h | 1 time per call
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
    open_heap = [(g[S] + heuristic(S, D), S)]                                       # Initialize open min-heap with (f(S), S)     | 1 time
    repetitions += 1                                                                # Count open heap initialization              | 1 time

    if trace:                                                                       # Check if step-by-step trace output is on    | 1 time
        print(f"\n--- A* Trace (N={N}, S={S}, D={D}) ---")                          # Print trace header                          | <= 1 time

    while open_heap:                                                                # Loop while open min-heap is not empty       | <= E + 1 times
        repetitions += 1                                                            # Count while-loop condition check            | <= E + 1 times
        f, u = heapq.heappop(open_heap)                                             # Pop node u with lowest f = g + h score      | <= E times
        if u in closed:                                                             # Skip if node u was already expanded         | <= E times
            continue                                                                # Ignore duplicate entry in heap              | <= E - N times
        closed.add(u)                                                               # Mark node u as expanded in closed set       | <= N times
        expanded += 1                                                               # Increment expanded node counter             | <= N times
        if trace:                                                                   # Print expanded node if tracing              | <= N times
            print(f"Step {expanded}: expand {u}  (g={g[u]}, h={heuristic(u, D)}, f={f})")# Expanded node with g, h, f | <= N times
        if u == D:                                                                  # Stop early if destination D is reached      | <= N times
            break                                                                   # Exit loop once shortest path is found       | <= 1 time

        for v, w in adj[u]:                                                         # Iterate through all neighbors v of u        | <= E times
            repetitions += 1                                                        # Count each neighbor relaxation check        | <= E times
            new_g = g[u] + w                                                        # Calculate tentative g-score for neighbor v  | <= E times
            if new_g < g[v]:                                                        # Check if new path to v is better            | <= E times
                g[v] = new_g                                                        # Update best known g-score for v             | <= E times
                parent[v] = u                                                       # Set u as predecessor of v                   | <= E times
                heapq.heappush(open_heap, (new_g + heuristic(v, D), v))             # Push (f(v), v) into open min-heap           | <= E times
                repetitions += 1                                                    # Count heap push operation                   | <= E times
        if trace:                                                                   # Print OPEN and CLOSED lists if tracing      | <= N times
            print(f"        OPEN = {sorted(open_heap)}  CLOSED = {sorted(closed)}") # Lists after the step | <= N times

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

HEURISTICS = [                                                                      # Heuristics compared in Q5                   | 1 time
    ("h = |D - n| (given)", h),                                                     # The heuristic required by the project       | 1 time
    ("h = 0 (Dijkstra)", h_zero),                                                   # Baseline: no heuristic                      | 1 time
    ("h = n + D", h_sum),                                                           # First and last edge bound                   | 1 time
    ("h = hop-based (exact)", h_hops),                                              # Minimum-hops bound                          | 1 time
]                                                                                   # End of the list                             | 1 time

def compare_heuristics():                                                           # Q5 table: expanded nodes / repetitions      | 1 time per call
    print("\n--- Heuristic comparison: expanded nodes / total repetitions ---")     # Print table title           | 1 time
    print(f"{'N':<6}{'S':>3}{'D':>6}" + "".join(f"{name:>24}" for name, _ in HEURISTICS))# Print header | 1 time
    for N, S, D in [(8, 1, 8)] + [(n, 1, n) for n in [10, 50, 100, 200, 500, 1000, 2000]]:# Q4 case + benchmark sizes | 8 times
        line = f"{N:<6}{S:>3}{D:>6}"                                                # Start the row with N, S, D                  | 8 times
        for name, func in HEURISTICS:                                               # Every heuristic in the list                 | 32 times
            _, _, reps, exp = astar(N, S, D, heuristic=func)                        # Run A* with this heuristic                  | 32 times
            line += f"{f'{exp} / {reps}':>24}"                                      # Add expanded / repetitions to the row       | 32 times
        print(line)                                                                 # Print the row                               | 8 times

def check_heuristics():                                                             # Every heuristic must match Dijkstra's cost  | 1 time per call
    from dijkstra import dijkstra                                                   # Import Dijkstra for the cross-check         | 1 time
    print("\n--- Correctness: A* cost vs Dijkstra cost, all N < 20 and all (S, D) ---")# Print title          | 1 time
    for name, func in HEURISTICS:                                                   # Every heuristic in the list                 | 4 times
        total = ok = 0                                                              # Reset the counters                          | 4 times
        for N in range(1, 20):                                                      # Every N from 1 to 19                        | 76 times
            for S in range(1, N + 1):                                               # Every source city                           | 760 times
                for D in range(1, N + 1):                                           # Every destination city                      | 9880 times
                    total += 1                                                      # Count one test case                         | 9880 times
                    if astar(N, S, D, heuristic=func)[1] == dijkstra(N, S, D)[1]:   # Same cost? | 9880 times
                        ok += 1                                                     # Count a matching case                       | <= 9880 times
        print(f"{name:<23} {ok}/{total} cases match")                               # Print the result for this heuristic         | 4 times

if __name__ == "__main__":                                                          # Run only when astar.py is started directly  | 1 time
    path, cost, reps, exp = astar(8, 1, 8, trace=True)                              # Q4: step table for N=8, S=1, D=8            | 1 time
    print(f"\nShortest Path: {path}  Total Cost: {cost}  Repetitions: {reps}  Expanded: {exp}")# Q4 result | 1 time
    compare_heuristics()                                                            # Q5: alternative heuristics table            | 1 time
    check_heuristics()                                                              # Q5: every heuristic finds the shortest path | 1 time
