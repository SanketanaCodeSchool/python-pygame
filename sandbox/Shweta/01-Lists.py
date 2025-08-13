#Data Structure
#List
#Tuple
#set
#Dictionary
fruits = ["Mango", "Apple", "Strawberry", "Oranges", "Pineapple", "KIWI", "Guava"]
print("Original list:")
for i in fruits:
    print(i)

fruits[1] = "Melon"
print()
x = input("Please enter your favourite fruit: ")
fruits.append("Watermelon")
fruits.append(x)
print("After update: ")
for i in fruits:
    print(i)



