# Prim’s Minimum Spanning Tree (MST) Algorithm Using Greedy Method

## What is Prim’s Algorithm?

Prim’s Algorithm is a **Greedy Algorithm** used to find the:

# Minimum Spanning Tree (MST)

of a graph.

---

# What is Minimum Spanning Tree?

A Minimum Spanning Tree is:

* A tree connecting all vertices
* Uses minimum total edge weight
* Contains no cycles

---

# Output

```text id="d7dzhy"
Edge : Weight
0 - 1 : 2
1 - 2 : 3
1 - 4 : 5
0 - 3 : 6
```

---

# Simple Explanation

## Step 1

Start from any vertex.

Example:

```text id="i4lfhi"
Start from vertex 0
```

---

## Step 2

Choose the smallest edge connected to selected vertices.

Example:

```text id="d3f86q"
0 → 1 (weight 2)
```

---

## Step 3

Add new vertex to MST.

---

## Step 4

Repeat until all vertices are connected.

---

# Why is it called Greedy Algorithm?

Because at every step it chooses:

```text id="wv2qwa"
Smallest possible edge
```

without thinking about future steps.

---

# Graph Used

```text id="52d6ze"
      2
  0 ----- 1
  | \     | \
6 |  \    |5 \ 3
  |   \   |   \
  3     \ 4----2
           7
```

---

# Important Concepts

| Concept | Meaning                        |
| ------- | ------------------------------ |
| Vertex  | Node in graph                  |
| Edge    | Connection between nodes       |
| Weight  | Cost of edge                   |
| MST     | Minimum cost tree              |
| Greedy  | Choose minimum value each step |

---

# Time Complexity

```text id="x6qkn4"
O(V²)
```

where:

```text id="8yyg9x"
V = Number of vertices
```

---

# Real Life Example

Prim’s Algorithm is used in:

* Network cable connections
* Road construction
* Electrical wiring
* Water pipeline systems

to minimize total cost.
