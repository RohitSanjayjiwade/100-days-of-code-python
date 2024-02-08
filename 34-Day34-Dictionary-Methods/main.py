info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info.update({'age': 20})
info.update({'DOB': 2001})
print(info)

# info.clear()
# print(info)

# info.pop('eligible')
# print(info)

# info.popitem()
# print(info)

del info['age']
print(info)

emp = {122: 45, 123: 89, 567: 69, 670: 69}

emp1 = {222: 67, 566: 90}

emp.update(emp1)
print(emp)

emp.update({122: 200})
print(emp)
