
# 🐍 Python Quick Revision Numbers Notes

Minimal, example-focused notes for fast review.

---

## 🔗 Chained Comparisons

```python
2 < 3 < 4       # True (same as: 2 < 3 and 3 < 4)
2 == 3 < 5      # False (2 == 3 is False)
```

---

## ⬇️ `floor()` vs `trunc()`

| Function    | 3.7 | -3.7 |
|-------------|-----|------|
| `floor()`   |  3  | -4   |
| `trunc()`   |  3  | -3   |

```python
from math import floor, trunc
floor(3.7)    # 3
trunc(-3.7)   # -3
```

❌ Do not work with complex numbers  
✅ Use `z.real` to extract real part

---

## 🔢 Imaginary Numbers

```python
z = 3 + 4j
z.real    # 3.0
z.imag    # 4.0
abs(z)    # 5.0

import cmath
cmath.sqrt(-1)   # 1j
```

---

## 🔣 Integer Literals & Conversion

```python
0o20    # Octal → 16
0xff    # Hex → 255
0b100   # Binary → 4
```

### Convert to base:
```python
oct(16)      # '0o20'
hex(255)     # '0xff'
bin(4)       # '0b100'
```

### Convert from base:
```python
int('64', 8)    # 52
int('100', 2)   # 4
int('ff', 16)   # 255
```

---

## 🔁 Bitwise Shifts

```python
3 << 2   # 12 (3 * 4)
8 >> 1   # 4  (8 // 2)
```

---

## 🎲 `random` Module

```python
import random

random.randint(1, 10)     # random int
random.choice([1, 2, 3])  # random element
random.shuffle(my_list)  # shuffle list in-place
```

---

## 💰 Floating Point Accuracy

```python
0.1 + 0.1 + 0.1 == 0.3     # ❌ False
```

### ✅ Use `decimal`
```python
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')  # Decimal('0.0')
```

### ✅ Use `fractions`
```python
from fractions import Fraction
Fraction(2, 7)   # exact fraction
```

---

## 🧮 Set Operations

```python
{1, 2} & {2, 3}     # {2}
{1, 2} | {3}        # {1, 2, 3}
{1, 2} - {1, 2}     # set()
```

### ❗ Empty set:
```python
type({})    # dict ❌
set()       # ✅ empty set
```

---

## ✅ `bool` Type

```python
type(True)        # bool
True == 1         # True
False == 0        # True
True is 1         # False ❗

True + 4          # 5
False + 3         # 3
```

---
