
# 🔧 Python Functions — Quick Revision Notes

Minimal and essential notes for mastering functions.

---

## 🧱 Function Basics

```python
def greet(name):
    return "Hello " + name
```

---

## ⚙️ Default Arguments

```python
def greet(name="Guest"):
    return "Hello " + name
```

---

## 📦 *args and **kwargs

```python
def add(*nums): return sum(nums)
def show(**info): print(info)
```

Looping over kwargs:
```python
for key, value in info.items():
    print(key, value)
```

---

## ⚡ Lambda Functions

```python
square = lambda x: x * x
list(map(lambda x: x*2, [1,2,3]))  # ➞ [2,4,6]
```

---

## 🔁 Returning Multiple Values

```python
def stats(x, y):
    return x + y, x * y
```

---

## 🌐 Scope

```python
x = 10
def func():
    x = 5  # local
```

Modify global:
```python
global x
```

---

## 🔁 yield — Generator Function

```python
def even_up_to(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
```

---

## 📚 Docstring

```python
def greet(): 
    """Returns greeting"""
```

---

## 🧠 First-Class Functions

```python
def shout(msg): return msg.upper()
def speak(func): return func("hi")
```

---

## 🧬 Nested Functions

```python
def outer():
    def inner():
        return "Inner"
    return inner()
```

---

## 🔒 Closures

```python
def outer(x):
    def inner():
        return x + 1
    return inner
```

---

## 🎁 Decorator (Intro)

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def say_hi(): print("Hi")
```

---
