import heapq
import math
from typing import Dict, List, Tuple

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # Initialize distances to infinity
    distances[start] = 0  # Distance to the starting node is 0
    priority_queue = [(0, start)]  # (distance, node)  Use a min-heap
    visited= set()

    while priority_queue:
        dist, u = heapq.heappop(priority_queue)  # Get the node with the smallest distance
        if u in visited:
            continue
        visited.add(u)

        if dist > distances[u]:  # Important: Check if the distance is outdated
            continue

        for v, weight in graph[u]:  # Iterate over neighbors of u
            new_distance = distances[u] + weight
            if new_distance < distances[v]:
                distances[v] = new_distance
                heapq.heappush(priority_queue, (new_distance, v))
    return distances

graph = {
    1: [(2, 2), (3, 4)],  # Node 1 has edges to Node 2 with weight 2, and Node 3 with weight 4
    2: [(3, 1), (4, 5)],
    3: [(4, 1)],
    4: []
}
start_node = 1
distances = dijkstra(graph, start_node)
print(f"Shortest distances from node {start_node}: {distances}")

"""
graph {1: [(2, 2), (3, 4)], 2: [(3, 1), (4, 5)], 3: [(4, 1)], 4: []}
distances {1: inf, 2: inf, 3: inf, 4: inf}
distances {1: 0, 2: inf, 3: inf, 4: inf}
priority_queue [(0, 1)]
visited set()
dist, u 0 1
priority_queue []
visited {1}
distances {1: 0, 2: inf, 3: inf, 4: inf}
v, weight 2 2
new_distance 2
priority_queue [(2, 2)]
distances {1: 0, 2: 2, 3: inf, 4: inf}
v, weight 3 4
new_distance 4
priority_queue [(2, 2), (4, 3)]
distances {1: 0, 2: 2, 3: 4, 4: inf}
dist, u 2 2
priority_queue [(4, 3)]
visited {1, 2}
distances {1: 0, 2: 2, 3: 4, 4: inf}
v, weight 3 1
new_distance 3
priority_queue [(3, 3), (4, 3)]
distances {1: 0, 2: 2, 3: 3, 4: inf}
v, weight 4 5
new_distance 7
priority_queue [(3, 3), (4, 3), (7, 4)]
distances {1: 0, 2: 2, 3: 3, 4: 7}
dist, u 3 3
priority_queue [(4, 3), (7, 4)]
visited {1, 2, 3}
distances {1: 0, 2: 2, 3: 3, 4: 7}
v, weight 4 1
new_distance 4
priority_queue [(4, 3), (7, 4), (4, 4)]
distances {1: 0, 2: 2, 3: 3, 4: 4}
dist, u 4 3
priority_queue [(4, 4), (7, 4)]
dist, u 4 4
priority_queue [(7, 4)]
visited {1, 2, 3, 4}
distances {1: 0, 2: 2, 3: 3, 4: 4}
dist, u 7 4
priority_queue []
Shortest distances from node 1: {1: 0, 2: 2, 3: 3, 4: 4}
"""