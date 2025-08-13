inventory = {}

while True:
    print("\nOptions:")
    print("1. Add item")
    print("2. Update quantity")
    print("3. Check item availability")
    print("4. Display inventory")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        quantity = int(input(f"Enter quantity for {item}: "))
        inventory[item] = quantity
    elif choice == 2:
        item = input("Enter item to update: ")
        if item in inventory:
            quantity = int(input(f"Enter new quantity for {item}: "))
            inventory[item] = quantity
        else:
            print(f"{item} not found in inventory.")
    elif choice == 3:
        item = input("Enter item to check: ")
        print(f"{item} is {'available' if item in inventory else 'not available'}.")
    elif choice == 4:
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    elif choice == 5:
        break
    else:
        print("Invalid choice! Try again.")
