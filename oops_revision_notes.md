# 🧱 Python OOP — Full Revision Notes

Everything you need to revise Object-Oriented Programming in Python.

---

## 📦 Class & Object Basics

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

p = Person("Utkarsh")
p.greet()   # "Hello, Utkarsh"
```

---

## 🔁 Constructor: `__init__`

Automatically called when object is created. Used to initialize attributes.

---

## ⚖️ Instance vs Class Variables

```python
class Counter:
    count = 0          # class variable

    def __init__(self):
        self.id = Counter.count   # instance variable
        Counter.count += 1
```

---

## 🧬 Inheritance + `super()`

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"
```

---

## 🔐 Access Modifiers

```python
class Demo:
    def __init__(self):
        self.name = "Public"
        self._id = 123          # protected
        self.__secret = "Top"   # private

d = Demo()
d.name          # ✅
d._id           # ⚠️
d._Demo__secret # ✅ (name mangling)
```

---

## 🧰 Method Types

```python
class Example:
    def instance_method(self): pass

    @classmethod
    def class_method(cls): pass

    @staticmethod
    def static_method(): pass
```

---

## 🏠 `@property` Decorator

```python
class Circle:
    def __init__(self, r):
        self._r = r

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, val):
        if val > 0:
            self._r = val
```

---

## 🧠 Polymorphism

```python
class Dog:
    def speak(self): return "Woof"
class Cat:
    def speak(self): return "Meow"

for pet in [Dog(), Cat()]:
    print(pet.speak())  # Polymorphism
```

---

## ⚔️ Operator Overloading

```python
class Point:
    def __init__(self, x): self.x = x
    def __add__(self, other): return Point(self.x + other.x)
```

---

## 📣 `__str__` vs `__repr__`

```python
def __str__(self): return "User string"
def __repr__(self): return "Debug string"
```

---

## 🚮 Destructor `__del__`

```python
def __del__(self):
    print("Object destroyed")
```

---

## 🔎 `isinstance()` and `issubclass()`

```python
isinstance(obj, Class)      # True
issubclass(Child, Parent)   # True
```

---

## 🧩 Full Example (All Concepts)

```python
class Account:
    bank_name = "BankPython"              # class variable

    def __init__(self, name, balance):
        self.name = name                  # instance variable
        self._balance = balance           # protected
        self.__pin = "1234"               # private

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amt):
        if amt >= 0:
            self._balance = amt

    def __str__(self):
        return f"Account({self.name})"

    def __del__(self):
        print(f"Account {self.name} closed.")

    def display(self):
        return f"{self.name} has ₹{self._balance}"

    @staticmethod
    def bank_policy():
        return "Minimum balance must be ₹1000"

class SavingsAccount(Account):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest

    def display(self):
        return f"{self.name} earns {self.interest}% interest"

# Polymorphism
def show_account_info(account):
    print(account.display())

# Usage
acc1 = SavingsAccount("Utkarsh", 5000, 5.5)
acc2 = Account("Guest", 3000)

print(acc1.balance)
acc1.balance = 6000
print(Account.bank_policy())
show_account_info(acc1)
print(isinstance(acc1, Account))       # True
print(issubclass(SavingsAccount, Account))  # True
```
