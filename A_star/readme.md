# A* (A Star) Algorithm for Path Finding

## What is A* Algorithm?

A* is a searching algorithm used to find the:

# Shortest Path

between two points.

It is used in:

* Games
* Google Maps
* Robot navigation

---

# Simple Example

We will find path from:

```text id="jpr8s9"
A → G
```

---

# Output

```text id="9fcjlwm"
Path found: ['A', 'C', 'F', 'G']
```

---

# Simple Explanation

## A* Formula

```text id="xjlwm7"
f(n) = g(n) + h(n)
```

Where:

| Term | Meaning                |
| ---- | ---------------------- |
| g(n) | Actual path cost       |
| h(n) | Estimated cost to goal |
| f(n) | Total cost             |

---

# How Algorithm Works

## Step 1

Start from source node.

```text id="e2bg6p"
A
```

---

## Step 2

Calculate:

```text id="k9v6ph"
f = g + h
```

for neighboring nodes.

---

## Step 3

Choose node with smallest value.

---

## Step 4

Repeat until goal node is reached.

---

# Why A* is Important?

A* is smart because:

* It uses actual cost
* AND estimated future cost

So it finds path faster.

---

# Real Life Uses

A* is used in:

* Video games
* GPS navigation
* Maze solving
* Robotics
* Path planning

---

# Important Concepts

| Concept     | Purpose                   |
| ----------- | ------------------------- |
| Open List   | Nodes to explore          |
| Closed List | Already explored nodes    |
| Heuristic   | Estimated distance        |
| Path Cost   | Actual distance travelled |

---

# Advantage of A*

```text id="4wpyq5"
Fast and finds shortest path
```

Compared to normal search algorithms.
