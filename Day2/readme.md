# Day 2
## Typecasting, Lists, and Tuples in Python
---

## **1. Typecasting**
Typecasting refers to converting one data type to another. There are two types:

### **Implicit Typecasting**
- Python automatically converts smaller data types to larger ones.
- Example:
  ```python
  num_int = 25
  num_float = 2.5
  result = num_int + num_float  # Implicitly converted to float
  print(type(result))  # Output: <class 'float'>
  ```

### **Explicit Typecasting**
- Manually converting one data type into another using functions like `int()`, `float()`, `str()`.
- Example:
  ```python
  value1 = int(input("Enter first value: "))
  print(type(value1))  # Output: <class 'int'>
  ```

---

## **2. Lists**
A list is a mutable, ordered collection that allows duplicate values and multiple data types.

### **List Methods:**
| Method | Description |
|--------|------------|
| `append(x)` | Adds an element `x` to the end of the list. |
| `insert(i, x)` | Inserts `x` at index `i`. |
| `remove(x)` | Removes the first occurrence of `x`. |
| `pop(i)` | Removes element at index `i` (default is last). |
| `sort(reverse=True)` | Sorts list in ascending order (descending if `reverse=True`). |
| `count(x)` | Returns the count of `x` in the list. |
| `copy()` | Creates a shallow copy of the list. |
| `extend(iterable)` | Adds elements from an iterable to the list. |
| `len(list)` | Returns the length of the list. |

### **Example List Usage:**
```python
fruits = ["Apple", "Banana", "Pineapple"]
fruits.append("Mango")
print(fruits)
```

---

## **3. Tuples**
A tuple is an immutable, ordered collection that allows duplicate values.

### **Tuple Methods:**
| Method | Description |
|--------|------------|
| `count(x)` | Returns the count of `x` in the tuple. |
| `index(x)` | Returns the first index of `x`. |
| `len(tuple)` | Returns the number of elements in the tuple. |

### **Example Tuple Usage:**
```python
colors = ("Red", "Green", "Blue")
print(colors[1])  # Accessing element
```

### **Tuple Unpacking:**
It is same like destructring in object in typescript.

```python
color1, color2, color3 = colors
print(color1, color2, color3)
```

---

## **4. Key Differences Between Lists and Tuples**
| Feature | List | Tuple |
|---------|------|-------|
| Mutability | Mutable | Immutable |
| Performance | Slower | Faster |
| Syntax | `[]` | `()` |
| Methods | More methods available | Fewer methods |

---

### **Conclusion:**
- Use **lists** when you need a dynamic collection that can change over time.
- Use **tuples** when you need an immutable collection that should remain constant.

Happy Coding! 🚀

