print("topic covered are: dictionaries and set")

person1_dict = {
    "id": 1,
    "name": "John",
    "country": "USA",
    "is_Employed": True,
    "city": "NY"
}

print(f"dictionary : {person1_dict}")

key_set = set(person1_dict.keys())
print(f"key_set: {key_set}")

print("\n--- printing dictionary(key, value) with for loop ---\n")

for key, value in person1_dict.items():
    print(f"{key} : {value}")

print("\n--- printing dictionary keys with for loop ---\n")

for key in person1_dict.keys():
    print(f"key: {key}")
    
print("\n--- printing dictionary values with for loop ---\n")

for value in person1_dict.values():
    print(f"value: {value}")
    
print("\n--- deleting key in dictionary ---\n")

del person1_dict["city"]
print(person1_dict)

set_1 = {1, 2, 3, 4}
set_2 = {2, 4, 5, 7, 8}

print(set_1)

set_1.add(5)
print(set_1)

set_1.add(2)
set_1.add(2)
set_1.add(2)
print(set_1)

set_1.remove(1)
print(set_1)

print(set_1 | set_2) # union
print(set_1 & set_2) # intersection
print(set_1 - set_2) # exists in 1st set and not in 2nd


# declare an empty set
empty_set = set()
empty_set.add(1)
empty_set.add(2)
print(empty_set)
# output: {1, 2}












