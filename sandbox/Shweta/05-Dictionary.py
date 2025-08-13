my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1990
}

print(type(my_dict))
print(my_dict)
print(my_dict["model"])
print(my_dict.get("year"))
my_dict["year"] = 2000

print(my_dict.get("year"))
for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

for i,j in my_dict.items():
    print(f"{i} : {j}")

my_dict['wheel_type'] = "MRF"

print(my_dict)

my_dict.pop("model")
print(my_dict)

my_dict.popitem()
print(my_dict)

del my_dict["year"]
print(my_dict)

#del my_dict
my_dict.clear()
print(my_dict)