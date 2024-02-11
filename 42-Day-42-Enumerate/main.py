marks = [12, 56, 32, 98, 12,  45, 1, 4]

print(marks[:3:-1])

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Rohit, awesome!")
#   index +=1


for i, mark in enumerate(marks, start=1):
  print(i, mark)
  if(i == 3):
    print("Rohit, awesome!")


