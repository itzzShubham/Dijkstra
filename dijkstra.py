import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  
    distances[start] = 0 
    queue = [(0, start)] 
    
    while queue: 
        current_distance, current_node = heapq.heappop(queue)  
        if current_distance > distances[current_node]:  
            continue
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))  
    
    return distances
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3},
    'E': {'C': 8, 'D': 3}
}

distances = dijkstra(graph, 'A')  
print(distances)  
