Title: 
Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem or a graph color problem.


# 8 Queens Problem Using Branch and Bound (Python)

## Problem Statement

Place 8 queens on an 8×8 chessboard such that:

* No two queens attack each other
* No same row
* No same column
* No same diagonal

---

# Sample Output

```text id="egudk9"
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
```

---

# Simple Explanation

## What is Branch and Bound?

Branch and Bound improves Backtracking by:

* Avoiding unnecessary checks
* Stopping invalid paths early

This makes the program faster.

---

# How the Code Works

## Step 1: Start from Row 0

Try placing queen in each column.

---

## Step 2: Check Safe Position

Before placing queen, check:

* Column
* Left diagonal
* Right diagonal

If safe → place queen.

---

## Step 3: Move to Next Row

Program recursively places next queen.

---

## Step 4: Backtracking

If no safe position found:

```text id="q19f4w"
Remove previous queen
Try next position
```

---

# Branch and Bound Optimization

Instead of checking whole board every time, we use arrays:

```python id="jqthkr"
column[]
leftDiagonal[]
rightDiagonal[]
```

These arrays quickly tell whether position is safe.

This reduces execution time.

---

# Time Complexity

```text id="ukgptf"
O(N!)
```

But Branch and Bound is much faster than normal brute force.

---

# Important Concepts Used

| Concept          | Purpose                  |
| ---------------- | ------------------------ |
| Recursion        | Solve row by row         |
| Backtracking     | Remove wrong choices     |
| Branch and Bound | Skip invalid paths early |
| Arrays           | Fast safety checking     |
