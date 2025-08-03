
# 🔄 Python — Inner Working of Loops

Quick notes and examples on how loops and iterators work under the hood.

---

## 🔁 For Loop Internals

```python
for x in iterable:
    # do something
```

Same as:

```python
it = iter(iterable)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
```

---

## 📄 Files Are Iterators

```python
f = open("file.txt")
next(f)      # ✅ works directly
```

- File objects implement `__iter__()` and `__next__()`  
- Can be looped and `next()`-ed directly

---

## 🧾 Lists Are Iterables (Not Iterators)

```python
lst = [1, 2, 3]
next(lst)      # ❌ TypeError

it = iter(lst)
next(it)       # ✅ 1
```

✅ Lists have `__iter__()`  
❌ But not `__next__()` until wrapped with `iter()`

---

## 🧭 `iter()` Starts at Beginning

```python
it = iter([10, 20, 30])
next(it)   # ➞ 10
next(it)   # ➞ 20
```

✅ Keeps internal position  
✅ Remembers progress in original object

---

## 🧠 Iterator Reads Live Data

```python
lst = [1, 2]
it = iter(lst)
lst[0] = 99
next(it)   # ➞ 99 (not 1!)
```

➡️ Iterator points to **same memory**

---

## ⚙️ `iter()` is `__iter__()`

```python
iter(lst)        # same as: lst.__iter__()
next(it)         # same as: it.__next__()
```

---

## 🔁 Dict Iterators

```python
D = {'a': 1, 'b': 2}
I = iter(D)        # ➞ dict_keyiterator
next(I)            # 'a'
next(I)            # 'b'
next(I)            # ❌ StopIteration
```

✅ Loops over keys  
✅ Dict is iterable, returns key iterator

---
