
# 🎁 Python Decorators — Quick Revision Notes

Minimal and practical decorator examples for fast learning and revision.

---

## ✅ 1. Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
````

Output:

```
Before
Hello
After
```

---

## ⏱️ 2. Timer Decorator — Measure Execution Time

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} sec")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Done"

slow_function()
```

---

## 🐞 3. Debug Decorator — Log Calls, Args, Return

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@debug
def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

greet("Utkarsh", msg="Hi")
```

---

## 🧠 4. Cache Decorator — Memoization

```python
def cache(func):
    saved = {}

    def wrapper(*args):
        if args in saved:
            print(f"Returning cached result for {args}")
            return saved[args]
        print(f"Computing result for {args}")
        result = func(*args)
        saved[args] = result
        return result

    return wrapper

@cache
def slow_add(x, y):
    print("Actually adding...")
    return x + y

slow_add(2, 3)
slow_add(2, 3)
slow_add(4, 5)
```

---

✅ Great for reducing repeated computation
✅ Only works with **hashable** arguments

---


