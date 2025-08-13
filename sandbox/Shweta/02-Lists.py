fruits = ["Mango", "Apple", "Strawberry", "Oranges", "Pineapple", "KIWI", "Guava"]
'''
fruit_name = input("Enter a fruit name of your choice: ")
if fruit_name not in fruits:
    fruits.append(fruit_name)
else:
    print(f"{fruit_name} already exist in fruits list")

print(f"There are {len(fruits)} fruits in my basket")


fruits.remove("Oranges")
fruits.pop()
del fruits[1]
#del fruits
#fruits.clear()
fruits2 = fruits
fruits3 = fruits.copy()
print(fruits)
print(fruits2)
print(fruits3)'
'''

list1 = [4,1,3,4,4]
list2 = [1,2,3]

list3 = list1 + list2
list1.extend(list2)
print(list1)

print(list1.count(4))
print(list1.index(1))
list1.reverse()
print(list1)
list1.sort()
print(list1)