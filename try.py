student = {
    "name": "Sriram",
    "age": 21,
    "course": "Data Science"
}

print(student["name"])
print(student.get("age"))

student["city"] = "Chennai"
student["age"] = 22

print(student)

# student.pop("age")
# student.popitem()
# del student["name"]
# student.clear()
# print(student)
# print("name" in student)
# print("age" not in student)

# for key in student:
#     print(key)

# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(key, value)

print(student.keys())        # all keys
print(student.values())      # all values
print(student.items())       # key-value pairs

print(student.get("name"))   # safe access

student.update({"age": 25}) # update dictionary

print(student.pop("age")) # remove key
print(student)
student.popitem() # remove last inserted
print(student)
student.clear() # remove all
print(student)
student.copy() # shallow copy
print(student)

print(dict.fromkeys(["a", "b"], 0)) # create new dict