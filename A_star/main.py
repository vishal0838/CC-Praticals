# Graph with cost
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

open_list = ['A']
closed_list = []

g = {'A': 0}

parent = {'A': 'A'}

while open_list:

    # Find node with minimum f = g + h
    n = open_list[0]

    for node in open_list:
        if g[node] + h[node] < g[n] + h[n]:
            n = node

    # Goal node found
    if n == 'G':
        path = []

        while parent[n] != n:
            path.append(n)
            n = parent[n]

        path.append('A')
        path.reverse()

        print("Path found:", path)
        break

    for (m, cost) in graph[n]:

        if m not in open_list and m not in closed_list:
            open_list.append(m)
            parent[m] = n
            g[m] = g[n] + cost

    open_list.remove(n)
    closed_list.append(n)