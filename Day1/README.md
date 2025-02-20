# Day 1 - Introduction to Python

## Overview
Today, we will cover the basics of Python programming, including installation, introduction, variables, printing output, and data types.

---

## 1. Python Installation
To get started with Python, follow these steps:

### Windows:
1. Download Python from the [official Python website](https://www.python.org/downloads/).
2. Run the installer and check "Add Python to PATH".
3. Verify installation using:
   ```sh
   python --version
   ```

---

## 2. Short Introduction of Python
Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used in web development, data science, automation, and more.

### Features of Python:
- Easy to learn and use
- Open-source and community-driven
- Cross-platform compatibility
- Extensive libraries and frameworks

#### Example Python Program:
```python
print("Hello, World!")
```

---

## 3. Variables in Python
Variables are used to store data in Python.

### Declaring Variables:
```python
name = "Sarfaraz"
age = 25
height = 5.6
```

### Variable Naming Rules:
- Must start with a letter or underscore (`_`).
- Cannot start with a number.
- Can only contain alphanumeric characters and underscores.

---

## 4. Printing Output
Python uses the `print()` function to display output.

### Example:
```python
print("Welcome to Python!")
```

### Printing Multiple Variables:
```python
name = "Sarfaraz"
age = 25
print("Name:", name, "| Age:", age)
```
#### Additional Parameters in print function
**sep** this argument requires a character that will be added between different parameters added in print function.
```python
print(name, age, sep=",")
```
**end** this argument requires a character that will be added in the end of output. Default value of `end` is `/n` 
```python
print(name, age, sep=",", end=" ") 
print("I am active") # this print output will be displayed in the same line of above print output
```

---

## 5. Data Types in Python
Python has several built-in data types:

| Data Type | Example |
|-----------|---------|
| String (`str`) | `"Hello"` |
| Integer (`int`) | `100` |
| Float (`float`) | `10.5` |
| Boolean (`bool`) | `True`, `False` |
| List (`list`) | `[1, 2, 3]` |
| Tuple (`tuple`) | `(1, 2, 3)` |
| Dictionary (`dict`) | `{"name": "Alice", "age": 25}` |
| Set (`set`) | `{1, 2, 3}` |

### Example Usage:
```python
x = "Hello"  # String
y = 10       # Integer
z = 3.14     # Float
flag = True  # Boolean

print(type(x), type(y), type(z), type(flag))
```


## Conclusion
This session introduced Python basics, including installation, variables, printing output, and data types. Understanding these concepts is fundamental for further learning.

Happy Coding! 🚀
