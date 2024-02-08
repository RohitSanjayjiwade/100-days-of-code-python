info = {'name': 'Rohit', 'age': 22, 'eligible': True}
print(info)

print(info['name'])
print(info.get("age"))

print(info.keys())
print(info.values())
print(info.items())

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")
  # print(f"The value corresponding to the key {key} is {info.get(key)}")

for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")
