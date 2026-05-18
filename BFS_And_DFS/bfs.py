from collections import deque

# Graph
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [],
    3: [],
    4: []
}

visited = set()
queue = deque([0])

print("BFS Traversal:")

while queue:
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            queue.append(neighbor)