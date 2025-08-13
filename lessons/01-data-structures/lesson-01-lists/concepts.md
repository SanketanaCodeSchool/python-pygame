# Lesson 1: Data Structures - Lists

## Learning Objectives
- Understand what lists are and their basic properties
- Learn how to create and initialize lists
- Master basic list operations (accessing, adding, removing elements)
- Practice with list indexing and slicing

## What are Lists?

Lists are one of Python's most versatile data structures. They are ordered collections of items that can store different types of data.

### Key Characteristics
- **Ordered**: Items maintain their position
- **Mutable**: Can be changed after creation
- **Indexed**: Access items by position (0-based)
- **Heterogeneous**: Can store different data types

## Creating Lists

```python
# Empty list
my_list = []

# List with items
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]

# Using list() constructor
letters = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
```

## Accessing List Elements

```python
fruits = ["apple", "banana", "orange", "grape"]

# First element (index 0)
first = fruits[0]  # "apple"

# Last element
last = fruits[-1]  # "grape"

# Negative indexing
second_last = fruits[-2]  # "orange"

# Slicing
subset = fruits[1:3]  # ["banana", "orange"]
first_two = fruits[:2]  # ["apple", "banana"]
last_two = fruits[-2:]  # ["orange", "grape"]
```

## Common List Operations

### Adding Items
```python
numbers = [1, 2, 3]

# Append to end
numbers.append(4)  # [1, 2, 3, 4]

# Insert at position
numbers.insert(1, 1.5)  # [1, 1.5, 2, 3, 4]

# Extend with another list
numbers.extend([5, 6])  # [1, 1.5, 2, 3, 4, 5, 6]
```

### Removing Items
```python
fruits = ["apple", "banana", "orange", "apple"]

# Remove first occurrence
fruits.remove("apple")  # ["banana", "orange", "apple"]

# Remove and return last item
last_fruit = fruits.pop()  # "apple", fruits = ["banana", "orange"]

# Remove by index
del fruits[0]  # fruits = ["orange"]
```

### Finding Items
```python
numbers = [3, 1, 4, 1, 5, 9]

# Find position
position = numbers.index(4)  # 2

# Count occurrences
count = numbers.count(1)  # 2

# Check if exists
exists = 5 in numbers  # True
```

## List Length and Iteration

```python
fruits = ["apple", "banana", "orange"]

# Length
length = len(fruits)  # 3

# Iteration
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

## Practical Examples

### Shopping List
```python
shopping_list = ["milk", "bread", "eggs", "butter"]

# Add item
shopping_list.append("cheese")

# Check if item exists
if "milk" in shopping_list:
    print("Milk is on the list!")

# Remove bought item
shopping_list.remove("bread")
```

### Student Grades
```python
grades = [85, 92, 78, 96, 88]

# Calculate average
average = sum(grades) / len(grades)

# Find highest grade
highest = max(grades)

# Sort grades
sorted_grades = sorted(grades)
```

## Common Mistakes to Avoid

1. **Index out of range**: Always check list length before accessing
2. **Forgetting 0-based indexing**: First element is at index 0, not 1
3. **Modifying list while iterating**: Can cause unexpected behavior
4. **Using = for copying**: Use `.copy()` or `list()` for true copies

## Best Practices

- Use descriptive variable names
- Keep lists focused on one type of data when possible
- Use list comprehensions for simple transformations
- Consider using `in` operator for membership testing
- Document your code with comments
