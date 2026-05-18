# Graph
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [],
    3: [],
    4: []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

print("DFS Traversal:")
dfs(0)