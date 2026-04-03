#  Tower of Hanoi in Prolog

## Aim
To implement the **Tower of Hanoi problem** using **first-order logic** in Prolog.

---

## Algorithm

1. **Base case**
   - Move 1 disk from source to destination.

2. **Recursive case (N > 1)**
   - Compute `M = N - 1`.

3. **Move M disks to auxiliary**
   - Transfer smaller stack to helper peg.

4. **Move 1 disk to destination**
   - Place the largest disk directly.

5. **Move M disks from auxiliary to destination**
   - Transfer the smaller stack onto the largest disk.

6. **Repeat recursively**
   - Continue until all disks are moved.

---

## Code
[`toh.pl`](toh.pl)

---

## Output
_Output image not available in repository._

---

## Result
The **Tower of Hanoi problem** was successfully implemented in Prolog using recursion and first-order logic, producing the correct sequence of moves to transfer all disks from the source peg to the destination peg.
