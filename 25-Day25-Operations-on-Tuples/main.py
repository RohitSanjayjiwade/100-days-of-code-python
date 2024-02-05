countries = ("United States", "Canada", "Mexico", "Brazil", "Argentina")
print(countries)

temp = list(countries)
print(temp)

temp.append("India")
print(temp)

temp.pop(4)
print(temp)

temp.remove("Mexico")
print(temp)

temp[2] = "China"
print(temp)

countries = tuple(temp)

print(countries)

countries2 = ("India", "Pakistan", "Nepal")
countries3 = countries + countries2
print(countries3)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print("Count of 3 in tuple1 is:", res)

res = tuple1.index(3)
print("First occurrence of 3 is", res)

res = tuple1.index(3, 6, 8)
print("First occurrence of 3 is", res)
