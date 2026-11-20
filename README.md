# COMP 303 Project 2: Dijkstra vs. A* Shortest Path

Özge Şahin (042401063), Can Önen (042401037)

## Requirements

- Python 3 (tested with Python 3.13)
- matplotlib, used by `main.py` for the benchmark plot:

```
pip install matplotlib
```

## Files

- `dijkstra.py`: graph builder (`build_graph`) and Dijkstra's algorithm with a min-heap, repetition counter and optional step trace
- `astar.py`: A* search with h(i, j) = |j − i|, repetition and expanded-node counters, optional step trace and the alternative heuristics
- `main.py`: menu program that reads N (< 20), S and D, prints the shortest path and its total cost, then runs the benchmark for N = 10, 50, 100, 200, 500, 1000, 2000 (S = 1, D = N) and saves `benchmark_comparison.png`

## How to run

```
python main.py
```

Menu options: 1 = Dijkstra (with step trace), 2 = A* search, 3 = compare both. Then enter N (< 20), S and D.

```
python astar.py
```

Prints the A* trace for N = 8, S = 1, D = 8, the heuristic comparison table and the cost check against Dijkstra for all 2,470 (N, S, D) cases with N < 20.

On some systems the command is `python3` instead of `python`.

## Expected results

- `main.py`, option 1, N = 10, S = 1, D = 8: path [1, 2, 5, 8], cost 23, 151 repetitions
- `main.py`, option 2, N = 8, S = 1, D = 8: path [1, 2, 5, 8], cost 23, 127 repetitions, 8 nodes expanded
- Benchmark at N = 2000: Dijkstra 37,310 repetitions, A* 37,311 repetitions
