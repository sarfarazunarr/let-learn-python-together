# Python Code Demonstrating Typecasting, Lists, and Tuples

# ---------- TYPECASTING ----------

# Implicit Typecasting
# Python automatically converts smaller data types to larger ones
num_int = 25  # Integer
num_float = 2.5  # Float
result = num_int + num_float  # Implicitly converted to float
print(type(result))  # Output: <class 'float'>

# Explicit Typecasting
# Manually converting one data type into another
value1 = int(input("Enter first value: "))  # Input is always a string; converting it to int
print(value1)
print(type(value1))

# ---------- LISTS ----------
# Lists are mutable, ordered collections that allow duplicate values and multiple data types
fruits = ["Apple", "Banana", "Pineapple", "Apple", 12, 33, 3.4, False, True, (1, 2), [12, 2, 23]]
values = [2, 5, 3, 6, 8, 1]
friends = list(("irfan", "mustafain", "saqib", 12, 22))  # Using list constructor

# Accessing list elements
print(fruits[-1][1])  # Accessing nested list element

# Adding elements to the list
friends.append("Zakir")
print(friends)  # Updated list

# Getting length and type
print(len(friends))  # Length of list
print(type(friends))  # Type of list

# Updating and removing elements
fruits[1] = "B"  # Updating an element
fruits.pop(2)  # Removing an element by index
print(fruits.count("Apple"))  # Counting occurrences of "Apple"

# Looping through a list
for item in fruits:
    print(f"{item} is delicious")

# Sorting a list
values.sort(reverse=True)  # Sorts list in descending order
print(values)

# Copying a list
new_copy = values.copy()  # Creates a new independent copy
values[1] = 12  # Modifying original list
print(values)  # Original List
print(new_copy)  # Copy remains unchanged

# Joining two lists
final_list = friends + fruits  # Merging two lists
print(final_list)

# ---------- TUPLES ----------
# Tuples are immutable, ordered collections that allow duplicate values
colors = ("Red", "Green", "Blue", "Black")
print(colors)

# Accessing tuple elements
print(colors[1])

# Updating a tuple (Not Recommended, but possible via conversion)
temp = list(colors)  # Convert tuple to list
temp[0] = "Blue"  # Modify element
colors = tuple(temp)  # Convert back to tuple
print(colors)

# Unpacking a tuple
color1, color2, color3, color4 = colors
print(color1, color2, color3, color4)

# Looping through a tuple
for color in colors:
    print(color)

# Tuple Methods
# Count occurrences of an element
print(colors.count("Blue"))

# Find the index of an element
print(colors.index("Green"))
