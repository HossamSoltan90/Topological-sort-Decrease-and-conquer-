def dfs(graph, vertex, stack, visited):
    visited.add (vertex)
    
    for neighbor in graph[vertex]: 
        if neighbor not in visited:
            dfs (graph, neighbor, stack, visited) 
    
    stack.append(vertex)


def topological_sort(graph) :
    stack = []
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            dfs (graph, vertex, stack, visited)
    
    ordering = []
    
    while stack:
        ordering.append(stack.pop())
    return ordering




# Example graph
graph = {
    'G': ['B', 'F'],
    'A': ['B', 'C'],
    'B': ['C', 'F'],
    'C': ['D'],
    'D': [],
    'E': [],
    'F': ['D', 'E'],
    
}

# Run topological sort on the example graph
result = topological_sort(graph)

print("Topological Order:")
print('\n')
print(result)
print('\n')


