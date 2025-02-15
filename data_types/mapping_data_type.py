person = {"name": "franka", "age": 25, "height":6.4}

# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.get("name"))
height = person.pop("height")
print(height)
person.update({"name":"chile", "age": 32, "gender": "male"})
print(person)