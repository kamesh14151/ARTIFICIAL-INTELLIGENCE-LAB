# A* Algorithm

## 🎯 Aim
To implement the **A\* (A-Star) algorithm** to find the shortest path between a start node and a goal node using heuristics.

---

## 📚 Algorithm

1. Initialize the **open list** with the start node; set `g(start) = 0`, `f(start) = g(start) + h(start)`
2. Initialize **closed list** = empty
3. Repeat until open list is empty:
   - Pick node with **lowest f(n)** → if goal, **return path**
   - Move node to **closed list**
   - For each neighbor: compute `g(n) = g(current) + cost`, `f(n) = g(n) + h(n)`
   - If not in open/closed list OR lower `g(n)` → update parent & add to open list
4. If goal not reached → return **failure**

---

## 💻 Code

[`exp1/a*algorithm/a*.py`](exp1/a*algorithm/a*.py)

---

## 🖼️ Output

![A* Output](exp1/a*algorithm/a*.png)

---

## ✅ Result
The **A\* algorithm** was successfully implemented and the shortest path from the **start node** to the **goal node** was found using heuristic values.
