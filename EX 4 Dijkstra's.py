import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, node = heapq.heappop(pq)
        for neighbor, weight in graph[node]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    return dist

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
print(dijkstra(graph, 'A'))
