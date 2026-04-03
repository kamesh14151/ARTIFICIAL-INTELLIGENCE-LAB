#  Water Jug Problem in Prolog

##  Aim
To implement the **Water Jug problem** using **first-order logic** in Prolog.

---

##  Algorithm

1. **Define valid jug operations**
   - Actions: `fill`, `empty`, `pour`

2. **Specify goal state**
   - Example: 2 liters in jug1

3. **Implement move/3**
   - Represent all possible actions.

4. **Use BFS (Breadth-First Search)**
   - Explore possible states systematically.

5. **Track visited states**
   - Avoid cycles and repeated exploration.

6. **Return path to goal**
   - Output the sequence of actions leading to the solution.

---

##  Code
[`water-jug.pl`](water-jug.pl)

---

##  Output
_Output image not available in repository._

---

##  Result
The **Water Jug problem** was successfully implemented in Prolog. The program explored states using BFS, avoided cycles, and returned the correct sequence of actions to reach the goal state.
