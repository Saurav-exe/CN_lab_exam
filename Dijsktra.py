import heapq

def dijkstra(graph, source):
    # Distance from source to every node (infinity at start)
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    # Priority queue for picking shortest edge
    pq = [(0, source)]

    # Store shortest path tree
    parent = {node: None for node in graph}

    while pq:
        curr_dist, node = heapq.heappop(pq)

        # Skip if old entry
        if curr_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, parent


# Example graph
# Replace this with your instructor's network diagram
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 5), ('B', 1), ('D', 2)],
    'D': [('B', 4), ('C', 2)]
}

source = 'A'
distances, parents = dijkstra(graph, source)

print("Shortest distances from", source)
for node, d in distances.items():
    print(node, ":", d)

print("\nShortest Path Tree (parent pointers)")
for node, p in parents.items():
    print(node, "←", p)
