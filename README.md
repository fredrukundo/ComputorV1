# 🧮 ComputorV1 — Advanced Polynomial Equation Solver (42 Project)

> A complete polynomial equation solver written in Python.  
> Handles equations up to degree 2, including real and complex solutions.  
> Fully compliant with the 42 subject — including mandatory and bonus parts.

---

# 📌 Project Overview

ComputorV1 parses, reduces, and solves polynomial equations of the form:

```
a * X^0 + b * X^1 + c * X^2 = d * X^0 + ...
```

It supports:

- Reduction to canonical form
- Degree detection
- Degree 0 resolution
- Degree 1 resolution
- Degree 2 resolution
- Real solutions
- Complex solutions
- Fraction input (bonus)
- Natural input format (bonus)
- Irreducible fraction output (bonus)
- Error handling
- Intermediate step display (bonus)

---

# 📂 Project Architecture

```
ComputorV1/
│
├── mandatory/
│   ├── main.py
│   ├── parser.py
│   ├── reducer.py
│   ├── solver.py
│   └── math_utils.py
│
├── bonus/
│   ├── main.py
│   ├── parser.py
│   ├── reducer.py
│   ├── solver.py
│   └── math_utils.py
│
└── README.md
```

---

# ✅ Mandatory Part

## ✔ What It Must Do

- Accept one equation as argument
- Display reduced form
- Display polynomial degree
- Solve degree 0, 1, 2
- Refuse degree > 2
- Handle negative numbers
- Handle decimals
- Handle fractions (if implemented in mandatory)
- Never crash
- Never infinite loop

---

## ▶️ Run Mandatory

```bash
cd mandatory
python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
```

---

## 🧪 Mandatory Test Cases

### Degree 0 — Infinite Solutions
```bash
python3 main.py "42 * X^0 = 42 * X^0"
```

Expected:
```
Any real number is a solution.
```

---

### Degree 0 — No Solution
```bash
python3 main.py "4 * X^0 = 8 * X^0"
```

Expected:
```
No solution.
```

---

### Degree 1
```bash
python3 main.py "2 * X^1 = 4 * X^0"
```

Expected:
```
2
```

---

### Degree 2 — Real Solutions
```bash
python3 main.py "1 * X^2 - 5 * X^1 + 6 * X^0 = 0"
```

Roots:
```
2
3
```

---

### Degree 2 — Complex Solutions
```bash
python3 main.py "1 * X^2 + 1 * X^0 = 0"
```

Expected:
```
-0 + 1i
-0 - 1i
```

---

### Degree > 2
```bash
python3 main.py "1 * X^3 + 1 * X^0 = 0"
```

Expected:
```
The polynomial degree is strictly greater than 2, I can't solve.
```

---

# ⭐ Bonus Part

The bonus extends the solver significantly.

---

## ✔ Natural Input Support

Accepts:

```
X = 0
4X = 8
2X + 1 = 0
5 + X^2 = X^2
```

---

## ✔ Fraction Input

```
5/2 * X^0 = 1
```

Interpreted as:
```
2.5 * X^0 = 1
```

---

## ✔ Irreducible Fraction Output

```
2X = 1
```

Outputs:
```
1/2
```

---

## ✔ Complex Solutions With Rational Parts

```
5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0
```

Output:
```
-1/2 + 1.040833i
-1/2 - 1.040833i
```

Rational parts simplified.
Irrational parts kept as clean decimals.

---

## ✔ Error Handling

Detects:
- Missing '='
- Invalid characters
- Invalid variable names
- Invalid power syntax
- Division by zero in fractions
- Malformed equations

Never prints Python traceback.

---

## ✔ Intermediate Steps (Bonus)

Displays:
- Parsing phase
- Reduction phase
- Discriminant value
- Solution type decision

---

# 🧠 Mathematical Concepts

## 1️⃣ Polynomial

A polynomial is an expression of the form:

\[
P(X) = a_0 + a_1X + a_2X^2 + ...
\]

The **degree** is the highest exponent.

---

## 2️⃣ Discriminant

\[
\Delta = b^2 - 4ac
\]

- Δ > 0 → Two real roots  
- Δ = 0 → One real root  
- Δ < 0 → Two complex roots  

---

## 3️⃣ Complex Solutions

When Δ < 0:

\[
X = \frac{-b \pm i\sqrt{-\Delta}}{2a}
\]

---

## 4️⃣ Euclidean Algorithm

Used to simplify fractions:

```
gcd(a, b)
```

---

## 5️⃣ Newton’s Method

Custom square root implementation:

```
sqrt_newton(n)
```

Avoids forbidden math functions.

---

# 🔒 Stability & Safety

The program guarantees:

- No infinite loops
- No division by zero
- No float explosion
- Safe epsilon comparisons
- Clean error reporting
- Controlled fraction denominator growth

---

# 🎓 Defense Preparation

If evaluator asks:

**Q: Why separate mandatory and bonus?**  
Mandatory must be perfect independently before bonus is evaluated.

**Q: Why custom square root?**  
Subject forbids direct `math.sqrt`.

**Q: How do you avoid floating precision issues?**  
Using small tolerance (`1e-10`) and controlled fraction conversion.

**Q: Why not always convert to fraction?**  
Irrational numbers must remain decimal; only rational numbers are simplified.

**Q: How do you prevent infinite loops?**  
Bounded Newton iterations and safe numeric thresholds.

---

# 🧪 Full Evaluation Script

Run these during defense:

```bash
# Mandatory tests
python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
python3 main.py "42 * X^0 = 42 * X^0"
python3 main.py "4 * X^0 = 8 * X^0"
python3 main.py "1 * X^2 - 2 * X^1 + 1 * X^0 = 0"
python3 main.py "1 * X^2 + 1 * X^0 = 0"
python3 main.py "1 * X^3 + 1 * X^0 = 0"

# Bonus tests
python3 main.py "2X + 1 = 0"
python3 main.py "5/2 * X^0 = 1"
python3 main.py "X^2 + 1 = 0"
python3 main.py "5 + X^2 = X^2"
python3 main.py "5 + Y = 0"
```

---

# 🏁 Conclusion

ComputorV1 is not just a formula implementation.

It demonstrates:

- Algebra mastery
- Numerical reasoning
- Robust parsing
- Defensive programming
- Modular architecture
- Clean CLI design
- Mathematical rigor

---

**Author:** Fred Rukundo  
42 Network — ComputorV1 Project
