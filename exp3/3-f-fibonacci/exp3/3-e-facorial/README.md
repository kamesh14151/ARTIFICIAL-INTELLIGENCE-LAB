# 🔢 Fibonacci in Prolog

## 🎯 Aim
To implement the **Fibonacci series** using **first-order logic** in Prolog.

---

## 📚 Algorithm

1. **Base cases**
   - `fibonacci(0, 0)`
   - `fibonacci(1, 1)`

2. **Recursive case (N > 1)**
   - Compute `N1 = N - 1` and `N2 = N - 2`

3. **Recursive calls**
   - `fibonacci(N1, R1)`
   - `fibonacci(N2, R2)`

4. **Sum results**
   - `Result = R1 + R2`

5. **Return result**
   - Output the computed Fibonacci number.

6. **Use recursion until base case**
   - Continue until reaching `fibonacci(0,0)` or `fibonacci(1,1)`.

---

## 💻 Code
[`exp3/prolog/fibonacci.pl`](exp3/prolog/fibonacci.pl)

---

## 🖼️ Output
![Fibonacci Output](exp3/prolog/fibonacci.png)

---

## ✅ Result
The **Fibonacci series** was successfully implemented in Prolog using recursion and first-order logic, producing correct results for given inputs.
