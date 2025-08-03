
# 🧵 Tuples & Dictionaries — Python Quick Notes

Minimal, example-focused for revision.

---

## 📦 Tuple Basics

```python
t = (1, 2, 3)
t[0]         # 1
t[-1]        # 3
```

✅ Tuples are immutable  
```python
t[0] = 10    # ❌ TypeError
```

---

## ➕ Tuple Concatenation

```python
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
# ➞ (1, 2, 3, 4)
```

---

## 📤 Tuple Unpacking

```python
t = (1, 2, 3)
a, b, c = t
# a = 1, b = 2, c = 3
```

---

## 🧯 Unpacking in Other Types

```python
a, b = [1, 2]         # list
x, y = "hi"           # string
a, b = {10, 20}       # set (order not guaranteed)
for k, v in d.items():  # dict items
    ...
```

---

## 📦 Tuple Packing & Unpacking Together

```python
a, b = (1, 2)
# a → 1, b → 2
```

---

## 🧰 Tuple Methods

```python
t = (1, 2, 3, 2)
t.count(2)    # 2
t.index(3)    # 2
```

---

## 📚 Dictionary Basics

```python
d = {"a": 1, "b": 2}
d["a"]         # 1
d["b"] = 10    # update
```

✅ Keys must be immutable (str, int, tuple)

---

## 🆚 .get() vs []

```python
d.get("x")        # None
d.get("x", 0)     # 0
d["x"]            # ❌ KeyError if not present
```

---

## 🔁 Looping in Dict

```python
for key in d:           # keys
for val in d.values():  # values
for k, v in d.items():  # key-value pairs
```

---

## 🧰 Dict Methods

```python
d.keys()       # dict_keys
d.values()     # dict_values
d.items()      # dict_items
d.pop("a")     # removes 'a'
d.update({"c": 3})
d.clear()      # empties dict
d.popitem()    # removes last item (3.7+)
del d["b"]     # delete key
```

---

## 📋 .copy() to Avoid Reference

```python
a = {"x": 1}
b = a
b["x"] = 99
# a → {'x': 99} ❌

c = a.copy()
c["x"] = 100
# a → {'x': 99}, c → {'x': 100'}
```

---

## 🧱 Nested Dict

```python
users = {
  "alice": {"age": 25},
  "bob": {"age": 30}
}
users["alice"]["age"]  # 25
```

---

## ⚡ Dict Comprehension

```python
{x: x*x for x in [1, 2, 3]}
# ➞ {1: 1, 2: 4, 3: 9}
```

---

## 🏗️ Create Dict from Lists

```python
keys = ['a', 'b']
values = [1, 2]
dict(zip(keys, values))  # {'a': 1, 'b': 2}
```

---

## 🆕 dict.fromkeys()

```python
dict.fromkeys(['a', 'b'], 0)
# ➞ {'a': 0, 'b': 0}
```

---

## 📊 Tuple vs List

| Feature     | List        | Tuple       |
|-------------|-------------|-------------|
| Syntax      | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable     | ✅ Yes      | ❌ No       |
| Methods     | More        | Fewer       |
| Use Case    | Dynamic     | Fixed data  |
| Memory      | More        | Less        |

---

## 🔒 Tuple Assignment Error

```python
t = (1, 2)
t[0] = 10    # ❌ TypeError
```

---
