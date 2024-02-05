tup = (1,2,3,4,5,6,7,8,9,10,10)
print(type(tup),tup)

tup2 = (1,)
print(type(tup2),tup2)

# tup[0] = 90  # Not allowed / It is Immutable

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
# print(tup[60])
print(len(tup))
print(tup[-4])


if 10 in tup:
  print("Yes 10 is present in this tuple")
else:
  print("No 10 is not present in this tuple")

tup2 = tup[1:4]
print(tup2)