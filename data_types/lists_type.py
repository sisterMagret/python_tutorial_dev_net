numbers = [2,3,8,1,1,3,9]
mixed_types = ["frank", 23, 6.5, True, None, [], (3,), {"name":"chile"}]

# (numbers.append(mixed_types))
# popped = numbers.pop(-1)
# print(numbers[0:5])
# for num in numbers:
#     print(num)

# numbers.extend(mixed_types)
numbers.remove(8)
print(numbers.sort())