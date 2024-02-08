s = {1, 3, 6, 9, 1}
print(s)
s.add(10)  # add method
# s.pop()                # pop the randoem element
# s.remove(3)            # Remove the element
s2 = {2, 4, 6, 8, 10}
s.update(s2)  # update the set
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

ro = set()
print(type(ro))
print(ro)

rohit = {1}
print(type(rohit))
print(rohit)

rohit = {}
print(type(rohit))
print(rohit)

r = []
print(type(r))
print(r)

t = ()
print(type(t))
print(t)

for value in info:
  print(value)
