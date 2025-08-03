
# 📦 Python List — Quick Revision Notes

Minimal, clear examples for fast review.

---

## 📚 Basics

```python
lst = [1, 2, 3]
lst[0]        # 1
lst[-1]       # 3
lst[1:3]      # [2, 3]
lst[0] = 10   # ➞ [10, 2, 3] (lists are mutable)
```

---

## ✂️ Slice Assignment

```python
tea = ['Black', 'Green', 'Oolong', 'Herbal']
tea[1:2] = "Lemon"
# ➞ ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']

tea[1:2] = ["Lemon"]
# ➞ ['Black', 'Lemon', 'Oolong', 'Herbal']
```

---

## ➕ Insert / ❌ Remove with Slice

```python
tea[1:1] = ["test", "test"]  
# ➞ insert at index 1

tea[1:3] = []  
# ➞ remove elements at index 1 & 2
```

---

## 🧰 Common Methods

```python
lst = [3, 1, 2]

lst.append(4)      # ➞ [3, 1, 2, 4]
lst.insert(1, 10)  # ➞ [3, 10, 1, 2, 4]
lst.remove(1)      # ➞ removes first 1
lst.pop()          # ➞ removes last
lst.sort()         # ➞ [2, 3, 10]
lst.reverse()      # ➞ [10, 3, 2]
lst.index(3)       # ➞ 1
lst.count(2)       # ➞ 1
```

---

## 🧠 Memory Reference

```python
a = [1, 2, 3]
b = a
b[0] = 100
# a ➞ [100, 2, 3] ❌ (same memory)
```

### ✅ Use `.copy()` to avoid this:

```python
c = a.copy()
c[0] = 0
# a ➞ [100, 2, 3], c ➞ [0, 2, 3]
```

---

## ⚡ List Comprehension

```python
[x*x for x in range(5)]            # [0, 1, 4, 9, 16]
[x for x in range(5) if x % 2]     # [1, 3]
[x.upper() for x in ['a', 'b']]    # ['A', 'B']
```

Syntax:
```python
[expression for item in iterable if condition]
```

---
