
# 🧵 Python String — Quick Revision Notes

Minimal examples for fast review.

---

## 📚 Basics

```python
s = "hello"
s[0]      # 'h'
s[-1]     # 'o'
s[1:4]    # 'ell'
```

---

## ✂️ Slicing

```python
num_list = "0123456789"

num_list[:]        # '0123456789'
num_list[3:]       # '3456789'
num_list[:7]       # '0123456'
num_list[0:7:2]    # '0246'
num_list[0:7:3]    # '036'
```

---

## 🛠️ Common String Methods + Examples

```python
s = "  Hello,World  "
s.lower()            # '  hello,world  '
s.upper()            # '  HELLO,WORLD  '
s.strip()            # 'Hello,World'
s.replace('o', '0')  # '  Hell0,W0rld  '
s.split(',')         # ['  Hello', 'World ']
'-'.join(['A', 'B']) # 'A-B'
s.startswith('  H')  # True
s.endswith('d  ')    # True
s.find('W')          # 8
```

---

## 🧾 `.format()` + count + string ↔ list

```python
"I ordered {} cups of {} chai".format(2, "Masala")
# 'I ordered 2 cups of Masala chai'

"banana".count('a')     # 3

"a,b,c".split(',')      # ['a', 'b', 'c']
'-'.join(['x', 'y'])    # 'x-y'
```

---

## 🔡 Escape Sequences & Raw Strings

```python
"He said, \"Masala chai\""     # He said, "Masala chai"

"Masala\nChai"      # newline
r"Masala\nChai"     # raw → shows 


path = r"c:\user\pwd"  # Windows path
```

---

## 🔍 Substring Check

```python
"masala" in "masala chai"     # True
"chai" not in "green tea"     # True
```

---
