Title:
Implement depth first search algorithm and Breadth First Search algorithm, use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.

# Simple Explanation

## Graph Used

```text
      0
     / \
    1   2
   / \
  3   4
```

---

# BFS (Breadth First Search)

## Output

```text
0 1 2 3 4
```

## What it does

* Visits nodes level by level
* Uses a Queue
* First visits nearby nodes

Example:

```text
0 → 1 → 2 → 3 → 4
```

---

# DFS (Depth First Search)

## Output

```text
0 1 3 4 2
```

## What it does

* Goes deep first
* Uses Recursion
* Visits one path completely before returning

Example:

```text
0 → 1 → 3 → 4 → 2
```

---

# Main Difference

| BFS                  | DFS                              |
| -------------------- | -------------------------------- |
| Level wise traversal | Deep traversal                   |
| Uses Queue           | Uses Recursion/Stack             |
| Finds shortest path  | Does not guarantee shortest path |
