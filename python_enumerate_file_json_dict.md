

### 🧾 Python Notes: `enumerate`, `File Handling`, `json`, `dict` vs JS Object

````markdown
# 🔁 enumerate() in Python

```python
colors = ['red', 'green', 'blue']

for i, color in enumerate(colors):
    print(i, color)
````

✅ Adds index to iterable
✅ Cleaner than using range
✅ Supports `start=1`

```python
enumerate(colors, start=1)
```

---

# 📂 File Handling

```python
# Open a file
f = open("file.txt", "r")   # modes: 'r', 'w', 'a', 'b'

# Read content
f.read()
f.readline()
f.readlines()

# Write content
f = open("file.txt", "w")
f.write("Hello")
f.writelines(["A\n", "B\n"])

f.close()  # Always close

# Recommended: use with
with open("file.txt") as f:
    content = f.read()
```

---

# 📦 json module

## ✅ Python → JSON

```python
import json

data = {"name": "Utkarsh", "age": 22}
s = json.dumps(data)
```

✅ `json.dump(data, file)` → write to file
✅ `json.dumps(obj)` → return JSON string

## ✅ JSON → Python

```python
obj = json.loads('{"name":"Utkarsh"}')
```

✅ `json.load(file)` → from file
✅ `json.loads(string)` → from string

---

# 🔄 JSON vs Python types

| JSON       | Python      |
| ---------- | ----------- |
| object     | dict        |
| array      | list, tuple |
| string     | str         |
| number     | int, float  |
| true/false | True, False |
| null       | None        |

---

# 🧱 Is Python dict like JavaScript Object?

✅ Yes conceptually, but:

| Feature  | Python dict         | JS object          |
| -------- | ------------------- | ------------------ |
| Key type | Any immutable type  | Always string      |
| Access   | d\["x"], d.get("x") | obj.x or obj\["x"] |

```python
user = {"name": "Utkarsh"}
user["name"]  # access
```

---


