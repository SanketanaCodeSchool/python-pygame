# Lesson 1: Data Structures - Lists
# Classwork Exercises and Solutions

# ============================================================================
# EXERCISE 1: Creating and Accessing Lists
# ============================================================================

"""
Exercise 1: Create a list of your favorite colors and access different elements
"""

# Student Task: Create a list of 5 favorite colors
# colors = [your colors here]

# Solution:
colors = ["blue", "green", "red", "purple", "yellow"]

# Task: Print the first color
print("First color:", colors[0])

# Task: Print the last color
print("Last color:", colors[-1])

# Task: Print colors from index 1 to 3
print("Colors 1-3:", colors[1:4])

# ============================================================================
# EXERCISE 2: List Operations
# ============================================================================

"""
Exercise 2: Practice adding and removing items from a list
"""

# Start with an empty list
fruits = []

# Task: Add fruits one by one
fruits.append("apple")
fruits.append("banana")
fruits.insert(1, "orange")  # Insert at position 1
fruits.extend(["grape", "mango"])

print("Fruits list:", fruits)

# Task: Remove "banana" and print the last fruit
fruits.remove("banana")
last_fruit = fruits.pop()
print("Removed fruit:", last_fruit)
print("Updated fruits:", fruits)

# ============================================================================
# EXERCISE 3: List Methods and Functions
# ============================================================================

"""
Exercise 3: Use list methods and functions to analyze data
"""

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Task: Find the length of the list
length = len(numbers)
print("List length:", length)

# Task: Count how many times 5 appears
count_5 = numbers.count(5)
print("Number of 5s:", count_5)

# Task: Find the position of the first 4
position_4 = numbers.index(4)
print("Position of first 4:", position_4)

# Task: Check if 7 is in the list
has_7 = 7 in numbers
print("Contains 7:", has_7)

# ============================================================================
# EXERCISE 4: List Iteration
# ============================================================================

"""
Exercise 4: Iterate through lists in different ways
"""

animals = ["cat", "dog", "bird", "fish", "hamster"]

# Task: Print all animals
print("All animals:")
for animal in animals:
    print(f"- {animal}")

# Task: Print animals with their index
print("\nAnimals with index:")
for i, animal in enumerate(animals):
    print(f"{i}: {animal}")

# Task: Print only animals with even indices
print("\nAnimals with even indices:")
for i in range(0, len(animals), 2):
    print(f"{i}: {animals[i]}")

# ============================================================================
# EXERCISE 5: Practical Application - Shopping List
# ============================================================================

"""
Exercise 5: Create a shopping list manager
"""

# Initialize shopping list
shopping_list = ["milk", "bread", "eggs"]

# Task: Add more items
shopping_list.extend(["butter", "cheese", "tomatoes"])

# Task: Check if "milk" is in the list
if "milk" in shopping_list:
    print("Milk is already in the shopping list!")
else:
    print("Adding milk to shopping list...")
    shopping_list.append("milk")

# Task: Remove "bread" and add "whole wheat bread"
shopping_list.remove("bread")
shopping_list.append("whole wheat bread")

# Task: Print final shopping list
print("\nFinal shopping list:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

# Task: Calculate total items
total_items = len(shopping_list)
print(f"\nTotal items to buy: {total_items}")

# ============================================================================
# EXERCISE 6: Challenge - Grade Calculator
# ============================================================================

"""
Exercise 6: Create a grade calculator using lists
"""

# Sample grades
grades = [85, 92, 78, 96, 88, 91, 75, 89]

# Task: Calculate average grade
average = sum(grades) / len(grades)
print(f"Average grade: {average:.2f}")

# Task: Find highest and lowest grades
highest = max(grades)
lowest = min(grades)
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")

# Task: Count grades above 90
above_90 = sum(1 for grade in grades if grade > 90)
print(f"Grades above 90: {above_90}")

# Task: Create a list of grades that need improvement (< 80)
needs_improvement = [grade for grade in grades if grade < 80]
print(f"Grades needing improvement: {needs_improvement}")

# ============================================================================
# BONUS EXERCISE: List Manipulation
# ============================================================================

"""
Bonus Exercise: Advanced list operations
"""

# Start with a mixed list
mixed_list = [1, "hello", 3.14, True, "world", 42]

# Task: Separate numbers and strings
numbers = []
strings = []

for item in mixed_list:
    if isinstance(item, (int, float)):
        numbers.append(item)
    elif isinstance(item, str):
        strings.append(item)

print("Numbers:", numbers)
print("Strings:", strings)

# Task: Create a new list with only unique items
original = [1, 2, 2, 3, 4, 4, 5]
unique = []
for item in original:
    if item not in unique:
        unique.append(item)

print("Original:", original)
print("Unique:", unique)
