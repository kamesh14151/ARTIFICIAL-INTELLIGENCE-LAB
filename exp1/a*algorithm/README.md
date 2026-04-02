# A* Algorithm

## 🎯 Aim

To implement the **A\* (A-Star) algorithm** to find the shortest path between a start node and a goal node using heuristics.

---

## 📚 Algorithm

1. Initialize the **open list** with the start node
2. Set `g(start) = 0`
3. Compute `f(start) = g(start) + h(start)`
4. Initialize **closed list** = empty
5. Repeat until open list is empty:
   - **a)** Select the node with the **lowest f(n)** from the open list
   - **b)** If the node is the **goal**, return the path
   - **c)** Move the node to the **closed list**
   - **d)** For each **neighbor**:
     - Calculate `g(n) = g(current) + cost`
     - Compute `f(n) = g(n) + h(n)`
     - If neighbor is **not in open/closed list** OR has a **lower g(n)**:
       - Update parent
       - Add to open list
6. If goal not reached, return **failure**

---

## 💻 Code

> Source: `exp2/a*algorithm/a*.png`

---

## ✅ Result

Thus, the **A\* algorithm** was successfully implemented and the shortest path from the **start node** to the **goal node** was found using heuristic values.
