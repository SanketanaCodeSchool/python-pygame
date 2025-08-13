# Lesson 1 Homework - Lists Practice
# Complete Solutions

# ============================================================================
# TASK 1: Personal Information Manager
# ============================================================================

# Create lists
favorite_movies = ["The Matrix", "Inception", "Interstellar", "The Dark Knight", "Pulp Fiction"]
favorite_foods = ["Pizza", "Sushi", "Pasta", "Burgers", "Ice Cream"]
hobbies = ["Reading", "Gaming", "Cooking"]

# Print original lists
print("My Favorite Movies:")
for i, movie in enumerate(favorite_movies, 1):
    print(f"{i}. {movie}")

print("\nMy Favorite Foods:")
for i, food in enumerate(favorite_foods, 1):
    print(f"{i}. {food}")

print("\nMy Hobbies:")
for i, hobby in enumerate(hobbies, 1):
    print(f"{i}. {hobby}")

# Add one new item to each list
favorite_movies.append("Avatar")
favorite_foods.append("Tacos")
hobbies.append("Photography")

# Remove one item from each list
favorite_movies.remove("Pulp Fiction")
favorite_foods.remove("Burgers")
hobbies.remove("Gaming")

# Print updated lists
print("\nUpdated Lists:")
print("Updated Movies:", favorite_movies)
print("Updated Foods:", favorite_foods)
print("Updated Hobbies:", hobbies)

# ============================================================================
# TASK 2: Number Analyzer
# ============================================================================

# Create a list of 10 numbers
numbers = [23, 45, 12, 67, 89, 34, 56, 78, 90, 11]

# Calculate and display statistics
# Sum
total = sum(numbers)
print(f"Sum: {total}")

# Average
average = total / len(numbers)
print(f"Average: {average:.2f}")

# Highest and lowest
highest = max(numbers)
lowest = min(numbers)
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

# Count even and odd numbers
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = len(numbers) - even_count
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")

# Sort and reverse the list
sorted_numbers = sorted(numbers)
reversed_numbers = sorted(numbers, reverse=True)

print(f"Sorted: {sorted_numbers}")
print(f"Reversed: {reversed_numbers}")

# ============================================================================
# TASK 3: Word Processor
# ============================================================================

# Create a list of words
words = ["python", "programming", "computer", "algorithm", "database", "network", "software", "developer"]

# Display original list
print("Original words:", words)

# Find longest and shortest words
longest_word = max(words, key=len)
shortest_word = min(words, key=len)
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortest_word}")

# Count words by starting letter
letter_counts = {}
for word in words:
    first_letter = word[0].upper()
    letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1

print("Words by starting letter:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")

# Create new list with long words
long_words = [word for word in words if len(word) > 4]
print("Words longer than 4 characters:", long_words)

# ============================================================================
# BONUS CHALLENGE: To-Do List Manager
# ============================================================================

def todo_list_manager():
    todo_list = []
    
    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display all tasks")
        print("4. Count tasks")
        print("5. Check if task exists")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            task = input("Enter task to add: ")
            todo_list.append(task)
            print(f"Added: {task}")
            
        elif choice == "2":
            if todo_list:
                task = input("Enter task to remove: ")
                if task in todo_list:
                    todo_list.remove(task)
                    print(f"Removed: {task}")
                else:
                    print("Task not found!")
            else:
                print("No tasks to remove!")
                
        elif choice == "3":
            if todo_list:
                print("All tasks:")
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks in the list!")
                
        elif choice == "4":
            print(f"Total tasks: {len(todo_list)}")
            
        elif choice == "5":
            task = input("Enter task to check: ")
            if task in todo_list:
                print(f"'{task}' exists in the list!")
            else:
                print(f"'{task}' not found in the list!")
                
        elif choice == "6":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

# Uncomment to run the bonus challenge
# todo_list_manager()

print("\nHomework completed!")
